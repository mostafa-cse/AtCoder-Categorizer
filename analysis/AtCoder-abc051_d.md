# Problem Analysis: AtCoder-abc051_d — Candidates of No Shortest Paths

**Problem ID**: `AtCoder-abc051_d`  
**Contest**: `abc051`  
**Rating / Difficulty**: 1566  
**URL**: https://atcoder.jp/contests/abc051/tasks/abc051_d  
**VJudge Tag**: `[problem:AtCoder-abc051_d]`  
**Category File**: [`../categories/graph_theory/floyd_warshall_shortest_path_edge_criterion.md`](../categories/graph_theory/floyd_warshall_shortest_path_edge_criterion.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `All-Pairs Shortest Paths`  
- **Topic (Skill)**: `Floyd-Warshall Edge Shortest Path Criterion`  

---

## 1. Problem Statement & Key Idea
An undirected weighted graph with N vertices and M edges. Count how many edges are NOT used in any shortest path between any pair of vertices.

**Key Insight**: Precompute all-pairs shortest paths using Floyd-Warshall. An edge e = (u, v, w) is used in a shortest path between some pair (s, t) if and only if dist[s][u] + w + dist[v][t] == dist[s][t] (or with u and v swapped).

## 2. Core Observation & Invariant
Setting s = u and t = v, edge (u, v) is used in some shortest path iff dist[u][v] == w! If dist[u][v] < w, the edge is strictly longer than an alternative path and will NEVER be part of any shortest path.

## 3. Step-by-Step Algorithm
1. Compute all-pairs shortest paths dist[u][v] using Floyd-Warshall in O(N^3).
2. unused_edges = 0.
3. For each edge (u, v, w):
4.   If dist[u][v] < w, unused_edges++.
5. Print unused_edges.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 + M)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct Edge {
    int u, v, w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        dist[edges[i].u][edges[i].v] = min(dist[edges[i].u][edges[i].v], edges[i].w);
        dist[edges[i].v][edges[i].u] = min(dist[edges[i].v][edges[i].u], edges[i].w);
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    int unused = 0;
    for (const auto& e : edges) {
        if (dist[e.u][e.v] < e.w) {
            unused++;
        }
    }

    cout << unused << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Identifying redundant edges via direct comparison against all-pairs shortest distance matrix.
- **Reusable Pattern**: `Unused Shortest Path Edge: count edges where dist[u][v] < edge_weight.`
