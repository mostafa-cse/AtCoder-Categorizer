# Problem Analysis: AtCoder-abc340_g — G. Leaf Color

**Problem ID**: `AtCoder-abc340_g`  
**Contest**: `abc340`  
**Rating / Difficulty**: 2401  
**URL**: https://atcoder.jp/contests/abc340/tasks/abc340_g  
**VJudge Tag**: `[problem:AtCoder-abc340_g]`  
**Category File**: [`../categories/graph_theory/virtual_tree_auxiliary_tree_leaf_color.md`](../categories/graph_theory/virtual_tree_auxiliary_tree_leaf_color.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `More Tree Stuff`  
- **Topic (Skill)**: `Virtual Tree / Auxiliary Tree`  

---

## 1. Problem Statement & Key Idea
Count connected induced subgraphs whose leaves all share a given color c. For each color c with k_c occurrences, build an Auxiliary / Virtual Tree in O(k_c log N) and run DP on the compressed tree.

## 2. Core Observation & Invariant
A valid subgraph with all leaves of color c is an induced subtree on the virtual tree whose extremal nodes are all colored c. Compressing the tree via LCA and DFS entry time reduces the total nodes evaluated across all colors to sum(2 k_c) = O(N).

## 3. Step-by-Step Algorithm
1. 1. Precompute LCA via binary lifting and tin/tout DFS entry/exit times.
2. 2. For each color c, sort the vertices by tin and construct the virtual tree using a monotonic stack.
3. 3. Run Tree DP on the auxiliary tree: dp[u] is the number of valid subtrees in u's subtree containing u. If u has color c, u can be a leaf; otherwise u cannot be an isolated leaf.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N log N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n + 1);
    vector<vector<int>> color_nodes(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
        color_nodes[a[i]].push_back(i);
    }

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    const int LOGN = 19;
    vector<vector<int>> up(LOGN, vector<int>(n + 1, 0));
    vector<int> tin(n + 1), tout(n + 1), depth(n + 1);
    int timer = 0;

    auto dfs_init = [&](auto& self, int u, int p, int d) -> void {
        up[0][u] = p;
        for (int i = 1; i < LOGN; i++) {
            up[i][u] = up[i - 1][up[i - 1][u]];
        }
        tin[u] = ++timer;
        depth[u] = d;
        for (int v : adj[u]) {
            if (v != p) self(self, v, u, d + 1);
        }
        tout[u] = timer;
    };
    dfs_init(dfs_init, 1, 1, 0);

    auto is_ancestor = [&](int u, int v) -> bool {
        return tin[u] <= tin[v] && tout[u] >= tout[v];
    };

    auto get_lca = [&](int u, int v) -> int {
        if (is_ancestor(u, v)) return u;
        if (is_ancestor(v, u)) return v;
        for (int i = LOGN - 1; i >= 0; i--) {
            if (!is_ancestor(up[i][u], v)) {
                u = up[i][u];
            }
        }
        return up[0][u];
    };

    vector<vector<int>> v_adj(n + 1);
    vector<bool> is_key(n + 1, false);
    vector<ll> dp(n + 1, 0);
    ll total_ans = 0;

    auto dfs_dp = [&](auto& self, int u) -> void {
        ll ways = 1;
        ll sum_dp = 0;
        for (int v : v_adj[u]) {
            self(self, v);
            ways = (ways * (dp[v] + 1)) % MOD;
            sum_dp = (sum_dp + dp[v]) % MOD;
        }
        if (is_key[u]) {
            dp[u] = ways;
            total_ans = (total_ans + ways) % MOD;
        } else {
            dp[u] = (ways - 1 + MOD) % MOD;
            total_ans = (total_ans + (ways - 1 - sum_dp + 2 * MOD)) % MOD;
        }
    };

    for (int c = 1; c <= n; c++) {
        if (color_nodes[c].empty()) continue;
        auto& nodes = color_nodes[c];
        sort(nodes.begin(), nodes.end(), [&](int u, int v) {
            return tin[u] < tin[v];
        });

        vector<int> vtree_nodes;
        vtree_nodes.reserve(nodes.size() * 2);
        for (int u : nodes) {
            vtree_nodes.push_back(u);
            is_key[u] = true;
        }
        int k = nodes.size();
        for (int i = 0; i < k - 1; i++) {
            vtree_nodes.push_back(get_lca(nodes[i], nodes[i + 1]));
        }

        sort(vtree_nodes.begin(), vtree_nodes.end(), [&](int u, int v) {
            return tin[u] < tin[v];
        });
        vtree_nodes.erase(unique(vtree_nodes.begin(), vtree_nodes.end()), vtree_nodes.end());

        vector<int> st;
        st.push_back(vtree_nodes[0]);
        for (size_t i = 1; i < vtree_nodes.size(); i++) {
            int u = vtree_nodes[i];
            while (!st.empty() && !is_ancestor(st.back(), u)) {
                st.pop_back();
            }
            v_adj[st.back()].push_back(u);
            st.push_back(u);
        }

        int root = vtree_nodes[0];
        dfs_dp(dfs_dp, root);

        // Cleanup
        for (int u : vtree_nodes) {
            v_adj[u].clear();
            is_key[u] = false;
            dp[u] = 0;
        }
    }

    cout << total_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
