# Spanning Tree Constructive Node Coloring

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Spanning Tree Constructive Node Coloring**.

---

## Curated Problems

### `[problem:AtCoder-arc108_c]` — Keep Graph Connected
- **Rating / Difficulty**: 1460
- **Contest**: `arc108`
- **Analysis**: [`analysis/AtCoder-arc108_c.md`](../../analysis/AtCoder-arc108_c.md)
- **Key Idea**: Extract any spanning tree. Root it arbitrarily and assign labels top-down via DFS/BFS: each child v is assigned the label of its tree edge to parent u; if that matches parent u's label, assign an alternative unused label.
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int to;
    int label;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    vector<int> ans(n + 1, 0);
    vector<bool> visited(n + 1, false);
    queue<int> q;

    ans[1] = 1;
    visited[1] = true;
    q.push(1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (const auto& edge : adj[u]) {
            int v = edge.to;
            int c = edge.label;
            if (!visited[v]) {
                visited[v] = true;
                if (ans[u] != c) {
                    ans[v] = c;
                } else {
                    ans[v] = (c % n) + 1;
                }
                q.push(v);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
