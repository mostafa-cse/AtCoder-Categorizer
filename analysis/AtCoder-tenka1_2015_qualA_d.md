# Problem Analysis: AtCoder-tenka1_2015_qualA_d — D. ハシポン (Hashipon)

**Problem ID**: `AtCoder-tenka1_2015_qualA_d`  
**Contest**: `tenka1-2015-quala`  
**Rating / Difficulty**: 2559  
**URL**: https://atcoder.jp/contests/tenka1-2015-quala/tasks/tenka1_2015_qualA_d  
**VJudge Tag**: `[problem:AtCoder-tenka1_2015_qualA_d]`  
**Category File**: [`../categories/graph_theory/hashipon_bridge_block_tree.md`](../categories/graph_theory/hashipon_bridge_block_tree.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Connectivity`  
- **Topic (Skill)**: `Articulation Bridges and Bridge Tree`  

---

## 1. Problem Statement & Key Idea
Given an undirected connected graph G, find the minimum number of additional edges needed to make the entire graph 2-edge-connected (bridge-free).

## 2. Core Observation & Invariant
A graph is 2-edge-connected if and only if it has no bridges. By finding all 2-edge-connected components (biconnected components via Tarjan or DFS bridge-finding algorithm) and contracting each component into a single vertex, the graph collapses into a bridge-block tree (2-edge-connected component tree). To make a tree 2-edge-connected by adding edges, the minimum number of edges needed is ceil(L / 2), where L is the number of leaves in the bridge-block tree.

## 3. Step-by-Step Algorithm
1. Run DFS with entry times and low-link values (Tarjan bridge-finding) to identify all bridges in G.
2. Contract 2-edge-connected components using disjoint set union or DFS coloring.
3. Build the condensed bridge-block tree where vertices are components and edges are the original bridges.
4. Count the degree of each vertex in the bridge-block tree; vertices with degree 1 are leaves.
5. Output ceil(L / 2) (or 0 if the tree has only 1 vertex).

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

const int INF = 1e9;

int N, M;
vector<pair<int, int>> orig_edges;
vector<vector<pair<int, int>>> adj; // to, edge_idx

vector<int> ord, low;
int timer = 0;
vector<bool> is_bridge;

void dfs_bridge(int u, int p_edge) {
    ord[u] = low[u] = ++timer;
    for (auto& edge : adj[u]) {
        int v = edge.first;
        int e_idx = edge.second;
        if (e_idx == p_edge) continue;
        if (ord[v]) {
            low[u] = min(low[u], ord[v]);
        } else {
            dfs_bridge(v, e_idx);
            low[u] = min(low[u], low[v]);
            if (low[v] > ord[u]) {
                is_bridge[e_idx] = true;
            }
        }
    }
}

vector<int> comp;
int comp_cnt = 0;
vector<int> comp_size;

void dfs_comp(int u, int c) {
    comp[u] = c;
    comp_size[c]++;
    for (auto& edge : adj[u]) {
        int v = edge.first;
        int e_idx = edge.second;
        if (is_bridge[e_idx] || comp[v] != -1) continue;
        dfs_comp(v, c);
    }
}

vector<vector<int>> tree;
int total_leaves = 0;
int min_added = INF;

// Returns pair: {number of leaves in subtree, total original vertices in subtree}
pair<int, int> dfs_tree(int u, int p) {
    int leaves = (tree[u].size() == 1 ? 1 : 0);
    int orig_nodes = comp_size[u];

    for (int v : tree[u]) {
        if (v == p) continue;
        auto res = dfs_tree(v, u);
        int l_sub = res.first;
        int n_sub = res.second;

        leaves += l_sub;
        orig_nodes += n_sub;

        // Consider the tree edge between u and v as the unique bridge!
        // Subtree v has n_sub original nodes.
        // The other side has N - n_sub original nodes.
        // If either side has exactly 2 original nodes, it cannot be made 2-edge-connected with simple edges!
        if (n_sub != 2 && (N - n_sub) != 2) {
            int l_v = l_sub + (tree[v].size() == 2 ? 1 : 0);
            int l_u = (total_leaves - l_sub) + (tree[u].size() == 2 ? 1 : 0);

            int cost_v = (l_v == 1 ? 0 : (l_v + 1) / 2);
            int cost_u = (l_u == 1 ? 0 : (l_u + 1) / 2);

            min_added = min(min_added, cost_v + cost_u);
        }
    }
    return {leaves, orig_nodes};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> N >> M)) return 0;
    adj.resize(N);
    orig_edges.resize(M);
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        orig_edges[i] = {u, v};
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }

    ord.assign(N, 0);
    low.assign(N, 0);
    is_bridge.assign(M, false);
    dfs_bridge(0, -1);

    comp.assign(N, -1);
    comp_size.clear();
    for (int i = 0; i < N; i++) {
        if (comp[i] == -1) {
            comp_size.push_back(0);
            dfs_comp(i, comp_cnt);
            comp_cnt++;
        }
    }

    if (comp_cnt == 1) {
        cout << "IMPOSSIBLE\n";
        return 0;
    }

    tree.resize(comp_cnt);
    for (int i = 0; i < M; i++) {
        if (is_bridge[i]) {
            int cu = comp[orig_edges[i].first];
            int cv = comp[orig_edges[i].second];
            tree[cu].push_back(cv);
            tree[cv].push_back(cu);
        }
    }

    total_leaves = 0;
    for (int i = 0; i < comp_cnt; i++) {
        if (tree[i].size() == 1) total_leaves++;
    }

    min_added = INF;
    dfs_tree(0, -1);

    if (min_added >= INF / 2) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << min_added << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
