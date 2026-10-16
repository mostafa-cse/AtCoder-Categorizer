# Problem Analysis: AtCoder-arc108_c — Keep Graph Connected

**Problem ID**: `AtCoder-arc108_c`  
**Contest**: `arc108`  
**Rating / Difficulty**: 1460  
**URL**: https://atcoder.jp/contests/arc108/tasks/arc108_c  
**VJudge Tag**: `[problem:AtCoder-arc108_c]`  
**Category File**: [`../categories/graph_theory/spanning_tree_node_coloring.md`](../categories/graph_theory/spanning_tree_node_coloring.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Spanning Tree Constructive Node Coloring`  

---

## 1. Problem Statement & Key Idea
Given a connected graph with N vertices and M edges, where edge i has label c_i (1 <= c_i <= N). Assign an integer label from 1 to N to each vertex such that for every vertex v, there is at least one incident edge (u, v) whose edge label equals the vertex label of v.

**Key Insight**: Extract any spanning tree. Root it arbitrarily and assign labels top-down via DFS/BFS: each child v is assigned the label of its tree edge to parent u; if that matches parent u's label, assign an alternative unused label.

## 2. Core Observation & Invariant
On a spanning tree, every vertex except the root has a unique parent edge. If child v takes label(v) = edge_label(u, v), that edge satisfies vertex v! The only issue is if label(u) == edge_label(u, v). In that case, choose any label for v different from edge_label(u, v), which satisfies parent u via edge (u, v).

## 3. Step-by-Step Algorithm
1. Build adjacency list for a spanning tree using BFS/DFS.
2. Initialize ans array with 0. Set ans[root = 1] = 1.
3. Traverse tree from root via BFS:
4.   For each child v with parent u and edge label c:
5.     If ans[u] != c, set ans[v] = c.
6.     Else set ans[v] = (c % N) + 1.
7. Print the assigned labels for all vertices.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    int label;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    vector<int> ans(n + 1, 0);
    vector<bool> visited(n + 1, false);
    queue<int> q;

    ans[1] = 1;
    visited[1] = true;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (const auto& edge : adj[u]) {
            int v = edge.to;
            int c = edge.label;
            if (!visited[v]) {
                visited[v] = true;
                if (ans[u] != c) {
                    ans[v] = c;
                } else {
                    ans[v] = (c % n) + 1;
                }
                q.push(v);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Constructive bipartite/tree assignment by decoupling parent-child constraints along a spanning forest.
- **Reusable Pattern**: `Spanning Tree Assignment: propagate constraints top-down, handling collision with cyclic fallback ((c % N) + 1).`
