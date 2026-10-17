# Induced Directed Cycle Extraction via Shortest Cycle BFS Search

**Domain**: `Graph Theory`  
**Subtopic**: `Cycles / BFS`  

This workbook contains curated, high-quality competitive programming problems teaching **Induced Directed Cycle Extraction via Shortest Cycle BFS Search**.

---

## Curated Problems

### `[problem:AtCoder-abc142_f]` — Pure
- **Rating / Difficulty**: 1919
- **Contest**: `abc142`
- **Analysis**: [`analysis/AtCoder-abc142_f.md`](../../analysis/AtCoder-abc142_f.md)
- **Key Idea**: Any chord in a directed cycle splits it into strictly shorter directed cycles. Therefore, a directed cycle of MINIMUM LENGTH in the graph cannot have any chord edges, making it guaranteed to be an induced cycle! Finding the shortest directed cycle is achieved by running BFS from every vertex s in O(N * (N + M)).
- **Time Complexity**: `O(N * (N + M))`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

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

    int min_len = n + 1;
    vector<int> best_cycle;

    for (int s = 1; s <= n; ++s) {
        vector<int> dist(n + 1, -1);
        vector<int> parent(n + 1, -1);
        queue<int> q;

        dist[s] = 0;
        q.push(s);

        int cycle_end = -1;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            bool found = false;
            for (int v : adj[u]) {
                if (v == s && dist[u] + 1 < min_len) {
                    min_len = dist[u] + 1;
                    cycle_end = u;
                    found = true;
                    break;
                }
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.push(v);
                }
            }
            if (found) break;
        }

        if (cycle_end != -1) {
            vector<int> path;
            int curr = cycle_end;
            while (curr != s) {
                path.push_back(curr);
                curr = parent[curr];
            }
            path.push_back(s);
            reverse(path.begin(), path.end());
            best_cycle = path;
        }
    }

    if (best_cycle.empty()) {
        cout << -1 << "\n";
    } else {
        cout << best_cycle.size() << "\n";
        for (int node : best_cycle) {
            cout << node << "\n";
        }
    }

    return 0;
}
```
