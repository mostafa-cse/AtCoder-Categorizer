# Bellman-Ford Constrained Negative Cycle Reachability (1 -> cycle -> N)

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Bellman-Ford Constrained Negative Cycle Reachability (1 -> cycle -> N)**.

---

## Curated Problems

### `[problem:AtCoder-abc137_e]` — Coins Respawn
- **Rating / Difficulty**: 1740
- **Contest**: `abc137`
- **Analysis**: [`analysis/AtCoder-abc137_e.md`](../../analysis/AtCoder-abc137_e.md)
- **Key Idea**: Negate rewards to edge weights w_i = P - C_i to convert into shortest path. An infinite gain exists iff there is a negative cycle that is simultaneously reachable from 1 AND can reach N.
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int u, v;
    long long w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long long p;
    if (!(cin >> n >> m >> p)) return 0;

    vector<Edge> edges;
    vector<vector<int>> fwd(n + 1), bwd(n + 1);

    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        edges.push_back({u, v, p - c});
        fwd[u].push_back(v);
        bwd[v].push_back(u);
    }

    // Reachability from 1
    vector<bool> from1(n + 1, false);
    queue<int> q;
    from1[1] = true;
    q.push(1);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : fwd[u]) {
            if (!from1[v]) {
                from1[v] = true;
                q.push(v);
            }
        }
    }

    // Reachability to N
    vector<bool> toN(n + 1, false);
    toN[n] = true;
    q.push(n);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : bwd[u]) {
            if (!toN[v]) {
                toN[v] = true;
                q.push(v);
            }
        }
    }

    vector<Edge> active_edges;
    for (auto& e : edges) {
        if (from1[e.u] && toN[e.u] && from1[e.v] && toN[e.v]) {
            active_edges.push_back(e);
        }
    }

    vector<long long> dist(n + 1, INF);
    dist[1] = 0;

    for (int iter = 1; iter < n; ++iter) {
        for (auto& e : active_edges) {
            if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
                dist[e.v] = dist[e.u] + e.w;
            }
        }
    }

    bool has_neg_cycle = false;
    for (auto& e : active_edges) {
        if (dist[e.u] != INF && dist[e.u] + e.w < dist[e.v]) {
            has_neg_cycle = true;
            break;
        }
    }

    if (has_neg_cycle) {
        cout << -1 << "\n";
    } else {
        cout << max(0LL, -dist[n]) << "\n";
    }

    return 0;
}
```
