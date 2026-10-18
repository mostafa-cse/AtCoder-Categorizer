# Problem Analysis: AtCoder-abc395_g — G. Minimum Steiner Tree 2

**Problem ID**: `AtCoder-abc395_g`  
**Contest**: `abc395`  
**Rating / Difficulty**: 2561  
**URL**: https://atcoder.jp/contests/abc395/tasks/abc395_g  
**VJudge Tag**: `[problem:AtCoder-abc395_g]`  
**Category File**: [`../categories/graph_theory/minimum_steiner_tree_dreyfus_wagner.md`](../categories/graph_theory/minimum_steiner_tree_dreyfus_wagner.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Minimum Spanning Tree (MST)`  
- **Topic (Skill)**: `Steiner Tree Problem`  

---

## 1. Problem Statement & Key Idea
Given edge weights $C_{u, v}$ and $K \le 8$ fixed terminal vertices $\{1 \dots K\}$, answer $Q$ queries: find the minimum weight connected subgraph spanning $\{1 \dots K\} \cup \{s, t\}$.

## 2. Core Observation & Invariant
Dreyfus-Wagner Minimum Steiner Tree DP on terminal subset $S \subseteq \{1 \dots K\}$. Precomputing extensions for each single query terminal $s \in [K, N-1]$ via $ndp_s[mask][u]$ allows every two-terminal query $(s, t)$ to be answered in $O(1)$ time by querying $ndp_s[(1 \ll K) - 1][t]$.

## 3. Step-by-Step Algorithm
1. 1. Run Dreyfus-Wagner DP to compute $DP[mask][u]$ for all $mask \subseteq \{1 \dots K\}$ and $u \in [0, N-1]$.
2. 2. For each query terminal candidate $s \in [K, N-1]$, initialize $ndp_s[0][s] = 0$ and run Dreyfus-Wagner combining with $DP$.
3. 3. Store $ans[s][t] = ndp_s[(1 \ll K) - 1][t]$.
4. 4. For each query $(s, t)$, output $ans[s-1][t-1]$ in $O(1)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^K N^2 + 2^K N^3 + Q)`
- **Space Complexity**: `O(2^K N + N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1LL << 60;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<vector<long long>> c(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> c[i][j];
        }
    }

    vector<vector<long long>> dp(1 << k, vector<long long>(n, INF));
    for (int j = 0; j < n; ++j) dp[0][j] = 0;
    for (int i = 0; i < k; ++i) dp[1 << i][i] = 0;

    for (int i = 1; i < (1 << k); ++i) {
        for (int bi = i; ; bi = (bi - 1) & i) {
            for (int j = 0; j < n; ++j) {
                dp[i][j] = min(dp[i][j], dp[bi][j] + dp[i ^ bi][j]);
            }
            if (bi == 0) break;
        }

        vector<bool> used(n, false);
        for (int step = 0; step < n; ++step) {
            long long mi = INF;
            int v = -1;
            for (int u = 0; u < n; ++u) {
                if (!used[u] && dp[i][u] < mi) {
                    mi = dp[i][u];
                    v = u;
                }
            }
            if (v == -1) break;
            used[v] = true;
            for (int u = 0; u < n; ++u) {
                dp[i][u] = min(dp[i][u], dp[i][v] + c[v][u]);
            }
        }
    }

    vector<vector<long long>> ans(n, vector<long long>(n, 0));
    for (int s = k; s < n; ++s) {
        vector<vector<long long>> ndp(1 << k, vector<long long>(n, INF));
        ndp[0][s] = 0;
        for (int i = 0; i < (1 << k); ++i) {
            for (int bi = i; ; bi = (bi - 1) & i) {
                for (int j = 0; j < n; ++j) {
                    ndp[i][j] = min(ndp[i][j], ndp[bi][j] + dp[i ^ bi][j]);
                }
                if (bi == 0) break;
            }

            vector<bool> used(n, false);
            for (int step = 0; step < n; ++step) {
                long long mi = INF;
                int v = -1;
                for (int u = 0; u < n; ++u) {
                    if (!used[u] && ndp[i][u] < mi) {
                        mi = ndp[i][u];
                        v = u;
                    }
                }
                if (v == -1) break;
                used[v] = true;
                for (int u = 0; u < n; ++u) {
                    ndp[i][u] = min(ndp[i][u], ndp[i][v] + c[v][u]);
                }
            }
        }
        ans[s] = ndp[(1 << k) - 1];
    }

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        int s, t;
        cin >> s >> t;
        s--; t--;
        cout << ans[s][t] << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
