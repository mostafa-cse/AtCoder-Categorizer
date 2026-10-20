# Problem Analysis: AtCoder-arc142_d — D. Deterministic Placing

**Problem ID**: `AtCoder-arc142_d`  
**Contest**: `arc142`  
**Rating / Difficulty**: 2938  
**URL**: https://atcoder.jp/contests/arc142/tasks/arc142_d  
**VJudge Tag**: `[problem:AtCoder-arc142_d]`  
**Category File**: [`../categories/dynamic_programming/deterministic_piece_movement_tree_path_dp.md`](../categories/dynamic_programming/deterministic_piece_movement_tree_path_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
On a tree of N vertices, place tokens on a non-empty subset such that every good move (moving each token to an adjacent vertex with at most 1 token per edge and per vertex) is uniquely determined for all infinite steps.

## 2. Core Observation & Invariant
The reversible deterministic condition forces the tree to be partitioned into disjoint simple paths (movement paths) of length >= 2, where exactly one endpoint is empty and tokens oscillate back and forth. No conflicting edges can exist between adjacent paths: non-endpoints can only connect to non-endpoints, and endpoints must connect oppositely. This yields a tree DP with states classifying a node's path degree (0, 1, or 2 connections into child subtrees) and endpoint status.

## 3. Step-by-Step Algorithm
1. 1. Root the tree arbitrarily and compute post-order traversal.
2. 2. DP states at u: f[u][0..2] (internal path vertex with 0, 1, 2 child connections) and g[u][0..1] (endpoint with 0, 1 child connection).
3. 3. Transitions merge children multiplicatively with symmetric doubling for non-endpoint connections.
4. 4. Total valid placements is f[root][2] + 2 g[root][1] mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> order;
    order.reserve(n);
    vector<int> parent(n + 1, 0);
    vector<int> stack_nodes;
    stack_nodes.reserve(n);
    vector<bool> visited(n + 1, false);

    stack_nodes.push_back(1);
    visited[1] = true;

    while (!stack_nodes.empty()) {
        int u = stack_nodes.back();
        stack_nodes.pop_back();
        order.push_back(u);
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                parent[v] = u;
                stack_nodes.push_back(v);
            }
        }
    }

    vector<vector<long long>> f(n + 1, vector<long long>(3, 0));
    vector<vector<long long>> g(n + 1, vector<long long>(2, 0));

    for (int i = n - 1; i >= 0; --i) {
        int u = order[i];
        long long cur_f0 = 1, cur_f1 = 0, cur_f2 = 0;
        long long cur_g0 = 1, cur_g1 = 0;

        for (int v : adj[u]) {
            if (v == parent[u]) continue;

            long long new_g0 = (cur_g0 * g[v][1]) % MOD;
            long long new_g1 = (cur_g0 * f[v][1] + cur_g1 * g[v][1]) % MOD;

            long long new_f0 = (cur_f0 * f[v][2]) % MOD;
            long long new_f1 = (cur_f0 * f[v][1] + cur_f1 * f[v][2]) % MOD;
            long long new_f2 = (cur_f2 * f[v][2] + 2LL * cur_f1 % MOD * f[v][1]) % MOD;

            cur_g0 = new_g0;
            cur_g1 = new_g1;
            cur_f0 = new_f0;
            cur_f1 = new_f1;
            cur_f2 = new_f2;
        }

        cur_f1 = (cur_f1 + cur_g0) % MOD;

        f[u][0] = cur_f0;
        f[u][1] = cur_f1;
        f[u][2] = cur_f2;
        g[u][0] = cur_g0;
        g[u][1] = cur_g1;
    }

    int root = 1;
    long long ans = (f[root][2] + 2LL * g[root][1]) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
