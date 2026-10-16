# Problem Analysis: AtCoder-abc120_d — Decayed Bridges

**Problem ID**: `AtCoder-abc120_d`  
**Contest**: `abc120`  
**Rating / Difficulty**: 1355  
**URL**: https://atcoder.jp/contests/abc120/tasks/abc120_d  
**VJudge Tag**: `[problem:AtCoder-abc120_d]`  
**Category File**: [`../categories/data_structures/reverse_offline_edge_addition_dsu.md`](../categories/data_structures/reverse_offline_edge_addition_dsu.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Disjoint Set Union`  
- **Topic (Skill)**: `Reverse Offline Edge Addition with DSU Connected Component Pairs`  

---

## 1. Problem Statement & Key Idea
N islands initially connected by M bridges. In each step i from 1 to M, bridge i collapses. 'Inconvenience' is the number of pairs (u, v) with u < v that cannot reach each other. Find inconvenience after each bridge collapses.

**Key Idea**: Processing bridge removals directly is hard. Inverting the timeline: start with 0 bridges, and add bridges in REVERSE order from bridge M down to 1!

## 2. Core Observation & Invariant
Initially (with no bridges), all C(N, 2) pairs are disconnected. When adding an edge between u and v: if u and v are in different DSU components of size sz[u] and sz[v], adding this bridge connects sz[u] * sz[v] new pairs of islands, decreasing inconvenience by sz[u] * sz[v]!

## 3. Step-by-Step Algorithm
1. Initialize DSU on N vertices.
2. Initial inconvenience = N * (N - 1) / 2.
3. Process bridges in reverse order from M - 1 down to 0:
4.   Record ans[i] = current inconvenience.
5.   If find(u) != find(v): inconvenience -= (long long)sz[find(u)] * sz[find(v)], unite(u, v).
6. Print ans[0..M-1].

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) * alpha(N))`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> sz;
    DSU(int n) : parent(n + 1), sz(n + 1, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j, long long& delta) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            delta = (long long)sz[root_i] * sz[root_j];
            parent[root_i] = root_j;
            sz[root_j] += sz[root_i];
            return true;
        }
        delta = 0;
        return false;
    }
};

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v;
    }

    DSU dsu(n);
    long long cur_inconvenience = (long long)n * (n - 1) / 2;
    vector<long long> ans(m);

    for (int i = m - 1; i >= 0; --i) {
        ans[i] = cur_inconvenience;
        long long delta = 0;
        dsu.unite(edges[i].u, edges[i].v, delta);
        cur_inconvenience -= delta;
    }

    for (int i = 0; i < m; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Reverse time offline processing using DSU edge addition.
- **Reusable Pattern**: `Bridge collapse / edge deletion: process backward with DSU, subtract sz[u] * sz[v] disconnected pairs.`
