# Dijkstra with Convex Time-Dependent Delay / Derivative Optimization

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Dijkstra with Convex Time-Dependent Delay / Derivative Optimization**.

---

## Curated Problems

### `[problem:AtCoder-abc204_e]` — Rush Hour 2
- **Rating / Difficulty**: 1710
- **Contest**: `abc204`
- **Analysis**: [`analysis/AtCoder-abc204_e.md`](../../analysis/AtCoder-abc204_e.md)
- **Key Idea**: Standard Dijkstra where arrival time via edge (u, v) is t' + C_i + floor(D_i / (t' + 1)) for some wait time t' >= dist[u]. The function f(t') = t' + D_i / (t' + 1) is convex with continuous minimum near t' + 1 approx sqrt(D_i).
- **Time Complexity**: `O(M log N)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long c, d;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c, d;
        cin >> u >> v >> c >> d;
        adj[u].push_back({v, c, d});
        adj[v].push_back({u, c, d});
    }

    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    dist[1] = 0;
    pq.push({0, 1});

    while (!pq.empty()) {
        auto [d_cur, u] = pq.top();
        pq.pop();

        if (d_cur > dist[u]) continue;

        for (auto& edge : adj[u]) {
            long long best_arrival = INF;
            long long t_opt = (long long)round(sqrt(edge.d)) - 1;
            
            vector<long long> candidates = {dist[u], t_opt - 1, t_opt, t_opt + 1};
            for (long long t : candidates) {
                if (t >= dist[u]) {
                    long long arr = t + edge.c + edge.d / (t + 1);
                    best_arrival = min(best_arrival, arr);
                }
            }

            if (best_arrival < dist[edge.to]) {
                dist[edge.to] = best_arrival;
                pq.push({best_arrival, edge.to});
            }
        }
    }

    cout << (dist[n] == INF ? -1 : dist[n]) << "\n";
    return 0;
}
```
