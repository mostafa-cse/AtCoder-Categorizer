# Problem Analysis: AtCoder-typical90_u — Come Back in One Piece

**Problem ID**: `AtCoder-typical90_u`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 021)  
**Rating / Difficulty**: 1750 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_u  
**VJudge Tag**: `[problem:AtCoder-typical90_u]`  
**Category File**: [`../categories/graph_theory/strongly_connected_components.md`](../categories/graph_theory/strongly_connected_components.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Directed Graphs`  
- **Topic (Skill)**: `Strongly Connected Components (SCC) / Tarjan & Kosaraju`  

---

## 1. Problem Statement & Key Idea
Given a directed graph with N vertices and M edges, count the number of pairs of vertices (u, v) with u < v such that u can reach v and v can reach u.

**Core Idea**: Two vertices can reach each other if and only if they belong to the same Strongly Connected Component (SCC).

## 2. Core Observation & Invariant
Decompose the graph into SCCs. Each SCC of size S contributes C(S, 2) = S*(S - 1)/2 mutually reachable pairs.

## 3. Step-by-Step Algorithm
1. Build adjacency list G and reversed graph G_rev.
2. DFS 1 on G: record vertices in order of post-order finish time.
3. DFS 2 on G_rev in reverse finish order: extract connected components.
4. For each component of size S: add S * (S - 1) / 2 to total count.

## 4. Complexity Analysis
Time: O(N + M), Space: O(N + M).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void dfs1(int u, const vector<vector<int>>& adj, vector<bool>& vis, vector<int>& order) {
    vis[u] = true;
    for (int v : adj[u]) {
        if (!vis[v]) dfs1(v, adj, vis, order);
    }
    order.push_back(u);
}

void dfs2(int u, const vector<vector<int>>& rev_adj, vector<bool>& vis, long long& comp_size) {
    vis[u] = true;
    comp_size++;
    for (int v : rev_adj[u]) {
        if (!vis[v]) dfs2(v, rev_adj, vis, comp_size);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1), rev_adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        rev_adj[v].push_back(u);
    }

    vector<bool> vis(n + 1, false);
    vector<int> order;
    for (int i = 1; i <= n; ++i) {
        if (!vis[i]) dfs1(i, adj, vis, order);
    }

    fill(vis.begin(), vis.end(), false);
    reverse(order.begin(), order.end());

    long long total_pairs = 0;
    for (int u : order) {
        if (!vis[u]) {
            long long comp_size = 0;
            dfs2(u, rev_adj, vis, comp_size);
            total_pairs += comp_size * (comp_size - 1) / 2;
        }
    }

    cout << total_pairs << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Kosaraju's two-pass Strongly Connected Components algorithm.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Strongly Connected Components, mutual reachability equivalence classes, and Kosaraju/Tarjan linear-time decomposition.
- **Reusable Pattern**: `Kosaraju / Tarjan Strongly Connected Components.`

---
Back to [Strongly Connected Components (SCC) / Tarjan & Kosaraju](../categories/graph_theory/strongly_connected_components.md) | [Categories Directory](../categories/README.md)