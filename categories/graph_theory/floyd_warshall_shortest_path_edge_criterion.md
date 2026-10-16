# Floyd-Warshall Edge Shortest Path Criterion

**Domain**: `Graph Theory`  
**Subtopic**: `All-Pairs Shortest Paths`  

This workbook contains curated, high-quality competitive programming problems teaching **Floyd-Warshall Edge Shortest Path Criterion**.

---

## Curated Problems

### `[problem:AtCoder-abc051_d]` — Candidates of No Shortest Paths
- **Rating / Difficulty**: 1566
- **Contest**: `abc051`
- **Analysis**: [`analysis/AtCoder-abc051_d.md`](../../analysis/AtCoder-abc051_d.md)
- **Key Idea**: Precompute all-pairs shortest paths using Floyd-Warshall. An edge e = (u, v, w) is used in a shortest path between some pair (s, t) if and only if dist[s][u] + w + dist[v][t] == dist[s][t] (or with u and v swapped).
- **Time Complexity**: `O(N^3 + M)`
- **Space Complexity**: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct Edge {
    int u, v, w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));
    for (int i = 1; i <= n; ++i) dist[i][i] = 0;

    vector<Edge> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        dist[edges[i].u][edges[i].v] = min(dist[edges[i].u][edges[i].v], edges[i].w);
        dist[edges[i].v][edges[i].u] = min(dist[edges[i].v][edges[i].u], edges[i].w);
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    int unused = 0;
    for (const auto& e : edges) {
        if (dist[e.u][e.v] < e.w) {
            unused++;
        }
    }

    cout << unused << "\n";
    return 0;
}
```
