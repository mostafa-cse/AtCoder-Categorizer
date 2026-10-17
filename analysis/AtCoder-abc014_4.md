# Problem Analysis: AtCoder-abc014_4 — 閉路

**Problem ID**: `AtCoder-abc014_4`  
**Contest**: `abc014`  
**Rating / Difficulty**: 1856  
**URL**: https://atcoder.jp/contests/abc014/tasks/abc014_4  
**VJudge Tag**: `[problem:AtCoder-abc014_4]`  
**Category File**: [`../categories/graph_theory/cycle_length_edge_addition_lca.md`](../categories/graph_theory/cycle_length_edge_addition_lca.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Tree LCA`  
- **Topic (Skill)**: `Cycle Length upon Edge Addition via Tree LCA (dist(u, v) + 1)`  

---

## 1. Problem Statement & Key Idea
Given a tree of N vertices. For Q queries (u, v), adding an edge between u and v creates a unique simple cycle. Find the length of this cycle for each query.

**Key Insight**: Adding edge (u, v) creates a cycle consisting of the tree path between u and v plus the new edge. Cycle length = dist(u, v) + 1 = depth[u] + depth[v] - 2 * depth[LCA(u, v)] + 1.

## 2. Core Observation & Invariant
Binary lifting precomputes ancestors in O(N log N) and answers each LCA query in O(log N).

## 3. Step-by-Step Algorithm
1. Root tree at 1. DFS computes depth and binary lifting table up[k][u].
2. For each query (u, v):
3.   lca = get_lca(u, v).
4.   dist = depth[u] + depth[v] - 2 * depth[lca].
5.   print dist + 1.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N log N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int n, q;
vector<vector<int>> adj;
vector<int> depth;
int up[20][100005];

void dfs(int u, int p, int d) {
    depth[u] = d;
    up[0][u] = p;
    for (int k = 1; k < 20; ++k) {
        up[k][u] = up[k - 1][up[k - 1][u]];
    }
    for (int v : adj[u]) {
        if (v != p) dfs(v, u, d + 1);
    }
}

int get_lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    for (int k = 19; k >= 0; --k) {
        if (depth[u] - (1 << k) >= depth[v]) {
            u = up[k][u];
        }
    }
    if (u == v) return u;
    for (int k = 19; k >= 0; --k) {
        if (up[k][u] != up[k][v]) {
            u = up[k][u];
            v = up[k][v];
        }
    }
    return up[0][u];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    adj.assign(n + 1, vector<int>());
    depth.assign(n + 1, 0);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 1, 0);

    cin >> q;
    while (q--) {
        int u, v;
        cin >> u >> v;
        int lca = get_lca(u, v);
        int cycle_len = depth[u] + depth[v] - 2 * depth[lca] + 1;
        cout << cycle_len << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Measuring tree distance and cycle lengths upon edge additions via binary lifting LCA.
- **Reusable Pattern**: `Tree Edge Addition Cycle: Length = dist(u, v) + 1 = depth[u] + depth[v] - 2*depth[LCA] + 1.`
