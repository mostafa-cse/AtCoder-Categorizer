# Strong Connectivity Graph Orientation and DFS Tree Back-Edge Directing

**Domain**: `Graph Theory`  
**Subtopic**: `Directed Graphs`  

This workbook contains curated, high-quality competitive programming problems teaching **Strong Connectivity Graph Orientation and DFS Tree Back-Edge Directing**.

---

## Curated Problems

### `[problem:AtCoder-arc111_d]` — Orientation
- **Rating / Difficulty**: 2064
- **Contest**: `arc111`
- **Analysis**: [`analysis/AtCoder-arc111_d.md`](../../analysis/AtCoder-arc111_d.md)
- **Key Idea**: If c_u > c_v, v cannot reach u (otherwise c_v >= c_u), so edge (u, v) must be directed u -> v. If c_u < c_v, it must be directed v -> u. If c_u == c_v, u and v must be mutually reachable and belong to the same Strongly Connected Component (SCC). We can orient the subgraph of edges with c_u == c_v into a strongly connected directed graph using Robbins' Theorem / DFS tree orientation: direct tree edges downward (parent -> child) and back-edges upward (descendant -> ancestor).
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v;
    }

    vector<int> c(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> c[i];
    }

    vector<string> ans(m);
    vector<vector<pair<int, int>>> adj_eq(n + 1);

    for (int i = 0; i < m; ++i) {
        int u = edges[i].u;
        int v = edges[i].v;
        if (c[u] > c[v]) {
            ans[i] = "->";
        } else if (c[u] < c[v]) {
            ans[i] = "<-";
        } else {
            adj_eq[u].push_back({v, i});
            adj_eq[v].push_back({u, i});
        }
    }

    vector<bool> visited(n + 1, false);
    vector<int> dep(n + 1, 0);

    auto dfs = [&](auto& self, int u, int p_edge, int d) -> void {
        visited[u] = true;
        dep[u] = d;
        for (auto& edge_info : adj_eq[u]) {
            int v = edge_info.first;
            int idx = edge_info.second;
            if (idx == p_edge) continue;
            if (visited[v]) {
                if (dep[v] < dep[u]) {
                    if (edges[idx].u == u) ans[idx] = "->";
                    else ans[idx] = "<-";
                }
            } else {
                if (edges[idx].u == u) ans[idx] = "->";
                else ans[idx] = "<-";
                self(self, v, idx, d + 1);
            }
        }
    };

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            dfs(dfs, i, -1, 1);
        }
    }

    for (int i = 0; i < m; ++i) {
        cout << ans[i] << "\n";
    }
    return 0;
}
```
