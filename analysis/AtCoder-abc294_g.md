# Problem Analysis: AtCoder-abc294_g — Distance Queries on a Tree

**Problem ID**: `AtCoder-abc294_g`  
**Contest**: `abc294`  
**Rating / Difficulty**: 1702  
**URL**: https://atcoder.jp/contests/abc294/tasks/abc294_g  
**VJudge Tag**: `[problem:AtCoder-abc294_g]`  
**Category File**: [`../categories/data_structures/euler_tour_tree_distance_dynamic_weights.md`](../categories/data_structures/euler_tour_tree_distance_dynamic_weights.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Euler Tour + Fenwick Tree`  
- **Topic (Skill)**: `Dynamic Tree Distance via Euler Tour Subtree Add and LCA`  

---

## 1. Problem Statement & Key Idea
Given a tree of N vertices with weighted edges. Process Q queries: (1) change the weight of edge i to w, or (2) find the shortest distance between vertices u and v.

**Key Insight**: Flatten the tree with an Euler Tour. Root distance dist(u) is represented by prefix sums on the tour array. An edge (u, v) (where v is a child of u) with weight change Delta updates the depth of all nodes in v's subtree by Delta, corresponding to range update [tin[v], tout[v]] in a Fenwick Tree. Then dist(u, v) = dist(u) + dist(v) - 2 * dist(LCA(u, v)).

## 2. Core Observation & Invariant
Binary lifting answers LCA in O(log N). Subtree weight updates and point root-distance queries are handled in O(log N) using a difference Fenwick tree.

## 3. Step-by-Step Algorithm
1. Root tree at 1. Run DFS to compute tin, tout, depth, and binary lifting table up[k][u].
2. Orient edge i as from parent u to child v.
3. Build Fenwick tree over [1, 2N]. For edge into v with weight w, add +w at tin[v] and -w at tout[v] + 1.
4. Type 1 query: update edge i weight from old_w to w. Delta = w - old_w. Update Fenwick at tin[v] with +Delta and tout[v]+1 with -Delta.
5. Type 2 query: query dist(u) + dist(v) - 2 * dist(LCA(u, v)). dist(x) is Fenwick prefix sum at tin[x].

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N log N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int to, id;
    long long w;
};

int n, q;
vector<vector<Edge>> adj;
vector<int> edge_child;
vector<long long> edge_w;
vector<int> tin, tout, depth;
int timer = 0;
int up_table[20][200005];

struct Fenwick {
    int sz;
    vector<long long> tree;
    Fenwick(int n) : sz(n), tree(n + 2, 0) {}
    void add(int i, long long delta) {
        for (; i <= sz; i += i & -i) tree[i] += delta;
    }
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

void dfs(int u, int p, int d) {
    tin[u] = ++timer;
    depth[u] = d;
    up_table[0][u] = p;
    for (int k = 1; k < 20; ++k) {
        up_table[k][u] = up_table[k - 1][up_table[k - 1][u]];
    }
    for (auto& e : adj[u]) {
        if (e.to != p) {
            edge_child[e.id] = e.to;
            dfs(e.to, u, d + 1);
        }
    }
    tout[u] = timer;
}

int get_lca(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    for (int k = 19; k >= 0; --k) {
        if (depth[u] - (1 << k) >= depth[v]) {
            u = up_table[k][u];
        }
    }
    if (u == v) return u;
    for (int k = 19; k >= 0; --k) {
        if (up_table[k][u] != up_table[k][v]) {
            u = up_table[k][u];
            v = up_table[k][v];
        }
    }
    return up_table[0][u];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;
    adj.assign(n + 1, vector<Edge>());
    edge_child.assign(n, 0);
    edge_w.assign(n, 0);
    tin.assign(n + 1, 0);
    tout.assign(n + 1, 0);
    depth.assign(n + 1, 0);

    for (int i = 1; i < n; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, i, w});
        adj[v].push_back({u, i, w});
        edge_w[i] = w;
    }

    dfs(1, 1, 0);

    Fenwick ft(2 * n + 5);
    for (int i = 1; i < n; ++i) {
        int ch = edge_child[i];
        ft.add(tin[ch], edge_w[i]);
        ft.add(tout[ch] + 1, -edge_w[i]);
    }

    cin >> q;
    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int e_id;
            long long new_w;
            cin >> e_id >> new_w;
            int ch = edge_child[e_id];
            long long delta = new_w - edge_w[e_id];
            edge_w[e_id] = new_w;
            ft.add(tin[ch], delta);
            ft.add(tout[ch] + 1, -delta);
        } else {
            int u, v;
            cin >> u >> v;
            int lca = get_lca(u, v);
            long long ans = ft.query(tin[u]) + ft.query(tin[v]) - 2 * ft.query(tin[lca]);
            cout << ans << "\n";
        }
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining Euler Tour subtree interval mapping with Fenwick range updates and LCA for dynamic edge weights.
- **Reusable Pattern**: `Euler Tour Subtree Add + LCA Point Distance: Fenwick range add + LCA depth subtraction.`
