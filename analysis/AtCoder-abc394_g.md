# Problem Analysis: AtCoder-abc394_g — Dense Buildings

**Problem ID**: `AtCoder-abc394_g`  
**Contest**: `abc394`  
**Rating / Difficulty**: 2031  
**URL**: https://atcoder.jp/contests/abc394/tasks/abc394_g  
**VJudge Tag**: `[problem:AtCoder-abc394_g]`  
**Category File**: [`../categories/graph_theory/kruskal_reconstruction_tree_bottleneck_path.md`](../categories/graph_theory/kruskal_reconstruction_tree_bottleneck_path.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Kruskal Reconstruction Tree Maximum Bottleneck Path Query via Binary Lifting`  

---

## 1. Problem Statement & Key Idea
An H x W grid has buildings of heights F_{r, c}. Horizontal bridges connect adjacent buildings on all floors k <= min(F_1, F_2) with 0 cost. Vertical elevator movement costs 1 per floor. Answer Q queries: min cost to travel from (A, Y_A) to (B, Y_B).

**Key Idea**: Between two buildings A and B, traveling horizontally at floor k requires a path where all edges have capacity min(F_u, F_v) >= k. The maximum floor at which horizontal traversal is possible is the maximum bottleneck capacity M(A, B) = min edge weight on the path between A and B in the Maximum Spanning Tree. If both start and destination are <= M(A, B), cost is |Y_A - Y_B|. If min(Y_A, Y_B) > M(A, B), one must descend to floor M(A, B), costing Y_A + Y_B - 2 * M(A, B). In all cases, cost = Y_A + Y_B - 2 * min({Y_A, Y_B, M(A, B)}). M(A, B) is queried via Binary Lifting on the MST in O(log(HW)).

## 2. Core Observation & Invariant
Grid skybridge travel reduces to the maximum bottleneck path problem on the grid MST, queried via LCA binary lifting.

## 3. Step-by-Step Algorithm
1. Construct edges between adjacent grid cells with weight = min(F_u, F_v).
2. Sort edges descending; build Maximum Spanning Tree (MST) using Kruskal's algorithm.
3. Root the MST tree at 1; precompute binary lifting tables for LCA and minimum edge weight along path.
4. For each query (A, Y_A, B, Y_B):
5.   Query bottleneck capacity M = min edge on path A to B in MST.
6.   Let max_bridge_floor = min({Y_A, Y_B, M}).
7.   Output Y_A + Y_B - 2 * max_bridge_floor.

## 4. Complexity Analysis
- **Time Complexity**: `O(HW log(HW) + Q log(HW))`
- **Space Complexity**: `O(HW log(HW))`

## 5. Core Algorithmic Skill & Learning Takeaway
Kruskal maximum spanning tree bottleneck path queries with binary lifting.

**Reusable Pattern**: Maximum Bottleneck Query via MST: Path bottleneck between u and v is precisely the minimum edge on the tree path in the Maximum Spanning Tree.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
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
