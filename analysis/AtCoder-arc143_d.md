# Problem Analysis: AtCoder-arc143_d — Bridges

**Problem ID**: `AtCoder-arc143_d`  
**Contest**: `arc143`  
**Rating / Difficulty**: 2229  
**URL**: https://atcoder.jp/contests/arc143/tasks/arc143_d  
**VJudge Tag**: `[problem:AtCoder-arc143_d]`  
**Category File**: [`../categories/graph_theory/dfs_tree_graph_orientation_bridge_minimization.md`](../categories/graph_theory/dfs_tree_graph_orientation_bridge_minimization.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `DFS Tree`  

---

## 1. Problem Statement & Key Idea
Orient M edges between top and bottom vertices in a 2N-vertex graph with fixed pillar edges (j, j+N) to minimize the number of bridges.

## 2. Core Observation & Invariant
Contracting pillar edges (j, j+N) yields a multigraph of N vertices and M edges. Directed cycles in the contracted graph lift to undirected cycles in the 2N graph using vertical edges. By Robbins' Theorem and DFS tree properties, directing tree edges forward (parent to child) and back edges backward (descendant to ancestor) strongly connects every 2-edge-connected component, eliminating all non-trivial bridges.

## 3. Step-by-Step Algorithm
1. 1. Build adjacency list for the contracted graph of N vertices and M edges, tracking original edge endpoints.
2. 2. For each connected component, execute DFS starting from an unvisited vertex.
3. 3. When traversing an unused edge:
4.    - Orient the edge from current vertex u to neighbor v (set S[e] = '0' if u == A_e else '1').
5.    - If v is unvisited, recurse (tree edge); if v is visited, record direction and do not recurse (back edge).
6. 4. Output the resulting binary string of orientations.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Edge {
    int to;
    int id;
    int orig_u; // A_i
    int orig_v; // B_i
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> A(m), B(m);
    for (int i = 0; i < m; ++i) cin >> A[i];
    for (int i = 0; i < m; ++i) cin >> B[i];

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        adj[A[i]].push_back({B[i], i, A[i], B[i]});
        adj[B[i]].push_back({A[i], i, A[i], B[i]});
    }

    string ans(m, '0');
    vector<bool> vis_edge(m, false);
    vector<int> depth(n + 1, -1);

    auto dfs = [&](auto& self, int u, int d) -> void {
        depth[u] = d;
        for (const auto& e : adj[u]) {
            if (vis_edge[e.id]) continue;
            vis_edge[e.id] = true;

            // Direct edge from u to e.to
            if (u == e.orig_u) {
                ans[e.id] = '0';
            } else {
                ans[e.id] = '1';
            }

            if (depth[e.to] == -1) {
                self(self, e.to, d + 1);
            }
        }
    };

    for (int i = 1; i <= n; ++i) {
        if (depth[i] == -1) {
            dfs(dfs, i, 0);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
