# Problem Analysis: AtCoder-abc362_f — I. Perfect Matching on a Tree

**Problem ID**: `AtCoder-abc362_f`  
**Contest**: `abc362`  
**Rating / Difficulty**: 2186  
**URL**: https://atcoder.jp/contests/abc362/tasks/abc362_f  
**VJudge Tag**: `[problem:AtCoder-abc362_f]`  
**Category File**: [`../categories/data_structures/tree_centroid_cyclic_pairing_max_matching.md`](../categories/data_structures/tree_centroid_cyclic_pairing_max_matching.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Centroid Decomposition`  
- **Topic (Skill)**: `Centroid Decomposition`  

---

## 1. Problem Statement & Key Idea
In a complete graph whose edge weights are tree shortest path distances, construct a maximum weight matching of floor(N/2) pairs. The theoretical upper bound sum_e min(sz_e, N - sz_e) is achieved when all matched pairs cross the tree centroid.

## 2. Core Observation & Invariant
Root the tree at its centroid C. Every branch attached to C has size at most floor(N/2). In a DFS traversal order of vertices starting from C, offsetting by floor(N/2) places the partner of any vertex in a completely different branch (or at C). Thus, every pair (v_i, v_{i + floor(N/2)}) has its tree path passing through C, saturating every tree edge to its maximum possible crossing capacity.

## 3. Step-by-Step Algorithm
1. Find a tree centroid C by computing subtree sizes in DFS and selecting a vertex whose components after removal all have size <= N/2.
2. Perform a DFS traversal rooted at centroid C to construct a traversal array order of length N.
3. Set K = floor(N/2). Pair vertex order[i] with vertex order[i + K] for all 0 <= i < K.
4. Print the K pairs.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> sz(N + 1, 0);
    int centroid = 1;

    auto get_centroid = [&](auto& self, int u, int p) -> void {
        sz[u] = 1;
        bool is_c = true;
        for (int v : adj[u]) {
            if (v != p) {
                self(self, v, u);
                sz[u] += sz[v];
                if (sz[v] > N / 2) is_c = false;
            }
        }
        if (N - sz[u] > N / 2) is_c = false;
        if (is_c) centroid = u;
    };

    get_centroid(get_centroid, 1, 0);

    vector<int> order;
    order.reserve(N);

    auto dfs = [&](auto& self, int u, int p) -> void {
        order.push_back(u);
        for (int v : adj[u]) {
            if (v != p) {
                self(self, v, u);
            }
        }
    };

    dfs(dfs, centroid, 0);

    int K = N / 2;
    for (int i = 0; i < K; ++i) {
        cout << order[i] << " " << order[i + K] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
