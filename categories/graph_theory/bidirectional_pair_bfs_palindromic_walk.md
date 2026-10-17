# Bidirectional Symmetric Pair BFS for Shortest Palindromic Graph Walk

**Domain**: `Graph Theory`  
**Subtopic**: `BFS / State Graphs`  

This workbook contains curated, high-quality competitive programming problems teaching **Bidirectional Symmetric Pair BFS for Shortest Palindromic Graph Walk**.

---

## Curated Problems

### `[problem:AtCoder-abc197_f]` — Construct a Palindrome
- **Rating / Difficulty**: 1945
- **Contest**: `abc197`
- **Analysis**: [`analysis/AtCoder-abc197_f.md`](../../analysis/AtCoder-abc197_f.md)
- **Key Idea**: A palindrome is symmetric: start from both endpoints (1, N) simultaneously. Define BFS state as (u, v) where u starts at 1 and v starts at N. From state (u, v), step to (u', v') if u has edge u -> u' labeled c and v has edge v -> v' with the same label c, increasing step distance by 2. When u == v, walk length is 2 * dist. When u and v share an edge, walk length is 2 * dist + 1.
- **Time Complexity**: `O(N^2 + M^2)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

const int INF = 1e9;

struct Edge {
    int to;
    char c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    vector<vector<int>> is_edge(n + 1, vector<int>(n + 1, 0));

    for (int i = 0; i < m; ++i) {
        int u, v;
        char c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
        is_edge[u][v] = 1;
        is_edge[v][u] = 1;
    }

    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));
    queue<pair<int, int>> q;

    dist[1][n] = 0;
    q.push({1, n});

    int ans = INF;

    while (!q.empty()) {
        auto [u, v] = q.front();
        q.pop();

        int d = dist[u][v];

        if (u == v) {
            ans = min(ans, 2 * d);
        }
        if (is_edge[u][v]) {
            ans = min(ans, 2 * d + 1);
        }

        for (const auto& eu : adj[u]) {
            for (const auto& ev : adj[v]) {
                if (eu.c == ev.c) {
                    if (dist[eu.to][ev.to] > d + 1) {
                        dist[eu.to][ev.to] = d + 1;
                        q.push({eu.to, ev.to});
                    }
                }
            }
        }
    }

    if (ans >= INF) {
        cout << -1 << "\n";
    } else {
        cout << ans << "\n";
    }

    return 0;
}
```
