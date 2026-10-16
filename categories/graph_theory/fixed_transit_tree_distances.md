# Fixed Transit Vertex Root-Referenced Tree Distances

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Fixed Transit Vertex Root-Referenced Tree Distances**.

---

## Curated Problems

### [problem:AtCoder-abc070_d] — Transit Tree Path
- **Contest**: `abc070`
- **Rating / Difficulty**: 1182
- **Specific Skill**: Fixed Transit Vertex Root-Referenced Tree Distances
- **Individual Analysis**: [`../../analysis/AtCoder-abc070_d.md`](../../analysis/AtCoder-abc070_d.md)
- **Problem Statement Summary**: Given a weighted tree with N vertices. Q queries: find the shortest path distance between x and y that passes through a fixed transit vertex K.
- **Core Insight**: Reroot the tree at vertex K! Run a single BFS or DFS from K to precompute dist[v] = distance from K to v for all v in O(N). Each query (x, y) is answered in O(1) via dist[x] + dist[y].
- **Complexity**: Time: `O(N + Q)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int to;
    long long w;
};

void dfs(int u, int p, long long d, const vector<vector<Edge>>& adj, vector<long long>& dist) {
    dist[u] = d;
    for (const auto& e : adj[u]) {
        if (e.to != p) {
            dfs(e.to, u, d + e.w, adj, dist);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    int q, k;
    cin >> q >> k;

    vector<long long> dist(n + 1, 0);
    dfs(k, 0, 0, adj, dist);

    while (q--) {
        int x, y;
        cin >> x >> y;
        cout << dist[x] + dist[y] << "\n";
    }

    return 0;
}
```
