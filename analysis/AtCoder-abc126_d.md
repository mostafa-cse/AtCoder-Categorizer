# Problem Analysis: AtCoder-abc126_d — Even Relation

**Problem ID**: `AtCoder-abc126_d`  
**Contest**: `abc126`  
**Rating / Difficulty**: 1279  
**URL**: https://atcoder.jp/contests/abc126/tasks/abc126_d  
**VJudge Tag**: `[problem:AtCoder-abc126_d]`  
**Category File**: [`../categories/graph_theory/tree_2coloring_edge_parities.md`](../categories/graph_theory/tree_2coloring_edge_parities.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Tree Coloring`  
- **Topic (Skill)**: `Tree 2-Coloring via Edge Weight Parities`  

---

## 1. Problem Statement & Key Idea
Given a weighted tree with N vertices. Color vertices with 0 or 1 such that any two vertices with the same color have an EVEN shortest path distance.

**Key Idea**: The distance dist(u, v) on a tree can be written as (dist(root, u) + dist(root, v) - 2 * dist(root, LCA(u, v))).

## 2. Core Observation & Invariant
Notice that 2 * dist(root, LCA) is always even! Thus, dist(u, v) = dist(root, u) + dist(root, v) (mod 2). For dist(u, v) to be even, dist(root, u) and dist(root, v) must have the EXACT SAME parity! Therefore, we simply color each vertex based on the parity of its distance from root 1: color[u] = dist(1, u) % 2.

## 3. Step-by-Step Algorithm
1. Root tree at vertex 1.
2. Run DFS/BFS: compute dist[u] from root 1.
3. Set color[u] = dist[u] % 2.
4. Print color[u] for each u from 1 to N.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int to;
    long long w;
};

void dfs(int u, int p, long long d, const vector<vector<Edge>>& adj, vector<int>& color) {
    color[u] = d % 2;
    for (const auto& e : adj[u]) {
        if (e.to != p) {
            dfs(e.to, u, d + e.w, adj, color);
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
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<int> color(n + 1, 0);
    dfs(1, 0, 0, adj, color);

    for (int i = 1; i <= n; ++i) {
        cout << color[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bipartite coloring of trees based on distance parity invariant.
- **Reusable Pattern**: `Even distance condition on trees: color[v] = dist_from_root[v] % 2.`
