# Problem Analysis: AtCoder-abc477_g — Frequency Query on Tree

**Problem ID**: `AtCoder-abc477_g`  
**Contest**: `abc477`  
**Rating / Difficulty**: 2226  
**URL**: https://atcoder.jp/contests/abc477/tasks/abc477_g  
**VJudge Tag**: `[problem:AtCoder-abc477_g]`  
**Category File**: [`../categories/data_structures/mos_algorithm_on_tree_frequency_path_queries.md`](../categories/data_structures/mos_algorithm_on_tree_frequency_path_queries.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Square Root Decomposition`  
- **Topic (Skill)**: `Mo's on Tree`  

---

## 1. Problem Statement & Key Idea
Given a tree with vertex values, answer Q path queries (s, t, a, b) asking for the number of distinct values y whose frequency on the path satisfies a <= freq(y) <= b.

## 2. Core Observation & Invariant
Flatten the tree via Euler tour of length 2N recording enter and exit times. Path between s and t translates to interval [tout[s], tin[t]] (plus LCA if lca != s) where vertices occurring odd times lie on the path. Mo's algorithm maintains frequency of each color: when color count updates, maintaining g[k] = count of colors with frequency >= k allows O(1) frequency transitions and O(1) range queries via g[a] - g[b+1].

## 3. Step-by-Step Algorithm
1. 1. Perform DFS to record Euler tour of entering and exiting times, depths, and binary lifting table for LCA.
2. 2. Convert each query (s, t) into segment [tin[s], tin[t]] if s is ancestor of t, or [tout[s], tin[t]] with lca(s, t) otherwise.
3. 3. Sort queries using Hilbert curve or block order with alternating right boundary.
4. 4. Maintain active vertex states, color frequencies freq[c], and aggregate threshold counts g[k].
5. 5. Add/remove vertex in O(1): toggle presence, update freq[c] and g[freq[c]].
6. 6. For each query, temporarily toggle LCA if necessary, evaluate answer as g[a] - g[b+1], and toggle LCA back.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) * sqrt(N))`
- **Space Complexity**: `O(N + Q)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Query {
    int id;
    int l, r;
    int lca;
    int a, b;
    int block;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<int> x(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> x[i];
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Binary lifting for LCA and Euler tour
    int LOGN = 20;
    vector<vector<int>> up(LOGN, vector<int>(n + 1, 0));
    vector<int> depth(n + 1, 0);
    vector<int> euler;
    euler.reserve(2 * n + 2);
    vector<int> tin(n + 1), tout(n + 1);

    auto dfs = [&](auto& self, int u, int p, int d) -> void {
        depth[u] = d;
        up[0][u] = p;
        for (int k = 1; k < LOGN; ++k) {
            up[k][u] = up[k - 1][up[k - 1][u]];
        }
        tin[u] = euler.size();
        euler.push_back(u);

        for (int v : adj[u]) {
            if (v != p) {
                self(self, v, u, d + 1);
            }
        }

        tout[u] = euler.size();
        euler.push_back(u);
    };

    dfs(dfs, 1, 1, 0);

    auto get_lca = [&](int u, int v) -> int {
        if (depth[u] < depth[v]) swap(u, v);
        for (int k = LOGN - 1; k >= 0; --k) {
            if (depth[u] - (1 << k) >= depth[v]) {
                u = up[k][u];
            }
        }
        if (u == v) return u;
        for (int k = LOGN - 1; k >= 0; --k) {
            if (up[k][u] != up[k][v]) {
                u = up[k][u];
                v = up[k][v];
            }
        }
        return up[0][u];
    };

    int m = euler.size();
    int block_size = max(1, (int)(m / sqrt(max(1, q))));

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        int s, t, a, b;
        cin >> s >> t >> a >> b;
        if (tin[s] > tin[t]) swap(s, t);
        int lca = get_lca(s, t);
        queries[i].id = i;
        queries[i].a = a;
        queries[i].b = b;

        if (lca == s) {
            queries[i].l = tin[s];
            queries[i].r = tin[t];
            queries[i].lca = 0;
        } else {
            queries[i].l = tout[s];
            queries[i].r = tin[t];
            queries[i].lca = lca;
        }
        queries[i].block = queries[i].l / block_size;
    }

    sort(queries.begin(), queries.end(), [](const Query& A, const Query& B) {
        if (A.block != B.block) return A.block < B.block;
        return (A.block & 1) ? A.r < B.r : A.r > B.r;
    });

    vector<int> freq(n + 1, 0);
    vector<int> g(n + 2, 0);
    vector<bool> vis(n + 1, false);

    auto toggle = [&](int u) {
        int c = x[u];
        if (!vis[u]) {
            vis[u] = true;
            freq[c]++;
            g[freq[c]]++;
        } else {
            vis[u] = false;
            g[freq[c]]--;
            freq[c]--;
        }
    };

    int cur_l = 0, cur_r = -1;
    vector<int> ans(q);

    for (const auto& qy : queries) {
        while (cur_r < qy.r) {
            cur_r++;
            toggle(euler[cur_r]);
        }
        while (cur_l > qy.l) {
            cur_l--;
            toggle(euler[cur_l]);
        }
        while (cur_r > qy.r) {
            toggle(euler[cur_r]);
            cur_r--;
        }
        while (cur_l < qy.l) {
            toggle(euler[cur_l]);
            cur_l++;
        }

        if (qy.lca != 0) {
            toggle(qy.lca);
        }

        int cnt_a = (qy.a <= n) ? g[qy.a] : 0;
        int cnt_b1 = (qy.b + 1 <= n) ? g[qy.b + 1] : 0;
        ans[qy.id] = cnt_a - cnt_b1;

        if (qy.lca != 0) {
            toggle(qy.lca);
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
