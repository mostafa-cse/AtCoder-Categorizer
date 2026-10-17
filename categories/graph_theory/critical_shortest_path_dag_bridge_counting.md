# Critical Shortest-Path Edges via Shortest Path DAG and Double-Mod Path Counting

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Critical Shortest-Path Edges via Shortest Path DAG and Double-Mod Path Counting**.

---

## Curated Problems

### `[problem:AtCoder-abc375_g]` — Road Blocked 2
- **Rating / Difficulty**: 2014
- **Contest**: `abc375`
- **Analysis**: [`analysis/AtCoder-abc375_g.md`](../../analysis/AtCoder-abc375_g.md)
- **Key Idea**: Let D = dist(1, N). An edge (u, v, w) lies on at least one shortest path from 1 to N iff dist_1(u) + w + dist_N(v) == D (or the reverse). These edges form the Shortest Path DAG. An edge is critical (its removal increases D) iff it lies on EVERY shortest path from 1 to N! We count the number of shortest paths from 1 to all vertices (cnt_1) and from all vertices to N (cnt_N) modulo two large distinct primes. Edge (u, v) lies on all shortest paths iff cnt_1(u) * cnt_N(v) = cnt_1(N) under both moduli.
- **Time Complexity**: `O((N + M) log N)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const long long INF = 1e18;
const long long MOD1 = 1e9 + 7;
const long long MOD2 = 998244353;

struct Edge {
    int id;
    int to;
    long long w;
};

void dijkstra(int start, int n, const vector<vector<Edge>>& adj, vector<long long>& dist,
              vector<long long>& cnt1, vector<long long>& cnt2) {
    dist.assign(n + 1, INF);
    cnt1.assign(n + 1, 0);
    cnt2.assign(n + 1, 0);

    dist[start] = 0;
    cnt1[start] = 1;
    cnt2[start] = 1;

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;

        for (const auto& e : adj[u]) {
            if (dist[e.to] > dist[u] + e.w) {
                dist[e.to] = dist[u] + e.w;
                cnt1[e.to] = cnt1[u];
                cnt2[e.to] = cnt2[u];
                pq.push({dist[e.to], e.to});
            } else if (dist[e.to] == dist[u] + e.w) {
                cnt1[e.to] = (cnt1[e.to] + cnt1[u]) % MOD1;
                cnt2[e.to] = (cnt2[e.to] + cnt2[u]) % MOD2;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    struct InputEdge {
        int u, v;
        long long w;
    };
    vector<InputEdge> edges(m);
    vector<vector<Edge>> adj(n + 1);

    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        adj[edges[i].u].push_back({i, edges[i].v, edges[i].w});
        adj[edges[i].v].push_back({i, edges[i].u, edges[i].w});
    }

    vector<long long> dist1, cnt1_1, cnt2_1;
    vector<long long> distN, cnt1_N, cnt2_N;

    dijkstra(1, n, adj, dist1, cnt1_1, cnt2_1);
    dijkstra(n, n, adj, distN, cnt1_N, cnt2_N);

    long long D = dist1[n];
    long long total_paths1 = cnt1_1[n];
    long long total_paths2 = cnt2_1[n];

    for (int i = 0; i < m; ++i) {
        int u = edges[i].u;
        int v = edges[i].v;
        long long w = edges[i].w;

        bool critical = false;

        // Check u -> v
        if (dist1[u] + w + distN[v] == D) {
            long long p1 = (cnt1_1[u] * cnt1_N[v]) % MOD1;
            long long p2 = (cnt2_1[u] * cnt2_N[v]) % MOD2;
            if (p1 == total_paths1 && p2 == total_paths2) critical = true;
        }

        // Check v -> u
        if (dist1[v] + w + distN[u] == D) {
            long long p1 = (cnt1_1[v] * cnt1_N[u]) % MOD1;
            long long p2 = (cnt2_1[v] * cnt2_N[u]) % MOD2;
            if (p1 == total_paths1 && p2 == total_paths2) critical = true;
        }

        cout << (critical ? "Yes\n" : "No\n");
    }

    return 0;
}
```
