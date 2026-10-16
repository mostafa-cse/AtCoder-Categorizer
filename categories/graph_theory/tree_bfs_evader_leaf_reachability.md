# Tree BFS Distances and Evader Leaf Reachability

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree BFS Distances and Evader Leaf Reachability**.

---

## Curated Problems

### `[problem:AtCoder-abc148_f]` — Playing Tag on Tree
- **Rating / Difficulty**: 1457
- **Contest**: `abc148`
- **Analysis**: [`analysis/AtCoder-abc148_f.md`](../../analysis/AtCoder-abc148_f.md)
- **Key Idea**: Takahashi can safely reach any vertex x if and only if dist(u, x) < dist(v, x). Once at x, Takahashi can escape to the deepest subtree reachable before Aoki arrives, surviving until Aoki reaches that boundary.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

void bfs(int start, const vector<vector<int>>& adj, vector<int>& dist) {
    dist[start] = 0;
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, u, v;
    if (!(cin >> n >> u >> v)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    vector<int> dist_u(n + 1, -1), dist_v(n + 1, -1);
    bfs(u, adj, dist_u);
    bfs(v, adj, dist_v);

    int max_steps = 0;
    for (int i = 1; i <= n; ++i) {
        if (dist_u[i] < dist_v[i]) {
            max_steps = max(max_steps, dist_v[i] - 1);
        }
    }

    cout << max_steps << "\n";
    return 0;
}
```
