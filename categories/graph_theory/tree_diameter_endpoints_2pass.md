# Tree Diameter Endpoints via 2-Pass BFS/DFS

**Domain**: `Graph Theory`  
**Subtopic**: `Tree Diameter`  

This workbook contains curated, high-quality competitive programming problems teaching **Tree Diameter Endpoints via 2-Pass BFS/DFS**.

---

## Curated Problems

### `[problem:AtCoder-arc022_3]` — Romeo and Juliet
- **Rating / Difficulty**: 1694
- **Contest**: `arc022`
- **Analysis**: [`analysis/AtCoder-arc022_3.md`](../../analysis/AtCoder-arc022_3.md)
- **Key Idea**: Canonical 2-pass BFS algorithm: 1) Run BFS from an arbitrary starting vertex (e.g. 1) to find the farthest vertex u; 2) Run BFS from vertex u to find the farthest vertex v. (u, v) is guaranteed to be a diameter of the tree.
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

pair<int, int> bfs(int start, int n, const vector<vector<int>>& adj) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    dist[start] = 0;
    q.push(start);

    int farthest_node = start;
    int max_d = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        if (dist[u] > max_d) {
            max_d = dist[u];
            farthest_node = u;
        }

        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return {farthest_node, max_d};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto [u, d1] = bfs(1, n, adj);
    auto [v, d2] = bfs(u, n, adj);

    cout << u << " " << v << "\n";
    return 0;
}
```
