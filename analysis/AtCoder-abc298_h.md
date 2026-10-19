# Problem Analysis: AtCoder-abc298_h — Ex - Sum of Min of Length

**Problem ID**: `AtCoder-abc298_h`  
**Contest**: `abc298`  
**Rating / Difficulty**: 2792  
**URL**: https://atcoder.jp/contests/abc298/tasks/abc298_h  
**VJudge Tag**: `[problem:AtCoder-abc298_h]`  
**Category File**: [`../categories/graph_theory/tree_distance_queries_midpoint_binary_lifting.md`](../categories/graph_theory/tree_distance_queries_midpoint_binary_lifting.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Lowest Common Ancestor (LCA)`  
- **Topic (Skill)**: `Binary Lifting and LCA`  

---

## 1. Problem Statement & Key Idea
Given a tree of N vertices, answer Q queries: given two vertices u and v, compute sum_{w=1}^N min(dist(u, w), dist(v, w)).

## 2. Core Observation & Invariant
The condition dist(u, w) <= dist(v, w) partitions the tree into two connected components along the midpoint of the path between u and v. Using binary lifting and LCA, we can find the midpoint on the u-v path in O(log N) time. The tree is thus split into two subtrees: u's side and v's side. With tree rerooting DP, we can precompute sum of distances from every vertex to all other vertices. For each query, the sum of distances restricted to each side can be computed in O(log N) using precomputed subtree aggregates.

## 3. Step-by-Step Algorithm
1. 1. Precompute LCA, depths, subtree sizes, and subtree distance sums via DFS.
2. 2. Precompute all-pairs distance sums using tree rerooting DP.
3. 3. For each query (u, v):
4.    a. Compute distance dist(u, v) and LCA(u, v).
5.    b. Find the path midpoint at distance floor((dist(u, v) - 1) / 2) from u using binary lifting.
6.    c. Split the tree into u's component and v's component.
7.    d. Sum distances from u to u's side and from v to v's side in O(1) using precalculated aggregates.
8. 4. Output the result for each query.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q log N)`
- **Space Complexity**: `O(N log N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> depth(N + 1, 0);
    vector<long long> sz(N + 1, 0);
    vector<long long> sub_dist(N + 1, 0);
    vector<vector<int>> up(N + 1, vector<int>(20, 0));

    // DFS from 1
    vector<int> order;
    order.reserve(N);
    vector<pair<int, int>> stack = {{1, 0}};
    depth[1] = 0;

    while (!stack.empty()) {
        auto [u, p] = stack.back();
        stack.pop_back();
        up[u][0] = p;
        order.push_back(u);
        for (int v : adj[u]) {
            if (v != p) {
                depth[v] = depth[u] + 1;
                stack.push_back({v, u});
            }
        }
    }

    for (int k = 1; k < 20; ++k) {
        for (int i = 1; i <= N; ++i) {
            up[i][k] = up[up[i][k - 1]][k - 1];
        }
    }

    for (int i = N - 1; i >= 0; --i) {
        int u = order[i];
        sz[u] = 1;
        sub_dist[u] = 0;
        for (int v : adj[u]) {
            if (v != up[u][0]) {
                sz[u] += sz[v];
                sub_dist[u] += sub_dist[v] + sz[v];
            }
        }
    }

    // Rerooting to compute S[u] for all u
    vector<long long> S(N + 1, 0);
    S[1] = sub_dist[1];
    for (int u : order) {
        for (int v : adj[u]) {
            if (v != up[u][0]) {
                S[v] = S[u] - sz[v] + (N - sz[v]);
            }
        }
    }

    auto get_lca = [&](int u, int v) -> int {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int k = 0; k < 20; ++k) {
            if ((diff >> k) & 1) u = up[u][k];
        }
        if (u == v) return u;
        for (int k = 19; k >= 0; --k) {
            if (up[u][k] != up[v][k]) {
                u = up[u][k];
                v = up[v][k];
            }
        }
        return up[u][0];
    };

    auto get_dist = [&](int u, int v) -> int {
        return depth[u] + depth[v] - 2 * depth[get_lca(u, v)];
    };

    auto jump_k = [&](int u, int k) -> int {
        for (int i = 0; i < 20; ++i) {
            if ((k >> i) & 1) u = up[u][i];
        }
        return u;
    };

    auto jump_on_path = [&](int u, int v, int step) -> int {
        int lca = get_lca(u, v);
        int d1 = depth[u] - depth[lca];
        if (step <= d1) {
            return jump_k(u, step);
        }
        int d2 = depth[v] - depth[lca];
        int step2 = d1 + d2 - step;
        return jump_k(v, step2);
    };

    int Q;
    if (!(cin >> Q)) return 0;

    while (Q--) {
        int L, R;
        cin >> L >> R;
        if (L == R) {
            cout << S[L] << "\n";
            continue;
        }

        int D = get_dist(L, R);
        int mid = D / 2;
        int u = jump_on_path(L, R, mid);
        int v = jump_on_path(L, R, mid + 1);

        if (up[v][0] == u) {
            // v is child of u. V_v is subtree of v (contains R)
            long long sum_L_Vv = sz[v] * get_dist(L, v) + sub_dist[v];
            long long sum_L_Vu = S[L] - sum_L_Vv;

            long long sum_R_Vu = (N - sz[v]) * get_dist(R, u) + (S[u] - sub_dist[v] - sz[v]);
            long long sum_R_Vv = S[R] - sum_R_Vu;

            cout << sum_L_Vu + sum_R_Vv << "\n";
        } else {
            // u is child of v. V_u is subtree of u (contains L)
            long long sum_R_Vu = sz[u] * get_dist(R, u) + sub_dist[u];
            long long sum_R_Vv = S[R] - sum_R_Vu;

            long long sum_L_Vv = (N - sz[u]) * get_dist(L, v) + (S[v] - sub_dist[u] - sz[u]);
            long long sum_L_Vu = S[L] - sum_L_Vv;

            cout << sum_L_Vu + sum_R_Vv << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
