# Problem Analysis: AtCoder-arc111_d — Orientation

**Problem ID**: `AtCoder-arc111_d`  
**Contest**: `arc111`  
**Rating / Difficulty**: 2064  
**URL**: https://atcoder.jp/contests/arc111/tasks/arc111_d  
**VJudge Tag**: `[problem:AtCoder-arc111_d]`  
**Category File**: [`../categories/graph_theory/dfs_tree_graph_orientation_scc.md`](../categories/graph_theory/dfs_tree_graph_orientation_scc.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Directed Graphs`  
- **Topic (Skill)**: `Strong Connectivity Graph Orientation and DFS Tree Back-Edge Directing`  

---

## 1. Problem Statement & Key Idea
Given an undirected graph with N vertices and M edges, and reachability requirements c_1, ..., c_N. Direct all edges such that the number of reachable vertices from vertex i is exactly c_i. A valid solution is guaranteed to exist.

**Key Idea**: If c_u > c_v, v cannot reach u (otherwise c_v >= c_u), so edge (u, v) must be directed u -> v. If c_u < c_v, it must be directed v -> u. If c_u == c_v, u and v must be mutually reachable and belong to the same Strongly Connected Component (SCC). We can orient the subgraph of edges with c_u == c_v into a strongly connected directed graph using Robbins' Theorem / DFS tree orientation: direct tree edges downward (parent -> child) and back-edges upward (descendant -> ancestor).

## 2. Core Observation & Invariant
Edges between different reachability values are strictly determined by reachability gradient; edges between equal values are made strongly connected via DFS tree orientation.

## 3. Step-by-Step Algorithm
1. For each edge (u, v):
2.   If c[u] > c[v]: orient u -> v.
3.   If c[u] < c[v]: orient v -> u.
4.   If c[u] == c[v]: add to equality adjacency list.
5. Run DFS on the equality subgraph to construct a DFS forest.
6. Orient tree edges from parent to child.
7. Orient non-tree back-edges from deeper node to shallower ancestor.
8. Output the resulting orientation for all M edges.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. Core Algorithmic Skill & Learning Takeaway
Directing bridgeless connected graphs into strongly connected components via DFS tree edge/back-edge orientation.

**Reusable Pattern**: Graph orientation with reachability constraints: cross-component edges follow topological order of reachability; intra-component edges are oriented via DFS tree.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

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

    vector<int> c(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> c[i];
    }

    vector<string> ans(m);
    vector<vector<pair<int, int>>> adj_eq(n + 1);

    for (int i = 0; i < m; ++i) {
        int u = edges[i].u;
        int v = edges[i].v;
        if (c[u] > c[v]) {
            ans[i] = "->";
        } else if (c[u] < c[v]) {
            ans[i] = "<-";
        } else {
            adj_eq[u].push_back({v, i});
            adj_eq[v].push_back({u, i});
        }
    }

    vector<bool> visited(n + 1, false);
    vector<int> dep(n + 1, 0);

    auto dfs = [&](auto& self, int u, int p_edge, int d) -> void {
        visited[u] = true;
        dep[u] = d;
        for (auto& edge_info : adj_eq[u]) {
            int v = edge_info.first;
            int idx = edge_info.second;
            if (idx == p_edge) continue;
            if (visited[v]) {
                if (dep[v] < dep[u]) {
                    if (edges[idx].u == u) ans[idx] = "->";
                    else ans[idx] = "<-";
                }
            } else {
                if (edges[idx].u == u) ans[idx] = "->";
                else ans[idx] = "<-";
                self(self, v, idx, d + 1);
            }
        }
    };

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            dfs(dfs, i, -1, 1);
        }
    }

    for (int i = 0; i < m; ++i) {
        cout << ans[i] << "\n";
    }
    return 0;
}
```
