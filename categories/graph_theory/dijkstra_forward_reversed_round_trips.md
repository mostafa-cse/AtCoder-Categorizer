# Forward & Reversed Graph Dijkstra for Time-Constrained Round Trips

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Forward & Reversed Graph Dijkstra for Time-Constrained Round Trips**.

---

## Curated Problems

### `[problem:AtCoder-abc035_d]` — Treasure Hunt
- **Rating / Difficulty**: 1591
- **Contest**: `abc035`
- **Analysis**: [`analysis/AtCoder-abc035_d.md`](../../analysis/AtCoder-abc035_d.md)
- **Key Idea**: Run Dijkstra from vertex 1 on the original graph to compute dist_to[v] (shortest travel time 1 -> v). Run Dijkstra from vertex 1 on the REVERSED graph to compute dist_from[v] (shortest travel time v -> 1).
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
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
