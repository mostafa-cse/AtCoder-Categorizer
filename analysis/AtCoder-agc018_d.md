# Problem Analysis: AtCoder-agc018_d — D - Tree and Hamilton Path

**Problem ID**: `AtCoder-agc018_d`  
**Contest**: `agc018`  
**Rating / Difficulty**: 2758  
**URL**: https://atcoder.jp/contests/agc018/tasks/agc018_d  
**VJudge Tag**: `[problem:AtCoder-agc018_d]`  
**Category File**: [`../categories/data_structures_ds/tree_and_hamilton_path_centroid.md`](../categories/data_structures_ds/tree_and_hamilton_path_centroid.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Centroid Decomposition`  
- **Topic (Skill)**: `Centroid Decomposition`  

---

## 1. Problem Statement & Key Idea
Given a weighted tree of N vertices, construct a complete graph where the edge weight between u and v is their distance in the tree. Find the length of the longest Hamiltonian path in this complete graph.

## 2. Core Observation & Invariant
In any Hamiltonian cycle on the complete graph, every edge e of the tree can be traversed at most 2 * min(sz_e, N - sz_e) times. Rooting the tree at its centroid allows achieving this upper bound for all edges simultaneously, so the maximum Hamiltonian cycle length is L_{cycle} = sum_e 2 * min(sz_e, N - sz_e) * weight(e). A Hamiltonian path is obtained by removing one edge from the cycle. If the tree has two centroids C_1 and C_2 (separated by an edge with sz = N/2), every step in the cycle must cross the centroid edge, so the minimum omitted edge has weight equal to that centroid edge. If the tree has a unique centroid C, the omitted edge can be the shortest edge incident to C.

## 3. Step-by-Step Algorithm
1. 1. Find the centroid(s) of the tree using DFS subtree sizes.
2. 2. Re-root the tree at a centroid and compute L_{cycle} = sum 2 * min(sz[v], N - sz[v]) * w.
3. 3. If there are two centroids, subtract the weight of the edge connecting them.
4. 4. If there is a unique centroid, subtract the minimum weight of an edge incident to it.
5. 5. Output L_{cycle} - omitted_weight.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    long long w;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<int> sz(n + 1, 0);
    auto get_sz = [&](auto& self, int u, int p) -> int {
        int s = 1;
        for (const auto& e : adj[u]) {
            if (e.to != p) {
                s += self(self, e.to, u);
            }
        }
        sz[u] = s;
        return s;
    };
    get_sz(get_sz, 1, 0);

    vector<int> centroids;
    auto find_cent = [&](auto& self, int u, int p) -> void {
        bool is_c = true;
        for (const auto& e : adj[u]) {
            if (e.to != p) {
                self(self, e.to, u);
                if (sz[e.to] > n / 2) {
                    is_c = false;
                }
            }
        }
        if (n - sz[u] > n / 2) {
            is_c = false;
        }
        if (is_c) {
            centroids.push_back(u);
        }
    };
    find_cent(find_cent, 1, 0);

    // Root at centroid[0]
    int c = centroids[0];
    get_sz(get_sz, c, 0);

    long long L_cycle = 0;
    for (int u = 1; u <= n; ++u) {
        for (const auto& e : adj[u]) {
            int v = e.to;
            if (u < v) {
                int s = min(sz[u], sz[v]);
                L_cycle += 2LL * min(s, n - s) * e.w;
            }
        }
    }

    long long omit = 0;
    if (centroids.size() == 2) {
        int c1 = centroids[0];
        int c2 = centroids[1];
        for (const auto& e : adj[c1]) {
            if (e.to == c2) {
                omit = e.w;
                break;
            }
        }
    } else {
        omit = 1e18;
        for (const auto& e : adj[c]) {
            omit = min(omit, e.w);
        }
    }

    long long ans = L_cycle - omit;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
