# Modulo-3 Expanded Graph Shortest Path BFS

**Domain**: `Graph Theory`  
**Subtopic**: `Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Modulo-3 Expanded Graph Shortest Path BFS**.

---

## Curated Problems

### `[problem:AtCoder-abc132_e]` — Hopscotch Addict
- **Rating / Difficulty**: 1625
- **Contest**: `abc132`
- **Analysis**: [`analysis/AtCoder-abc132_e.md`](../../analysis/AtCoder-abc132_e.md)
- **Key Idea**: Split each vertex v into 3 states: (v, 0), (v, 1), and (v, 2) representing the step count modulo 3. Traversing an edge (u, v) advances state (u, m) to (v, (m + 1) % 3).
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

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
    }

    int s, t;
    cin >> s >> t;

    vector<vector<int>> dist(n + 1, vector<int>(3, -1));
    queue<pair<int, int>> q;

    dist[s][0] = 0;
    q.push({s, 0});

    while (!q.empty()) {
        auto [u, step] = q.front();
        q.pop();

        if (u == t && step == 0) {
            cout << dist[u][0] / 3 << "\n";
            return 0;
        }

        int next_step = (step + 1) % 3;
        for (int v : adj[u]) {
            if (dist[v][next_step] == -1) {
                dist[v][next_step] = dist[u][step] + 1;
                q.push({v, next_step});
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}
```
