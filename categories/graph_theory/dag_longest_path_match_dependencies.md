# DAG Longest Path / Topological Sort on Match Dependencies

**Domain**: `Graph Theory`  
**Subtopic**: `Directed Graphs`  

This workbook contains curated, high-quality competitive programming problems teaching **DAG Longest Path / Topological Sort on Match Dependencies**.

---

## Curated Problems

### `[problem:AtCoder-abc139_e]` — League
- **Rating / Difficulty**: 1528
- **Contest**: `abc139`
- **Analysis**: [`analysis/AtCoder-abc139_e.md`](../../analysis/AtCoder-abc139_e.md)
- **Key Idea**: Each match between player u and v (u < v) is a node in a directed graph. A player's required order creates directed dependency edges between consecutive matches. The answer is the longest path in this DAG, or -1 if a cycle exists.
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`
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

    int n;
    if (!(cin >> n)) return 0;

    auto get_id = [&](int u, int v) -> int {
        if (u > v) swap(u, v);
        // u in 1..n-1, v in u+1..n
        return (u - 1) * n + (v - 1);
    };

    int total_nodes = n * n;
    vector<vector<int>> adj(total_nodes);
    vector<int> in_deg(total_nodes, 0);
    vector<bool> exists(total_nodes, false);

    for (int i = 1; i <= n; ++i) {
        int prev_match = -1;
        for (int j = 0; j < n - 1; ++j) {
            int opp;
            cin >> opp;
            int cur_match = get_id(i, opp);
            exists[cur_match] = true;
            if (prev_match != -1) {
                adj[prev_match].push_back(cur_match);
                in_deg[cur_match]++;
            }
            prev_match = cur_match;
        }
    }

    queue<int> q;
    vector<int> dist(total_nodes, 0);
    int active_nodes = 0;

    for (int i = 0; i < total_nodes; ++i) {
        if (exists[i]) {
            active_nodes++;
            if (in_deg[i] == 0) {
                dist[i] = 1;
                q.push(i);
            }
        }
    }

    int processed = 0;
    int max_days = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        processed++;
        max_days = max(max_days, dist[u]);

        for (int v : adj[u]) {
            dist[v] = max(dist[v], dist[u] + 1);
            if (--in_deg[v] == 0) {
                q.push(v);
            }
        }
    }

    if (processed < active_nodes) {
        cout << -1 << "\n";
    } else {
        cout << max_days << "\n";
    }

    return 0;
}
```
