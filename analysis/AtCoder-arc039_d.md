# Problem Analysis: AtCoder-arc039_d — D. 旅行会社高橋君

**Problem ID**: `AtCoder-arc039_d`  
**Contest**: `arc039`  
**Rating / Difficulty**: 2550  
**URL**: https://atcoder.jp/contests/arc039/tasks/arc039_d  
**VJudge Tag**: `[problem:AtCoder-arc039_d]`  
**Category File**: [`../categories/graph_theory/travel_agency_bridge_block_tree_lca.md`](../categories/graph_theory/travel_agency_bridge_block_tree_lca.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Connectivity`  
- **Topic (Skill)**: `Articulation Bridges and Bridge Tree`  

---

## 1. Problem Statement & Key Idea
Given an undirected connected graph, answer $Q$ queries: does there exist a trail (no repeated edges) from $A$ to $C$ passing through $B$? Contract all 2-edge-connected components (2-ECCs) by finding bridges using Tarjan's algorithm to construct the Bridge Block Tree. In any 2-ECC, any two vertices have two edge-disjoint paths between them. Thus, a valid trail exists if and only if $B$'s component lies on the tree path between $A$'s component and $C$'s component.

## 2. Core Observation & Invariant
In the Bridge Block Tree, component $comp[B]$ lies on the simple tree path between $comp[A]$ and $comp[C]$ if and only if $\text{dist}(comp[A], comp[B]) + \text{dist}(comp[B], comp[C]) == \text{dist}(comp[A], comp[C])$. Tree distances are computed in $O(\log N)$ using binary lifting and LCA.

## 3. Step-by-Step Algorithm
1. 1. Find all bridges using Tarjan's DFS algorithm (`low` and `tin` arrays).
2. 2. Contract non-bridge edges to assign 2-ECC component IDs $comp[1 \dots N]$.
3. 3. Build the Bridge Block Tree connecting components with bridge edges.
4. 4. Precompute binary lifting table `up[u][20]` and `depth[u]` for LCA queries on the tree.
5. 5. For each query $(A, B, C)$, output `OK` if $\text{dist}(comp[A], comp[B]) + \text{dist}(comp[B], comp[C]) == \text{dist}(comp[A], comp[C])$, else `NG`.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M + Q \log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int to, id;
};

const int MAXN = 100005;
vector<Edge> adj[MAXN];
int tin[MAXN], low[MAXN], timer = 0;
bool is_bridge[200005];

void dfs_bridges(int u, int p_edge) {
    tin[u] = low[u] = ++timer;
    for (const auto& e : adj[u]) {
        if (e.id == p_edge) continue;
        if (tin[e.to]) {
            low[u] = min(low[u], tin[e.to]);
        } else {
            dfs_bridges(e.to, e.id);
            low[u] = min(low[u], low[e.to]);
            if (low[e.to] > tin[u]) {
                is_bridge[e.id] = true;
            }
        }
    }
}

int comp[MAXN], comp_cnt = 0;
void dfs_comp(int u, int c) {
    comp[u] = c;
    for (const auto& e : adj[u]) {
        if (is_bridge[e.id]) continue;
        if (!comp[e.to]) {
            dfs_comp(e.to, c);
        }
    }
}

// Tree on 2-ECC
vector<int> tree_adj[MAXN];
int up[MAXN][20], depth[MAXN];

void dfs_tree(int u, int p, int d) {
    depth[u] = d;
    up[u][0] = p;
    for (int i = 1; i < 20; ++i) {
        up[u][i] = up[up[u][i - 1]][i - 1];
    }
    for (int v : tree_adj[u]) {
        if (v != p) {
            dfs_tree(v, u, d + 1);
        }
    }
}

int get_lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    int diff = depth[u] - depth[v];
    for (int i = 0; i < 20; ++i) {
        if ((diff >> i) & 1) u = up[u][i];
    }
    if (u == v) return u;
    for (int i = 19; i >= 0; --i) {
        if (up[u][i] != up[v][i]) {
            u = up[u][i];
            v = up[v][i];
        }
    }
    return up[u][0];
}

int dist_tree(int u, int v) {
    return depth[u] + depth[v] - 2 * depth[get_lca(u, v)];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<pair<int, int>> edge_list(m);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
        edge_list[i] = {u, v};
    }

    dfs_bridges(1, -1);

    for (int i = 1; i <= n; ++i) {
        if (!comp[i]) {
            dfs_comp(i, ++comp_cnt);
        }
    }

    for (int i = 0; i < m; ++i) {
        if (is_bridge[i]) {
            int cu = comp[edge_list[i].first];
            int cv = comp[edge_list[i].second];
            tree_adj[cu].push_back(cv);
            tree_adj[cv].push_back(cu);
        }
    }

    dfs_tree(1, 1, 0);

    int q;
    if (cin >> q) {
        while (q--) {
            int a, b, c;
            cin >> a >> b >> c;
            int ca = comp[a], cb = comp[b], cc = comp[c];
            if (dist_tree(ca, cb) + dist_tree(cb, cc) == dist_tree(ca, cc)) {
                cout << "OK\n";
            } else {
                cout << "NG\n";
            }
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
