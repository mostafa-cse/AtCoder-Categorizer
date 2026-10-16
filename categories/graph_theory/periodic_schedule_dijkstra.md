# Periodic Departure Schedule Dijkstra

**Domain**: `Graph Theory`  
**Subtopic**: `Dijkstra`  

This workbook contains curated, high-quality competitive programming problems teaching **Periodic Departure Schedule Dijkstra**.

---

## Curated Problems

### [problem:AtCoder-abc192_e] — Train
- **Contest**: `abc192`
- **Rating / Difficulty**: 1135
- **Specific Skill**: Periodic Departure Schedule Dijkstra
- **Individual Analysis**: [`../../analysis/AtCoder-abc192_e.md`](../../analysis/AtCoder-abc192_e.md)
- **Problem Statement Summary**: A rail network has N cities and M train lines. Train line i connects A_i and B_i taking T_i time, but only departs at times that are multiples of K_i (0, K_i, 2*K_i...). Find the earliest time to travel from X to Y.
- **Core Insight**: If you arrive at city u at time cur_time, the earliest departure for line i with interval K is dep_time = ((cur_time + K - 1) / K) * K. The arrival at city v is dep_time + T. Because departure time is non-decreasing with arrival time, the greedy property of Dijkstra holds.
- **Complexity**: Time: `O(M log N)` | Space: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    long long t, k;
};

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, x, y;
    if (!(cin >> n >> m >> x >> y)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long t, k;
        cin >> u >> v >> t >> k;
        adj[u].push_back({v, t, k});
        adj[v].push_back({u, t, k});
    }

    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    dist[x] = 0;
    pq.push({0, x});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;
        if (u == y) break;

        for (const auto& e : adj[u]) {
            long long dep = ((d + e.k - 1) / e.k) * e.k;
            long long arr = dep + e.t;
            if (arr < dist[e.to]) {
                dist[e.to] = arr;
                pq.push({arr, e.to});
            }
        }
    }

    cout << (dist[y] == INF ? -1 : dist[y]) << "\n";
    return 0;
}
```
