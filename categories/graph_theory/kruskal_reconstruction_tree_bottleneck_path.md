# Kruskal Reconstruction Tree Maximum Bottleneck Path Query via Binary Lifting

**Domain**: `Graph Theory`  
**Subtopic**: `Trees`  

This workbook contains curated, high-quality competitive programming problems teaching **Kruskal Reconstruction Tree Maximum Bottleneck Path Query via Binary Lifting**.

---

## Curated Problems

### `[problem:AtCoder-abc394_g]` — Dense Buildings
- **Rating / Difficulty**: 2031
- **Contest**: `abc394`
- **Analysis**: [`analysis/AtCoder-abc394_g.md`](../../analysis/AtCoder-abc394_g.md)
- **Key Idea**: Between two buildings A and B, traveling horizontally at floor k requires a path where all edges have capacity min(F_u, F_v) >= k. The maximum floor at which horizontal traversal is possible is the maximum bottleneck capacity M(A, B) = min edge weight on the path between A and B in the Maximum Spanning Tree. If both start and destination are <= M(A, B), cost is |Y_A - Y_B|. If min(Y_A, Y_B) > M(A, B), one must descend to floor M(A, B), costing Y_A + Y_B - 2 * M(A, B). In all cases, cost = Y_A + Y_B - 2 * min({Y_A, Y_B, M(A, B)}). M(A, B) is queried via Binary Lifting on the MST in O(log(HW)).
- **Time Complexity**: `O(HW log(HW) + Q log(HW))`
- **Space Complexity**: `O(HW log(HW))`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

struct Edge {
    int u, v, w;
    bool operator<(const Edge& other) const {
        return w > other.w; // descending for Max ST
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

struct TreeEdge {
    int to, w;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<vector<int>> f(h, vector<int>(w));
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            cin >> f[i][j];
        }
    }

    auto get_id = [&](int r, int c) {
        return r * w + c + 1;
    };

    int total_nodes = h * w;
    vector<Edge> edges;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            int u = get_id(r, c);
            if (r + 1 < h) {
                edges.push_back({u, get_id(r + 1, c), min(f[r][c], f[r + 1][c])});
            }
            if (c + 1 < w) {
                edges.push_back({u, get_id(r, c + 1), min(f[r][c], f[r][c + 1])});
            }
        }
    }

    sort(edges.begin(), edges.end());

    DSU dsu(total_nodes);
    vector<vector<TreeEdge>> adj(total_nodes + 1);

    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            adj[e.u].push_back({e.v, e.w});
            adj[e.v].push_back({e.u, e.w});
        }
    }

    int log_n = 0;
    while ((1 << log_n) <= total_nodes) log_n++;

    vector<vector<int>> up(log_n, vector<int>(total_nodes + 1, 0));
    vector<vector<int>> min_edge(log_n, vector<int>(total_nodes + 1, INF));
    vector<int> depth(total_nodes + 1, 0);

    auto dfs = [&](auto& self, int u, int p, int d, int w_up) -> void {
        up[0][u] = p;
        min_edge[0][u] = w_up;
        depth[u] = d;

        for (const auto& edge : adj[u]) {
            if (edge.to != p) {
                self(self, edge.to, u, d + 1, edge.w);
            }
        }
    };

    dfs(dfs, 1, 1, 0, INF);

    for (int k = 1; k < log_n; ++k) {
        for (int i = 1; i <= total_nodes; ++i) {
            up[k][i] = up[k - 1][up[k - 1][i]];
            min_edge[k][i] = min(min_edge[k - 1][i], min_edge[k - 1][up[k - 1][i]]);
        }
    }

    auto query_bottleneck = [&](int u, int v) {
        if (u == v) return INF;
        int res = INF;

        if (depth[u] < depth[v]) swap(u, v);

        for (int k = log_n - 1; k >= 0; --k) {
            if (depth[u] - (1 << k) >= depth[v]) {
                res = min(res, min_edge[k][u]);
                u = up[k][u];
            }
        }

        if (u == v) return res;

        for (int k = log_n - 1; k >= 0; --k) {
            if (up[k][u] != up[k][v]) {
                res = min({res, min_edge[k][u], min_edge[k][v]});
                u = up[k][u];
                v = up[k][v];
            }
        }

        res = min({res, min_edge[0][u], min_edge[0][v]});
        return res;
    };

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int r1, c1, y1, r2, c2, y2;
        cin >> r1 >> c1 >> y1 >> r2 >> c2 >> y2;
        --r1; --c1; --r2; --c2;

        int u = get_id(r1, c1);
        int v = get_id(r2, c2);

        int bottleneck = query_bottleneck(u, v);
        int max_bridge = min({y1, y2, bottleneck});

        long long ans = (long long)y1 + y2 - 2LL * max_bridge;
        cout << ans << "\n";
    }

    return 0;
}
```
