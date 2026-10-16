# Multi-Source BFS on K Targets + TSP Bitmask DP

**Domain**: `Graph Theory`  
**Subtopic**: `Traveling Salesperson Problem`  

This workbook contains curated, high-quality competitive programming problems teaching **Multi-Source BFS on K Targets + TSP Bitmask DP**.

---

## Curated Problems

### `[problem:AtCoder-abc190_e]` — Magical Ornament
- **Rating / Difficulty**: 1645
- **Contest**: `abc190`
- **Analysis**: [`analysis/AtCoder-abc190_e.md`](../../analysis/AtCoder-abc190_e.md)
- **Key Idea**: Compute all-pairs shortest paths between the K targets using K runs of BFS. Then solve the Traveling Salesperson Problem (TSP) on the complete graph of K targets using bitmask DP.
- **Time Complexity**: `O(K * (N + M) + K^2 * 2^K)`
- **Space Complexity**: `O(K * 2^K + N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int k;
    cin >> k;
    vector<int> c(k);
    for (int i = 0; i < k; ++i) {
        cin >> c[i];
    }

    // Pairwise distance matrix between targets
    vector<vector<int>> dist(k, vector<int>(k, INF));

    for (int i = 0; i < k; ++i) {
        vector<int> d(n + 1, -1);
        queue<int> q;
        d[c[i]] = 0;
        q.push(c[i]);

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (d[v] == -1) {
                    d[v] = d[u] + 1;
                    q.push(v);
                }
            }
        }

        for (int j = 0; j < k; ++j) {
            if (d[c[j]] != -1) {
                dist[i][j] = d[c[j]];
            }
        }
    }

    // TSP Bitmask DP
    int total_masks = 1 << k;
    vector<vector<int>> dp(total_masks, vector<int>(k, INF));

    for (int i = 0; i < k; ++i) {
        dp[1 << i][i] = 1; // 1 vertex visited
    }

    for (int mask = 1; mask < total_masks; ++mask) {
        for (int u = 0; u < k; ++u) {
            if (dp[mask][u] == INF) continue;

            for (int v = 0; v < k; ++v) {
                if (!(mask & (1 << v))) {
                    if (dist[u][v] < INF) {
                        dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + dist[u][v]);
                    }
                }
            }
        }
    }

    int ans = INF;
    for (int i = 0; i < k; ++i) {
        ans = min(ans, dp[total_masks - 1][i]);
    }

    cout << (ans >= INF ? -1 : ans) << "\n";
    return 0;
}
```
