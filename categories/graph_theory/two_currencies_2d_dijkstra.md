# 2D State Dijkstra on Resource/Currency Bounds

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **2D State Dijkstra on Resource/Currency Bounds**.

---

## Curated Problems

### `[problem:AtCoder-abc164_e]` — Two Currencies
- **Rating / Difficulty**: 1877
- **Contest**: `abc164`
- **Analysis**: [`analysis/AtCoder-abc164_e.md`](../../analysis/AtCoder-abc164_e.md)
- **Key Idea**: The maximum silver coins required at any city is bounded by max(A_i) * (N - 1) <= 50 * 50 = 2500. Cap the silver coin state at MAX_S = 2500. Run Dijkstra on the state space (city u, silver coins s).
- **Time Complexity**: `O(N * MAX_S * log(N * MAX_S))`
- **Space Complexity**: `O(N * MAX_S)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;
const int MAX_S = 2500;

struct Edge {
    int to;
    int a;
    long long t;
};

struct State {
    long long d;
    int u, s;
    bool operator>(const State& other) const {
        return d > other.d;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long initial_s;
    if (!(cin >> n >> m >> initial_s)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, a;
        long long t;
        cin >> u >> v >> a >> t;
        adj[u].push_back({v, a, t});
        adj[v].push_back({u, a, t});
    }

    vector<long long> C(n + 1), D(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> C[i] >> D[i];
    }

    int start_s = min((long long)MAX_S, initial_s);
    vector<vector<long long>> dist(n + 1, vector<long long>(MAX_S + 1, INF));
    priority_queue<State, vector<State>, greater<State>> pq;

    dist[1][start_s] = 0;
    pq.push({0, 1, start_s});

    while (!pq.empty()) {
        auto [d, u, s] = pq.top();
        pq.pop();

        if (d > dist[u][s]) continue;

        // Option 1: Currency exchange
        int next_s = min((long long)MAX_S, s + C[u]);
        if (d + D[u] < dist[u][next_s]) {
            dist[u][next_s] = d + D[u];
            pq.push({dist[u][next_s], u, next_s});
        }

        // Option 2: Ride train
        for (auto& e : adj[u]) {
            if (s >= e.a) {
                if (d + e.t < dist[e.to][s - e.a]) {
                    dist[e.to][s - e.a] = d + e.t;
                    pq.push({dist[e.to][s - e.a], e.to, s - e.a});
                }
            }
        }
    }

    for (int i = 2; i <= n; ++i) {
        long long ans = INF;
        for (int s = 0; s <= MAX_S; ++s) {
            ans = min(ans, dist[i][s]);
        }
        cout << ans << "\n";
    }

    return 0;
}
```
