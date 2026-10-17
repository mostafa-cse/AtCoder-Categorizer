# Problem Analysis: AtCoder-abc133_f — F. Colorful Tree

**Problem ID**: `AtCoder-abc133_f`  
**Contest**: `abc133`  
**Rating / Difficulty**: 2330  
**URL**: https://atcoder.jp/contests/abc133/tasks/abc133_f  
**VJudge Tag**: `[problem:AtCoder-abc133_f]`  
**Category File**: [`../categories/graph_theory/tree_colored_edge_dynamic_length_offline_lca.md`](../categories/graph_theory/tree_colored_edge_dynamic_length_offline_lca.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Lowest Common Ancestor (LCA)`  
- **Topic (Skill)**: `Binary Lifting and LCA`  

---

## 1. Problem Statement & Key Idea
Given a tree with colored weighted edges, answer $Q$ queries: if all edges of color $x$ have their weights replaced with $y$, what is the distance between vertices $u$ and $v$?

## 2. Core Observation & Invariant
The distance between $u$ and $v$ when edges of color $x$ are set to length $y$ is $\text{dist}(u, v) - \text{sum}(u, v, x) + \text{cnt}(u, v, x) \cdot y$, where $\text{cnt}(u, v, x)$ and $\text{sum}(u, v, x)$ decompose along the tree path via $u + v - 2 \cdot \text{lca}(u, v)$.

## 3. Step-by-Step Algorithm
1. Precompute LCA and depth using binary lifting in $O(N \log N)$ time.
2. Attach query color requests to nodes $u, v$ with weight $+1$ and to $\text{lca}(u, v)$ with weight $-2$.
3. Perform a single DFS from the root, maintaining running frequencies and weight sums for each color on the active path, evaluating all $Q$ queries offline in $O(N + Q)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) \log N)`
- **Space Complexity**: `O(N + Q)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Edge {
    int to, col;
    long long cost;
};

struct Query {
    int q_idx;
    int col;
    int sign;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<vector<Edge>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v, c;
        long long d;
        cin >> u >> v >> c >> d;
        adj[u].push_back({v, c, d});
        adj[v].push_back({u, c, d});
    }

    const int LOGN = 18;
    vector<vector<int>> up(LOGN, vector<int>(n + 1, 0));
    vector<int> depth(n + 1, 0);
    vector<long long> dist(n + 1, 0);

    vector<bool> vis(n + 1, false);
    queue<int> que;
    que.push(1);
    vis[1] = true;

    while (!que.empty()) {
        int u = que.front();
        que.pop();
        for (const auto& e : adj[u]) {
            int v = e.to;
            if (!vis[v]) {
                vis[v] = true;
                up[0][v] = u;
                depth[v] = depth[u] + 1;
                dist[v] = dist[u] + e.cost;
                que.push(v);
            }
        }
    }

    for (int j = 1; j < LOGN; ++j) {
        for (int i = 1; i <= n; ++i) {
            up[j][i] = up[j - 1][up[j - 1][i]];
        }
    }

    auto get_lca = [&](int u, int v) -> int {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int j = 0; j < LOGN; ++j) {
            if ((diff >> j) & 1) u = up[j][u];
        }
        if (u == v) return u;
        for (int j = LOGN - 1; j >= 0; --j) {
            if (up[j][u] != up[j][v]) {
                u = up[j][u];
                v = up[j][v];
            }
        }
        return up[0][u];
    };

    vector<vector<Query>> node_queries(n + 1);
    vector<long long> q_new_len(q);
    vector<long long> q_base_dist(q);

    for (int i = 0; i < q; ++i) {
        int x, u, v;
        long long y;
        cin >> x >> y >> u >> v;
        int lca = get_lca(u, v);
        q_new_len[i] = y;
        q_base_dist[i] = dist[u] + dist[v] - 2 * dist[lca];
        node_queries[u].push_back({i, x, 1});
        node_queries[v].push_back({i, x, 1});
        node_queries[lca].push_back({i, x, -2});
    }

    vector<int> col_cnt(n, 0);
    vector<long long> col_sum(n, 0);
    vector<int> ans_cnt(q, 0);
    vector<long long> ans_sum(q, 0);

    function<void(int, int)> dfs = [&](int u, int p) {
        for (const auto& qry : node_queries[u]) {
            ans_cnt[qry.q_idx] += qry.sign * col_cnt[qry.col];
            ans_sum[qry.q_idx] += qry.sign * col_sum[qry.col];
        }
        for (const auto& e : adj[u]) {
            int v = e.to;
            if (v != p) {
                col_cnt[e.col]++;
                col_sum[e.col] += e.cost;
                dfs(v, u);
                col_cnt[e.col]--;
                col_sum[e.col] -= e.cost;
            }
        }
    };

    dfs(1, 0);

    for (int i = 0; i < q; ++i) {
        long long cur_ans = q_base_dist[i] - ans_sum[i] + 1LL * ans_cnt[i] * q_new_len[i];
        cout << cur_ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
