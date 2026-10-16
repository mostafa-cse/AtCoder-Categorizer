# Problem Analysis: AtCoder-typical90_m — Passing

**Problem ID**: `AtCoder-typical90_m`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 013)  
**Rating / Difficulty**: 1350 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_m  
**VJudge Tag**: `[problem:AtCoder-typical90_m]`  
**Category File**: [`../categories/graph_theory/shortest_paths_dijkstra.md`](../categories/graph_theory/shortest_paths_dijkstra.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dual-Source Dijkstra / Intermediate Node Shortest Path`  

---

## 1. Problem Statement & Key Idea
Given a weighted undirected graph with N vertices and M edges, for each vertex k from 1 to N, find the length of the shortest path from vertex 1 to vertex N that passes through vertex k.

**Core Idea**: The shortest path from 1 to N passing through k is dist(1, k) + dist(k, N).

## 2. Core Observation & Invariant
Run Dijkstra from node 1 once to compute all dist(1, k), and Dijkstra from node N once to compute all dist(N, k). For each k, sum dist1[k] + distN[k].

## 3. Step-by-Step Algorithm
1. Run Dijkstra from vertex 1 -> dist1.
2. Run Dijkstra from vertex N -> distN.
3. For each k in 1..N: output dist1[k] + distN[k].

## 4. Complexity Analysis
Time: O((N + M) log N), Space: O(N + M).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const long long INF = 1e18;

vector<long long> dijkstra(int start, const vector<vector<pair<int, long long>>>& adj, int n) {
    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;

        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<pair<int, long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    auto dist1 = dijkstra(1, adj, n);
    auto distN = dijkstra(n, adj, n);

    for (int k = 1; k <= n; ++k) {
        cout << dist1[k] + distN[k] << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Dual-source Dijkstra decomposition.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Decomposing constrained shortest path queries into independent source/sink distance fields.
- **Reusable Pattern**: `Dual Dijkstra (Start to K + K to Goal).`

---
Back to [Dual-Source Dijkstra / Intermediate Node Shortest Path](../categories/graph_theory/shortest_paths_dijkstra.md) | [Categories Directory](../categories/README.md)