# Problem Analysis: AtCoder-arc178_d — D. Delete Range Mex

**Problem ID**: `AtCoder-arc178_d`  
**Contest**: `arc178`  
**Rating / Difficulty**: 2498  
**URL**: https://atcoder.jp/contests/arc178/tasks/arc178_d  
**VJudge Tag**: `[problem:AtCoder-arc178_d]`  
**Category File**: [`../categories/data_structures_ds/delete_range_mex_cartesian_tree_dp.md`](../categories/data_structures_ds/delete_range_mex_cartesian_tree_dp.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `More Tree Data Structures`  
- **Topic (Skill)**: `Cartesian Tree`  

---

## 1. Problem Statement & Key Idea
Count permutations $P$ of $(0, 1, \dots, N-1)$ containing sequence $A$ as a subsequence such that repeatedly deleting range minimum / MEX reduces to valid intervals.

## 2. Core Observation & Invariant
The condition corresponds to Cartesian tree insertion: elements not in $A$ must be inserted strictly outside the span of currently placed smaller elements. Tracking $l$ and $r$ as the remaining unplaced elements of $A$ to the left and right, placing element $i \notin A$ splits into transitions $(l, r) \to (l', r)$ or $(l, r')$. These transitions can be updated in $O(M^2)$ using 2D prefix sums.

## 3. Step-by-Step Algorithm
1. 1. Map indices of elements in $A$ into $B[v] \in [0, M-1]$, or $-1$ if not in $A$.
2. 2. Initialize $DP[l][r]$ at step 0: if $B[0] \ne -1$, $DP[B[0]][M - 1 - B[0]] = 1$; else $DP[i][M - i] = 1$.
3. 3. For $i = 1 \dots N-1$:
4.    - If $B[i] \ne -1$, transition $DP[\min(l, B[i])][\min(r, M - 1 - B[i])] += DP[l][r]$.
5.    - If $B[i] == -1$, compute prefix sums of $DP$ along columns and rows: $DP[l][r] \leftarrow \sum_{l' \ge l} DP[l'][r] + \sum_{r' \ge r} DP[l][r']$.
6. 4. Output $DP[0][0] \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N M^2)`
- **Space Complexity**: `O(M^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<int> a(m);
    vector<int> b(n, -1);
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
        b[a[i]] = i;
    }

    vector<vector<int>> dp(m + 1, vector<int>(m + 1, 0));
    vector<vector<int>> n_dp(m + 1, vector<int>(m + 1, 0));

    if (b[0] != -1) {
        dp[b[0]][m - 1 - b[0]] = 1;
    } else {
        for (int i = 0; i <= m; ++i) {
            dp[i][m - i] = 1;
        }
    }

    for (int i = 1; i < n; ++i) {
        if (b[i] != -1) {
            for (int l = 0; l <= m; ++l) {
                for (int r = 0; r <= m - l; ++r) {
                    if (!dp[l][r]) continue;
                    int na = min(l, b[i]);
                    int nb = min(r, m - 1 - b[i]);
                    if (na != l || nb != r) {
                        dp[na][nb] = (dp[na][nb] + dp[l][r]) % MOD;
                        dp[l][r] = 0;
                    }
                }
            }
        } else {
            for (int l = 0; l <= m; ++l) {
                for (int r = 0; r <= m - l; ++r) {
                    n_dp[l][r] = dp[l][r];
                }
            }
            for (int l = m; l >= 0; --l) {
                for (int r = m - l; r >= 0; --r) {
                    if (l != m) dp[l][r] = (dp[l][r] + dp[l + 1][r]) % MOD;
                    if (r != m) n_dp[l][r] = (n_dp[l][r] + n_dp[l][r + 1]) % MOD;
                }
            }
            for (int l = 0; l <= m; ++l) {
                for (int r = 0; r <= m - l; ++r) {
                    dp[l][r] = (dp[l][r] + n_dp[l][r]) % MOD;
                }
            }
        }
    }

    cout << dp[0][0] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
