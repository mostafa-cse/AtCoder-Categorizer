# Multi-Source Dijkstra Shortest Cycle / Self-Loop Detection

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Multi-Source Dijkstra Shortest Cycle / Self-Loop Detection**.

---

## Curated Problems

### [problem:AtCoder-abc191_e] — Come Back Quickly
- **Contest**: `abc191`
- **Rating / Difficulty**: 1323
- **Specific Skill**: Multi-Source Dijkstra Shortest Cycle / Self-Loop Detection
- **Individual Analysis**: [`../../analysis/AtCoder-abc191_e.md`](../../analysis/AtCoder-abc191_e.md)
- **Problem Statement Summary**: A directed weighted graph with N vertices and M edges. For each vertex i in 1..N, find the minimum length of a directed cycle that starts and ends at vertex i (or -1 if none exists).
- **Core Insight**: Because N <= 2000, we can run Dijkstra's algorithm once from each vertex i! To cleanly find the shortest cycle from i to i, initialize dist array to INF. Push all immediate outgoing edges (i -> v, c) into the priority queue with initial distance c (instead of dist[i] = 0). When vertex i is popped from the priority queue, the extracted distance is the exact shortest cycle!
- **Complexity**: Time: `O(N * (M log N))` | Space: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    long long w;
};

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
    }

    for (int i = 1; i <= n; ++i) {
        vector<long long> dist(n + 1, INF);
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

        for (const auto& e : adj[i]) {
            if (e.w < dist[e.to]) {
                dist[e.to] = e.w;
                pq.push({e.w, e.to});
            }
        }

        long long cycle_len = -1;
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();

            if (u == i) {
                cycle_len = d;
                break;
            }
            if (d > dist[u]) continue;

            for (const auto& e : adj[u]) {
                if (d + e.w < dist[e.to]) {
                    dist[e.to] = d + e.w;
                    pq.push({d + e.w, e.to});
                }
            }
        }

        cout << cycle_len << "\n";
    }

    return 0;
}
```
