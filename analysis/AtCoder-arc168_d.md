# Problem Analysis: AtCoder-arc168_d — D. Maximize Update

**Problem ID**: `AtCoder-arc168_d`  
**Contest**: `arc168`  
**Rating / Difficulty**: 2440  
**URL**: https://atcoder.jp/contests/arc168/tasks/arc168_d  
**VJudge Tag**: `[problem:AtCoder-arc168_d]`  
**Category File**: [`../categories/dynamic_programming_dp/maximize_update_interval_dp.md`](../categories/dynamic_programming_dp/maximize_update_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Maximize the number of operations that paint at least one previously white square black, given $M$ candidate intervals $[L_i, R_i]$.

## 2. Core Observation & Invariant
Consider the last square $k \in [l, r]$ to be newly painted. The operation covering $k$ must be strictly contained inside $[l, r]$. All other operations painting squares in $[l, k-1]$ or $[k+1, r]$ cannot cover $k$, separating the problem into completely independent subintervals $[l, k-1]$ and $[k+1, r]$. An interval covering $k$ inside $[l, r]$ exists iff $\max \{ L_i \mid L_i \le k \le R_i \le r \} \ge l$.

## 3. Step-by-Step Algorithm
1. 1. For each square $k$ and right endpoint $r$, precompute `best_l[k][r]` as the maximum $L_i$ of an interval covering $k$ with $R_i \le r$.
2. 2. Compute 2D DP $DP[l][r]$ over interval lengths from 1 to $N$.
3. 3. Transition: $DP[l][r] = \max_{l \le k \le r} (DP[l][k-1] + DP[k+1][r] + [\text{best\_l}[k][r] \ge l])$.
4. 4. Output $DP[1][N]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 + M)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> best_l(n + 2, vector<int>(n + 2, 0));
    for (int i = 0; i < m; ++i) {
        int l, r;
        cin >> l >> r;
        for (int k = l; k <= r; ++k) {
            best_l[k][r] = max(best_l[k][r], l);
        }
    }
    for (int k = 1; k <= n; ++k) {
        for (int r = 1; r <= n; ++r) {
            best_l[k][r] = max(best_l[k][r], best_l[k][r - 1]);
        }
    }
    vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
    for (int len = 1; len <= n; ++len) {
        for (int l = 1; l + len - 1 <= n; ++l) {
            int r = l + len - 1;
            int mx = 0;
            for (int k = l; k <= r; ++k) {
                int cost = (best_l[k][r] >= l ? 1 : 0);
                int val = dp[l][k - 1] + dp[k + 1][r] + cost;
                if (val > mx) mx = val;
            }
            dp[l][r] = mx;
        }
    }
    cout << dp[1][n] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
