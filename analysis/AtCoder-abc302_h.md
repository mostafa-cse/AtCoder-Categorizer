# Problem Analysis: AtCoder-abc302_h — Ex. Ball Collector

**Problem ID**: `AtCoder-abc302_h`  
**Contest**: `abc302`  
**Rating / Difficulty**: 2407  
**URL**: https://atcoder.jp/contests/abc302/tasks/abc302_h  
**VJudge Tag**: `[problem:AtCoder-abc302_h]`  
**Category File**: [`../categories/data_structures/dsu_with_rollbacks_tree_dfs_bipartite_functional_graph.md`](../categories/data_structures/dsu_with_rollbacks_tree_dfs_bipartite_functional_graph.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `DSU with Rollbacks`  

---

## 1. Problem Statement & Key Idea
Along each tree path from 1 to v, select one of two balls (A_u, B_u) at each node to maximize distinct values. Model ball pairs as edges in a functional component graph and maintain the maximum matching across DFS paths using DSU with Rollbacks.

## 2. Core Observation & Invariant
In any connected component of the value graph with V vertices and E edges, the maximum number of distinct vertices that can be covered by orienting edges is min(V, E). A tree component yields E = V-1, while any component containing a cycle yields all V vertices.

## 3. Step-by-Step Algorithm
1. 1. Run DFS starting from root vertex 1 on the tree.
2. 2. When entering node u, add edge (A_u, B_u) into an Undoable Disjoint Set Union (union by rank/size, recording history).
3. 3. Maintain total answer dynamically as sum of min(size, edge_count) across all components.
4. 4. Record answer at node u, recurse to children, and roll back the edge addition upon return.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct UndoUnionFind {
    int n;
    vector<int> parent, sz, edges;
    struct History {
        int u, v;
        bool merged;
        int old_val;
    };
    vector<History> hist;
    int total_ans;

    UndoUnionFind(int n) : n(n), parent(n + 1), sz(n + 1, 1), edges(n + 1, 0), total_ans(0) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int i) {
        while (i != parent[i]) i = parent[i];
        return i;
    }

    void add_edge(int u, int v) {
        int ru = find(u), rv = find(v);
        if (ru == rv) {
            int old_val = min(sz[ru], edges[ru]);
            hist.push_back({ru, rv, false, old_val});
            edges[ru]++;
            int new_val = min(sz[ru], edges[ru]);
            total_ans += (new_val - old_val);
        } else {
            if (sz[ru] < sz[rv]) swap(ru, rv);
            int old_val = min(sz[ru], edges[ru]) + min(sz[rv], edges[rv]);
            hist.push_back({ru, rv, true, old_val});
            parent[rv] = ru;
            sz[ru] += sz[rv];
            edges[ru] += edges[rv] + 1;
            int new_val = min(sz[ru], edges[ru]);
            total_ans += (new_val - old_val);
        }
    }

    void rollback() {
        History h = hist.back();
        hist.pop_back();
        int cur_val = min(sz[h.u], edges[h.u]);
        total_ans -= (cur_val - h.old_val);
        if (h.merged) {
            edges[h.u] -= (edges[h.v] + 1);
            sz[h.u] -= sz[h.v];
            parent[h.v] = h.v;
        } else {
            edges[h.u]--;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<int, int>> balls(n + 1);
    for (int i = 1; i <= n; i++) cin >> balls[i].first >> balls[i].second;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    UndoUnionFind dsu(n);
    vector<int> ans(n + 1, 0);

    auto dfs = [&](auto& self, int u, int p) -> void {
        dsu.add_edge(balls[u].first, balls[u].second);
        ans[u] = dsu.total_ans;
        for (int v : adj[u]) {
            if (v != p) self(self, v, u);
        }
        dsu.rollback();
    };

    dfs(dfs, 1, 0);

    for (int i = 2; i <= n; i++) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
