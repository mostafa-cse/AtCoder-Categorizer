# Problem Analysis: AtCoder-abc035_d — Treasure Hunt

**Problem ID**: `AtCoder-abc035_d`  
**Contest**: `abc035`  
**Rating / Difficulty**: 1591  
**URL**: https://atcoder.jp/contests/abc035/tasks/abc035_d  
**VJudge Tag**: `[problem:AtCoder-abc035_d]`  
**Category File**: [`../categories/graph_theory/dijkstra_forward_reversed_round_trips.md`](../categories/graph_theory/dijkstra_forward_reversed_round_trips.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Forward & Reversed Graph Dijkstra for Time-Constrained Round Trips`  

---

## 1. Problem Statement & Key Idea
Directed graph with N vertices and M edges. Vertex i yields treasure A_i per minute. You have T minutes total. Start at vertex 1, travel to some vertex v, stay there collecting treasure, and return to vertex 1. Maximize total treasure collected.

**Key Insight**: Run Dijkstra from vertex 1 on the original graph to compute dist_to[v] (shortest travel time 1 -> v). Run Dijkstra from vertex 1 on the REVERSED graph to compute dist_from[v] (shortest travel time v -> 1).

## 2. Core Observation & Invariant
The total travel time for a round trip 1 -> v -> 1 is dist_to[v] + dist_from[v]. If this round trip takes time <= T, Takahashi can spend remaining time T - (dist_to[v] + dist_from[v]) at vertex v collecting treasure. Maximize over all v.

## 3. Step-by-Step Algorithm
1. Build forward adjacency list and reversed adjacency list.
2. Run Dijkstra from 1 on forward graph: dist_to[v].
3. Run Dijkstra from 1 on reversed graph: dist_from[v].
4. max_treasure = 0.
5. For v from 1 to N:
6.   If dist_to[v] + dist_from[v] <= T:
7.     rem_time = T - (dist_to[v] + dist_from[v]);
8.     max_treasure = max(max_treasure, rem_time * A[v]);
9. Print max_treasure.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

struct Edge {
    int to;
    long long cost;
};

void dijkstra(int start, int n, const vector<vector<Edge>>& adj, vector<long long>& dist) {
    dist.assign(n + 1, INF);
    dist[start] = 0;
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u]) continue;

        for (const auto& e : adj[u]) {
            if (dist[u] + e.cost < dist[e.to]) {
                dist[e.to] = dist[u] + e.cost;
                pq.push({dist[e.to], e.to});
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long T;
    if (!(cin >> n >> m >> T)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<vector<Edge>> adj(n + 1), rev_adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        rev_adj[v].push_back({u, c});
    }

    vector<long long> dist_to, dist_from;
    dijkstra(1, n, adj, dist_to);
    dijkstra(1, n, rev_adj, dist_from);

    long long max_treasure = 0;
    for (int v = 1; v <= n; ++v) {
        if (dist_to[v] < INF && dist_from[v] < INF) {
            long long round_trip = dist_to[v] + dist_from[v];
            if (round_trip <= T) {
                max_treasure = max(max_treasure, (T - round_trip) * a[v]);
            }
        }
    }

    cout << max_treasure << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Dual-graph Dijkstra (forward and reversed) for directed round-trip optimization.
- **Reusable Pattern**: `Directed Round Trip: Dijkstra(start) + Dijkstra_Reversed(start), round_trip = dist1 + dist2.`
