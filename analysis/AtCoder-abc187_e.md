# Problem Analysis: AtCoder-abc187_e — Through Path

**Problem ID**: `AtCoder-abc187_e`  
**Contest**: `abc187`  
**Rating / Difficulty**: 1358  
**URL**: https://atcoder.jp/contests/abc187/tasks/abc187_e  
**VJudge Tag**: `[problem:AtCoder-abc187_e]`  
**Category File**: [`../categories/data_structures/tree_edge_cut_orienting_imos.md`](../categories/data_structures/tree_edge_cut_orienting_imos.md)  

- **Tag (Domain)**: `Data Structures`  
- **Subtopic**: `Tree Difference Arrays`  
- **Topic (Skill)**: `Tree Edge Cut Orienting with Subtree Difference Array DFS`  

---

## 1. Problem Statement & Key Idea
Given a tree with N vertices. Q queries: (t, e, x) where edge e connects a and b. If t=1, add x to all vertices reachable from a without crossing edge e. If t=2, add x to all vertices reachable from b without crossing edge e. Find final values.

**Key Idea**: Removing edge e splits the tree into two components: one is a subtree, the other is the rest of the tree (complement).

## 2. Core Observation & Invariant
Root the tree at vertex 1 and compute depth[v]. Between endpoints a and b of edge e, let deeper endpoint be child, other be parent. (1) If we want to add x to child's component: add +x to child's subtree! (2) If we want to add x to parent's component: add +x to ALL vertices (global val[1] += x) and subtract -x from child's subtree (val[child] -= x). Propagate in a single DFS!

## 3. Step-by-Step Algorithm
1. Root tree at 1, compute depth[u] via DFS.
2. For each query (t, e, x): identify from_u and to_v based on t.
3. If depth[from_u] > depth[to_v]: from_u is child -> val[from_u] += x.
4. Else: to_v is child -> val[1] += x, val[to_v] -= x.
5. Run single DFS to push prefix sums down from root to leaves.
6. Print val[1..N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int u, v;
};

void get_depth(int u, int p, int d, const vector<vector<int>>& adj, vector<int>& depth) {
    depth[u] = d;
    for (int v : adj[u]) {
        if (v != p) {
            get_depth(v, u, d + 1, adj, depth);
        }
    }
}

void dfs_propagate(int u, int p, const vector<vector<int>>& adj, vector<long long>& val) {
    for (int v : adj[u]) {
        if (v != p) {
            val[v] += val[u];
            dfs_propagate(v, u, adj, val);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<Edge> edges(n);
    for (int i = 1; i <= n - 1; ++i) {
        cin >> edges[i].u >> edges[i].v;
        adj[edges[i].u].push_back(edges[i].v);
        adj[edges[i].v].push_back(edges[i].u);
    }

    vector<int> depth(n + 1, 0);
    get_depth(1, 0, 1, adj, depth);

    vector<long long> val(n + 1, 0);
    int q;
    cin >> q;

    while (q--) {
        int t, e;
        long long x;
        cin >> t >> e >> x;

        int u = edges[e].u;
        int v = edges[e].v;
        int from_node = (t == 1 ? u : v);
        int other_node = (t == 1 ? v : u);

        if (depth[from_node] > depth[other_node]) {
            val[from_node] += x;
        } else {
            val[1] += x;
            val[other_node] -= x;
        }
    }

    dfs_propagate(1, 0, adj, val);

    for (int i = 1; i <= n; ++i) {
        cout << val[i] << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Subtree vs tree-complement updates via tree imos and depth orientation.
- **Reusable Pattern**: `Complement update on tree: add globally to root, subtract from child subtree.`
