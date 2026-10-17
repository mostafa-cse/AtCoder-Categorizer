# Problem Analysis: AtCoder-nikkei2019_qual_e — E. Avoid Deletion

**Problem ID**: `AtCoder-nikkei2019_qual_e`  
**Contest**: `nikkei2019_qual`  
**Rating / Difficulty**: 2294  
**URL**: https://atcoder.jp/contests/nikkei2019_qual/tasks/nikkei2019_qual_e  
**VJudge Tag**: `[problem:AtCoder-nikkei2019_qual_e]`  
**Category File**: [`../categories/data_structures/kruskal_reconstruction_tree_weight_threshold.md`](../categories/data_structures/kruskal_reconstruction_tree_weight_threshold.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Reachability Tree / DSU Tree / Kruskal Reconstruction Tree (KRT)`  

---

## 1. Problem Statement & Key Idea
Given a weighted graph with vertex weights $X_v$ and edge weights $Y_e$, find the minimum number of edges to delete such that every remaining edge belongs to a connected component whose total vertex weight is at least its edge weight.

## 2. Core Observation & Invariant
In the Kruskal Reconstruction Tree ordered by edge weight $Y_e$, a subtree $u$ represents a connected component formed by all edges of weight $\le \mathrm{val}[u]$. The component is valid if total vertex weight $W(u) \ge \mathrm{val}[u]$. If valid, all edges inside subtree $u$ are preserved without deletion.

## 3. Step-by-Step Algorithm
1. 1. An edge $e = (u, v)$ with weight $Y$ can be kept if it belongs to a connected component $C$ whose total vertex weight $W(C) = \sum_{x \in C} X_x \ge Y$.
2. 2. Sort all edges in ascending order of $Y_e$. Construct the Kruskal Reconstruction Tree (KRT):
3.    - When edge $e$ connects two components $r_1, r_2$, create a new node with value $Y_e$, make $r_1, r_2$ its children, and set its weight $W = W(r_1) + W(r_2)$.
4.    - If edge $e$ is a non-tree edge connecting nodes already in the same component, create a new parent node over the component with value $Y_e$ and the same weight $W$.
5. 3. A KRT node $u$ is valid if $W(u) \ge \mathrm{val}[u]$. If a node is valid, all non-tree and tree edges within its subtree satisfy the condition and need not be deleted.
6. 4. Propagate validity downwards: if any ancestor of $v$ is valid, all edges in $v$'s subtree are saved.
7. 5. Count all edges in subtrees that have no valid ancestor; these must be deleted. Total complexity is $O(M \log M)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(M \log M + (N + M) \alpha(N))`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v;
    long long w;
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int ri = find(i), rj = find(j);
        if (ri != rj) parent[ri] = rj;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> X(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> X[i];
    }

    vector<Edge> edges(M);
    for (int i = 0; i < M; ++i) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.w < b.w;
    });

    int total_nodes = N;
    // Max nodes in KRT is N + M
    vector<long long> weight_sum(N + M + 5, 0);
    vector<long long> edge_val(N + M + 5, 0);
    vector<vector<int>> children(N + M + 5);
    vector<bool> is_edge_node(N + M + 5, false);

    for (int i = 1; i <= N; ++i) {
        weight_sum[i] = X[i];
    }

    DSU dsu(N + M + 5);

    for (int i = 0; i < M; ++i) {
        int ru = dsu.find(edges[i].u);
        int rv = dsu.find(edges[i].v);
        total_nodes++;
        int new_node = total_nodes;
        edge_val[new_node] = edges[i].w;
        is_edge_node[new_node] = true;

        if (ru != rv) {
            dsu.parent[ru] = new_node;
            dsu.parent[rv] = new_node;
            children[new_node].push_back(ru);
            children[new_node].push_back(rv);
            weight_sum[new_node] = weight_sum[ru] + weight_sum[rv];
        } else {
            dsu.parent[ru] = new_node;
            children[new_node].push_back(ru);
            weight_sum[new_node] = weight_sum[ru];
        }
    }

    int root = total_nodes;
    int deleted_edges = 0;

    auto dfs = [&](auto& self, int u, bool valid_ancestor) -> void {
        bool current_valid = valid_ancestor || (is_edge_node[u] && weight_sum[u] >= edge_val[u]);
        if (is_edge_node[u] && !current_valid) {
            deleted_edges++;
        }
        for (int v : children[u]) {
            self(self, v, current_valid);
        }
    };

    dfs(dfs, root, false);

    cout << deleted_edges << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
