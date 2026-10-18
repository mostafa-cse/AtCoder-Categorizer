# Problem Analysis: AtCoder-abc207_f — F. Tree Patrolling

**Problem ID**: `AtCoder-abc207_f`  
**Contest**: `abc207`  
**Rating / Difficulty**: 2398  
**URL**: https://atcoder.jp/contests/abc207/tasks/abc207_f  
**VJudge Tag**: `[problem:AtCoder-abc207_f]`  
**Category File**: [`../categories/dynamic_programming/tree_guard_coverage_combining_subtrees_dp.md`](../categories/dynamic_programming/tree_guard_coverage_combining_subtrees_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `Combining Subtrees Technique`  

---

## 1. Problem Statement & Key Idea
Tree DP with 3 states per node (unguarded, guard placed, guarded by child) counts covered vertices. Merging subtrees via tree knapsack bounds total operations to O(N^2).

## 2. Core Observation & Invariant
In tree DP counting guard placements covering exactly K vertices, each vertex u requires 3 states: 0 (no guard, unguarded), 1 (guard placed at u, self and neighbors guarded), 2 (no guard at u, guarded by a child). Subtree merges run in O(size(u) * size(v)), bounding total complexity to O(N^2) by the tree knapsack theorem.

## 3. Step-by-Step Algorithm
1. Root the tree arbitrarily at vertex 1.
2. Define dp[u][state][k] where state in {0, 1, 2} and k is guarded vertices in u's subtree.
3. Base case for vertex u: dp[u][0][0] = 1, dp[u][1][1] = 1.
4. For each child v of u, merge dp tables considering edge interactions between u and v across all 3 x 3 state pairs.
5. Sum dp[root][0..2][K] for each K in [0, N] in O(N^2) total time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    if (!(cin >> N)) return 0;
    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> sz(N + 1, 1);
    vector<vector<vector<ll>>> dp(N + 1, vector<vector<ll>>(3));

    function<void(int, int)> dfs = [&](int u, int p) {
        dp[u][0] = {1, 0};
        dp[u][1] = {0, 1};
        dp[u][2] = {0, 0};
        sz[u] = 1;

        for (int v : adj[u]) {
            if (v == p) continue;
            dfs(v, u);

            int new_sz = sz[u] + sz[v];
            vector<vector<ll>> nxt(3, vector<ll>(new_sz + 1, 0));

            for (int su = 0; su < 3; su++) {
                for (int ku = 0; ku <= sz[u]; ku++) {
                    ll val_u = dp[u][su][ku];
                    if (!val_u) continue;
                    for (int sv = 0; sv < 3; sv++) {
                        for (int kv = 0; kv <= sz[v]; kv++) {
                            ll val_v = dp[v][sv][kv];
                            if (!val_v) continue;
                            ll ways = (val_u * val_v) % MOD;

                            if (su == 0) {
                                if (sv == 0) {
                                    nxt[0][ku + kv] = (nxt[0][ku + kv] + ways) % MOD;
                                } else if (sv == 1) {
                                    nxt[2][ku + kv + 1] = (nxt[2][ku + kv + 1] + ways) % MOD;
                                } else {
                                    nxt[0][ku + kv] = (nxt[0][ku + kv] + ways) % MOD;
                                }
                            } else if (su == 1) {
                                if (sv == 0) {
                                    nxt[1][ku + kv + 1] = (nxt[1][ku + kv + 1] + ways) % MOD;
                                } else {
                                    nxt[1][ku + kv] = (nxt[1][ku + kv] + ways) % MOD;
                                }
                            } else { // su == 2
                                nxt[2][ku + kv] = (nxt[2][ku + kv] + ways) % MOD;
                            }
                        }
                    }
                }
            }
            sz[u] = new_sz;
            dp[u] = move(nxt);
        }
    };

    dfs(1, 0);

    for (int k = 0; k <= N; k++) {
        ll total = (dp[1][0][k] + dp[1][1][k] + dp[1][2][k]) % MOD;
        cout << total << "\n";
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
