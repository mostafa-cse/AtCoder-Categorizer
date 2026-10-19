# Problem Analysis: AtCoder-abc301_h — Ex. Difference of Distance

**Problem ID**: `AtCoder-abc301_h`  
**Contest**: `abc301`  
**Rating / Difficulty**: 2898  
**URL**: https://atcoder.jp/contests/abc301/tasks/abc301_h  
**VJudge Tag**: `[problem:AtCoder-abc301_h]`  
**Category File**: [`../categories/data_structures/kruskal_reconstruction_tree_bottleneck_sensitivity.md`](../categories/data_structures/kruskal_reconstruction_tree_bottleneck_sensitivity.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)`  

---

## 1. Problem Statement & Key Idea
In a weighted undirected graph, process queries asking: if the weight of edge e is increased from w to w', how does the bottleneck shortest path distance between u and v change?

## 2. Core Observation & Invariant
Bottleneck path distance between u and v is given by their LCA on the Kruskal Reconstruction Tree (KRT). Changing edge e's weight affects the distance iff e was a bottleneck bridge in the threshold graph at weight W. By building the KRT and maintaining 2-edge-connected components (2ECC bridge-block trees) layer-by-layer, we can detect whether alternative paths exist at weight W.

## 3. Step-by-Step Algorithm
1. 1. Sort edges by weight and construct Kruskal Reconstruction Tree (KRT).
2. 2. Decompose graph into 2-edge-connected components at each weight threshold.
3. 3. For each query (u, v, e), check if e is the unique bridge on the bottleneck path.
4. 4. If e is unique bridge, return the alternative weight from the 2ECC tree; otherwise distance is unchanged.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M + Q) log N)`
- **Space Complexity**: `O(N + M + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v;
    int w;
    int id;
};

struct Query {
    int id;
    int edge_id;
    int s, t;
};

struct DSU {
    vector<int> parent;
    DSU(int n) : parent(n + 1) {
        for (int i = 0; i <= n; ++i) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int ri = find(i);
        int rj = find(j);
        if (ri != rj) {
            parent[ri] = rj;
            return true;
        }
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<Edge> edges(m + 1);
    vector<vector<int>> weight_to_edges(m + 1);

    for (int i = 1; i <= m; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
        edges[i].id = i;
        if (edges[i].w <= m) {
            weight_to_edges[edges[i].w].push_back(i);
        }
    }

    int q;
    cin >> q;
    vector<Query> queries(q);
    vector<vector<int>> edge_to_queries(m + 1);
    for (int i = 0; i < q; ++i) {
        queries[i].id = i;
        cin >> queries[i].edge_id >> queries[i].s >> queries[i].t;
        edge_to_queries[queries[i].edge_id].push_back(i);
    }

    vector<int> ans(q, 0);
    DSU dsu(n);

    for (int w = 1; w <= m; ++w) {
        const auto& e_list = weight_to_edges[w];
        if (e_list.empty()) continue;

        vector<int> nodes;
        for (int e_idx : e_list) {
            int ru = dsu.find(edges[e_idx].u);
            int rv = dsu.find(edges[e_idx].v);
            nodes.push_back(ru);
            nodes.push_back(rv);
        }
        sort(nodes.begin(), nodes.end());
        nodes.erase(unique(nodes.begin(), nodes.end()), nodes.end());

        // Map original DSU roots to 0..K-1
        int K = nodes.size();
        auto get_id = [&](int r) -> int {
            return lower_bound(nodes.begin(), nodes.end(), r) - nodes.begin();
        };

        vector<vector<pair<int, int>>> adj(K);
        for (int e_idx : e_list) {
            int u = get_id(dsu.find(edges[e_idx].u));
            int v = get_id(dsu.find(edges[e_idx].v));
            adj[u].push_back({v, e_idx});
            adj[v].push_back({u, e_idx});
        }

        // Find bridges using Tarjan
        vector<int> tin(K, -1), low(K, -1);
        int timer = 0;
        vector<bool> is_bridge(m + 1, false);

        auto dfs_bridge = [&](auto& self, int u, int p_edge) -> void {
            tin[u] = low[u] = ++timer;
            for (auto& edge_info : adj[u]) {
                int v = edge_info.first;
                int e_idx = edge_info.second;
                if (e_idx == p_edge) continue;
                if (tin[v] != -1) {
                    low[u] = min(low[u], tin[v]);
                } else {
                    self(self, v, e_idx);
                    low[u] = min(low[u], low[v]);
                    if (low[v] > tin[u]) {
                        is_bridge[e_idx] = true;
                    }
                }
            }
        };

        for (int i = 0; i < K; ++i) {
            if (tin[i] == -1) {
                dfs_bridge(dfs_bridge, i, -1);
            }
        }

        // Bridge-Block Tree (2ECC)
        vector<int> comp(K, -1);
        int num_comps = 0;

        auto dfs_2ecc = [&](auto& self, int u, int c_id) -> void {
            comp[u] = c_id;
            for (auto& edge_info : adj[u]) {
                int v = edge_info.first;
                int e_idx = edge_info.second;
                if (is_bridge[e_idx] || comp[v] != -1) continue;
                self(self, v, c_id);
            }
        };

        for (int i = 0; i < K; ++i) {
            if (comp[i] == -1) {
                dfs_2ecc(dfs_2ecc, i, num_comps++);
            }
        }

        // Tree of 2ECCs
        vector<vector<pair<int, int>>> tree_adj(num_comps);
        vector<int> bridge_child(m + 1, -1);

        for (int e_idx : e_list) {
            if (is_bridge[e_idx]) {
                int cu = comp[get_id(dsu.find(edges[e_idx].u))];
                int cv = comp[get_id(dsu.find(edges[e_idx].v))];
                tree_adj[cu].push_back({cv, e_idx});
                tree_adj[cv].push_back({cu, e_idx});
            }
        }

        // Root each component of tree and assign in/out Euler tour times
        vector<int> in_time(num_comps, 0), out_time(num_comps, 0);
        int tree_timer = 0;
        vector<bool> tree_vis(num_comps, false);

        auto dfs_tree = [&](auto& self, int u, int p) -> void {
            tree_vis[u] = true;
            in_time[u] = ++tree_timer;
            for (auto& edge_info : tree_adj[u]) {
                int v = edge_info.first;
                int e_idx = edge_info.second;
                if (v == p) continue;
                bridge_child[e_idx] = v;
                self(self, v, u);
            }
            out_time[u] = tree_timer;
        };

        for (int i = 0; i < num_comps; ++i) {
            if (!tree_vis[i]) {
                dfs_tree(dfs_tree, i, -1);
            }
        }

        auto in_subtree = [&](int v_comp, int child_comp) -> bool {
            return in_time[child_comp] <= in_time[v_comp] && out_time[v_comp] <= out_time[child_comp];
        };

        // Answer queries for bridges in this layer
        for (int e_idx : e_list) {
            if (is_bridge[e_idx] && !edge_to_queries[e_idx].empty()) {
                int ch = bridge_child[e_idx];
                for (int q_idx : edge_to_queries[e_idx]) {
                    int s = queries[q_idx].s;
                    int t = queries[q_idx].t;
                    int rs = dsu.find(s);
                    int rt = dsu.find(t);

                    // Check if both are in this layer's nodes
                    auto it_s = lower_bound(nodes.begin(), nodes.end(), rs);
                    auto it_t = lower_bound(nodes.begin(), nodes.end(), rt);

                    if (it_s != nodes.end() && *it_s == rs && it_t != nodes.end() && *it_t == rt) {
                        int comp_s = comp[it_s - nodes.begin()];
                        int comp_t = comp[it_t - nodes.begin()];
                        bool s_in = in_subtree(comp_s, ch);
                        bool t_in = in_subtree(comp_t, ch);
                        if (s_in != t_in) {
                            ans[q_idx] = 1;
                        }
                    }
                }
            }
        }

        // Union all edges of this layer in DSU
        for (int e_idx : e_list) {
            dsu.unite(edges[e_idx].u, edges[e_idx].v);
        }
    }

    for (int i = 0; i < q; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
