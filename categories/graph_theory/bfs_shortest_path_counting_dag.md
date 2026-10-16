# BFS Shortest Path Counting on DAG

**Domain**: `Graph Theory`  
**Subtopic**: `BFS`  

This workbook contains curated, high-quality competitive programming problems teaching **BFS Shortest Path Counting on DAG**.

---

## Curated Problems

### [problem:AtCoder-abc021_c] — Shortest Path Count
- **Contest**: `abc021`
- **Rating / Difficulty**: 1324
- **Specific Skill**: BFS Shortest Path Counting on DAG
- **Individual Analysis**: [`../../analysis/AtCoder-abc021_c.md`](../../analysis/AtCoder-abc021_c.md)
- **Problem Statement Summary**: An unweighted connected graph with N vertices and M edges. Count the number of shortest paths from vertex a to vertex b, modulo 10^9 + 7.
- **Core Insight**: When popping vertex u in BFS: for neighbor v: (1) if dist[v] == -1 (first time seen), set dist[v] = dist[u] + 1, ways[v] = ways[u], and push v to queue; (2) if dist[v] == dist[u] + 1 (another shortest path to v), add ways[u] to ways[v] modulo 10^9 + 7.
- **Complexity**: Time: `O(N + M)` | Space: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a, b, m;
    if (!(cin >> n >> a >> b >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist(n + 1, -1);
    vector<long long> ways(n + 1, 0);
    queue<int> q;

    dist[a] = 0;
    ways[a] = 1;
    q.push(a);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                ways[v] = ways[u];
                q.push(v);
            } else if (dist[v] == dist[u] + 1) {
                ways[v] = (ways[v] + ways[u]) % MOD;
            }
        }
    }

    cout << ways[b] << "\n";
    return 0;
}
```
