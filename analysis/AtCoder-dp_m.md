# Problem Analysis: AtCoder-dp_m — Candies

**Problem ID**: `AtCoder-dp_m`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1550  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_m  
**VJudge Tag**: `[problem:AtCoder-dp_m]`  
**Category File**: [`../categories/dp/prefix_sum_dp.md`](../categories/dp/prefix_sum_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Prefix Sum Optimized DP`  

---

## 1. Problem Statement & Key Idea
Distribute K candies among N children such that child i receives at most a_i candies.

**Core Idea**: The naive transition dp[i][j] = sum_{k=0}^{a_i} dp[i-1][j-k] is over a contiguous range [j - a_i, j] in dp[i-1].

## 2. Core Observation & Invariant
Prefix sums of the previous row evaluate the contiguous range sum in O(1), dropping overall complexity from O(N * K^2) to O(N * K).

## 3. Step-by-Step Algorithm
1. dp[0] = 1, others 0.
2. For each child i: compute prefix sums pref of current dp.
3. dp[j] = (pref[j+1] - pref[max(0, j - a_i)]) mod MOD.
4. Return dp[K].

## 4. Complexity Analysis
Time: O(N * K), Space: O(K).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> dp(k + 1, 0);
    dp[0] = 1;

    for (int i = 0; i < n; ++i) {
        vector<int> pref(k + 2, 0);
        for (int j = 0; j <= k; ++j) {
            pref[j + 1] = (pref[j] + dp[j]) % MOD;
        }

        vector<int> next_dp(k + 1, 0);
        for (int j = 0; j <= k; ++j) {
            int left = max(0, j - a[i]);
            next_dp[j] = (pref[j + 1] - pref[left] + MOD) % MOD;
        }
        dp = next_dp;
    }

    cout << dp[k] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Prefix sum acceleration of contiguous state transitions.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Sliding window range sum optimization reducing quadratic transitions to linear.
- **Reusable Pattern**: `Prefix sum acceleration of contiguous state transitions.`

---
Back to [Prefix Sum Optimized DP](../categories/dp/prefix_sum_dp.md) | [Categories Directory](../categories/README.md)