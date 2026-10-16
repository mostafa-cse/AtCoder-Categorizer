# Problem Analysis: AtCoder-typical90_ai — Preserve Connectivity

**Problem ID**: `AtCoder-typical90_ai`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 035)  
**Rating / Difficulty**: 2450 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ai  
**VJudge Tag**: `[problem:AtCoder-typical90_ai]`  
**Category File**: [`../categories/graph_theory/euler_tour_lca.md`](../categories/graph_theory/euler_tour_lca.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees & LCA`  
- **Topic (Skill)**: `Euler Tour DFS Order + LCA for Minimal Subtree on Subset of Vertices`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices, answer Q queries: each query gives K vertices V_1, ..., V_K. Find the minimum number of edges in a connected subgraph containing all K vertices.

**Core Idea**: The minimal connecting subtree (Steiner tree on vertices) has edge count equal to half the sum of distances between adjacent vertices when sorted by Euler Tour order.

## 2. Core Observation & Invariant
Sort the K query vertices by their DFS entry time in an Euler Tour: u_1, u_2, ..., u_K. The minimal subtree edge count is (1/2) * sum_{i=1}^K dist(u_i, u_{i+1}) with u_{K+1} = u_1.

## 3. Step-by-Step Algorithm
1. Run DFS to compute depth, binary lifting LCA table, and entry timestamp tin[u].
2. For each query: sort the K vertices by tin[u].
3. Sum dist(u_i, u_{i+1}) = depth[u_i] + depth[u_{i+1}] - 2 * depth[LCA(u_i, u_{i+1})].
4. Output sum / 2.

## 4. Complexity Analysis
Time: O((N + Q*K) log N), Space: O(N log N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 100005;
const int LOGN = 18;

vector<int> adj[MAXN];
int up[LOGN][MAXN];
int depth[MAXN];
int tin[MAXN];
int timer_dfs = 0;

void dfs(int u, int p, int d) {
    tin[u] = ++timer_dfs;
    depth[u] = d;
    up[0][u] = p;
    for (int i = 1; i < LOGN; ++i) {
        up[i][u] = up[i - 1][up[i - 1][u]];
    }
    for (int v : adj[u]) {
        if (v != p) dfs(v, u, d + 1);
    }
}

int get_lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    for (int i = LOGN - 1; i >= 0; --i) {
        if (depth[u] - (1 << i) >= depth[v]) {
            u = up[i][u];
        }
    }
    if (u == v) return u;
    for (int i = LOGN - 1; i >= 0; --i) {
        if (up[i][u] != up[i][v]) {
            u = up[i][u];
            v = up[i][v];
        }
    }
    return up[0][u];
}

int dist(int u, int v) {
    return depth[u] + depth[v] - 2 * depth[get_lca(u, v)];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1, 1, 0);

    int q;
    cin >> q;
    while (q--) {
        int k;
        cin >> k;
        vector<int> v(k);
        for (int i = 0; i < k; ++i) cin >> v[i];

        sort(v.begin(), v.end(), [](int a, int b) {
            return tin[a] < tin[b];
        });

        long long total_dist = 0;
        for (int i = 0; i < k; ++i) {
            int u1 = v[i];
            int u2 = v[(i + 1) % k];
            total_dist += dist(u1, u2);
        }
        cout << total_dist / 2 << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Euler Tour order cyclic distance sum for minimal connecting subtree.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Euler Tour vertex ordering, minimal spanning forest on trees, and LCA distance queries.
- **Reusable Pattern**: `Euler Tour Order + LCA Cyclic Distance.`

---
Back to [Euler Tour DFS Order + LCA for Minimal Subtree on Subset of Vertices](../categories/graph_theory/euler_tour_lca.md) | [Categories Directory](../categories/README.md)