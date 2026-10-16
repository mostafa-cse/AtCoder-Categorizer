# Problem Analysis: AtCoder-abc070_d — Transit Tree Path

**Problem ID**: `AtCoder-abc070_d`  
**Contest**: `abc070`  
**Rating / Difficulty**: 1182  
**URL**: https://atcoder.jp/contests/abc070/tasks/abc070_d  
**VJudge Tag**: `[problem:AtCoder-abc070_d]`  
**Category File**: [`../categories/graph_theory/fixed_transit_tree_distances.md`](../categories/graph_theory/fixed_transit_tree_distances.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Trees`  
- **Topic (Skill)**: `Fixed Transit Vertex Root-Referenced Tree Distances`  

---

## 1. Problem Statement & Key Idea
Given a weighted tree with N vertices. Q queries: find the shortest path distance between x and y that passes through a fixed transit vertex K.

**Key Idea**: The path must go from x to K, then from K to y. Since the graph is a tree, shortest path x -> K -> y has length dist(K, x) + dist(K, y).

## 2. Core Observation & Invariant
Reroot the tree at vertex K! Run a single BFS or DFS from K to precompute dist[v] = distance from K to v for all v in O(N). Each query (x, y) is answered in O(1) via dist[x] + dist[y].

## 3. Step-by-Step Algorithm
1. Root tree at transit vertex K.
2. Run DFS(K, 0, 0) to compute dist[v] for all vertices.
3. For each query (x, y): print dist[x] + dist[y].

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q)`
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Tree distance queries referenced through a fixed common transit node.
- **Reusable Pattern**: `Fixed transit tree query: dist_via_K(x, y) = dist[x] + dist[y] rooted at K.`
