# Problem Analysis: AtCoder-arc121_e — E - Directed Tree

**Problem ID**: `AtCoder-arc121_e`  
**Contest**: `arc121`  
**Rating / Difficulty**: 2645  
**URL**: https://atcoder.jp/contests/arc121/tasks/arc121_e  
**VJudge Tag**: `[problem:AtCoder-arc121_e]`  
**Category File**: [`../categories/combinatorics/directed_tree_ancestor_pie.md`](../categories/combinatorics/directed_tree_ancestor_pie.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Given a directed tree rooted at 1, find the number of permutations a of (1 ... N) such that for every i, i is unreachable from a_i by traversing 1 or more edges, modulo 998244353.

## 2. Core Observation & Invariant
The bad condition is that a_i is a proper ancestor of i. By the Principle of Inclusion-Exclusion, we count ways to choose k pairs (u, a_u) where a_u is a proper ancestor of u. Reversing the perspective, ancestor v chooses a proper descendant u. In post-order traversal, if j descendant choices were already made in the subtree of v, exactly sz(v) - 1 - j proper descendants remain available for v to choose. This independence allows subtree knapsack DP in O(N^2).

## 3. Step-by-Step Algorithm
1. Compute subtree sizes sz_u via DFS.
2. Subtree DP: DP[u][j] is the number of ways to pick j ancestor-descendant pairs within u's subtree.
3. Convolve DP polynomials of children of u.
4. When incorporating u: either u is unmatched (j pairs), or u matches one of the (sz_u - 1 - j) available proper descendants (j+1 pairs).
5. At the root, apply PIE: sum_{k=0}^N (-1)^k DP[1][k] * (N - k)! mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int N;
vector<vector<int>> adj;
vector<int> sz;
vector<vector<long long>> dp;

void dfs(int u) {
    sz[u] = 1;
    dp[u] = {1}; // 0 pairs chosen

    for (int v : adj[u]) {
        dfs(v);
        vector<long long> next_dp(sz[u] + sz[v], 0);
        for (int i = 0; i < sz[u]; ++i) {
            if (!dp[u][i]) continue;
            for (int j = 0; j <= sz[v]; ++j) {
                if (j < (int)dp[v].size() && dp[v][j]) {
                    next_dp[i + j] = (next_dp[i + j] + dp[u][i] * dp[v][j]) % MOD;
                }
            }
        }
        dp[u] = move(next_dp);
        sz[u] += sz[v];
    }

    // Now consider whether u chooses a proper descendant
    vector<long long> res_dp(sz[u] + 1, 0);
    for (int j = 0; j < sz[u]; ++j) {
        if (!dp[u][j]) continue;
        // u does not choose
        res_dp[j] = (res_dp[j] + dp[u][j]) % MOD;
        // u chooses one of the (sz[u] - 1 - j) available proper descendants
        long long avail = sz[u] - 1 - j;
        if (avail > 0) {
            res_dp[j + 1] = (res_dp[j + 1] + dp[u][j] * avail) % MOD;
        }
    }
    dp[u] = move(res_dp);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;

    adj.assign(N + 1, vector<int>());
    sz.assign(N + 1, 0);
    dp.assign(N + 1, vector<long long>());

    for (int i = 2; i <= N; ++i) {
        int p;
        cin >> p;
        adj[p].push_back(i);
    }

    dfs(1);

    vector<long long> fact(N + 1, 1);
    for (int i = 1; i <= N; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }

    long long ans = 0;
    for (int k = 0; k <= N; ++k) {
        if (k < (int)dp[1].size() && dp[1][k]) {
            long long term = dp[1][k] * fact[N - k] % MOD;
            if (k % 2 == 1) {
                ans = (ans - term + MOD) % MOD;
            } else {
                ans = (ans + term) % MOD;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
