# Problem Analysis: AtCoder-abc275_f — Erase Subarrays

**Problem ID**: `AtCoder-abc275_f`  
**Contest**: `abc275`  
**Rating / Difficulty**: 1608  
**URL**: https://atcoder.jp/contests/abc275/tasks/abc275_f  
**VJudge Tag**: `[problem:AtCoder-abc275_f]`  
**Category File**: [`../categories/dp/subarray_deletion_knapsack_dp.md`](../categories/dp/subarray_deletion_knapsack_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `2-State DP on Subarray Deletion to Match Target Sum`  

---

## 1. Problem Statement & Key Idea
Given an array A of length N. For each integer z from 1 to M, find the minimum number of contiguous subarrays to erase from A such that the sum of the remaining elements is exactly z (or -1 if impossible).

**Key Insight**: Dynamic programming maintaining whether the previous element was deleted or retained. `dp[sum][state]` where state 0 = retained, state 1 = deleted.

## 2. Core Observation & Invariant
Transitioning to state 0 (keep A[i]): adds A[i] to sum, taking min(dp[sum][0], dp[sum][1]). Transitioning to state 1 (erase A[i]): from state 1 costs 0 extra operations (continuing erasure); from state 0 costs +1 operation (starting a new erasure).

## 3. Step-by-Step Algorithm
1. Initialize dp[M + 1][2] with INF. dp[0][0] = 0.
2. For each element a in A:
3.   next_dp[M + 1][2] = INF.
4.   For s from 0 to M:
5.     // State 1: erase a
6.     next_dp[s][1] = min(dp[s][1], dp[s][0] + 1);
7.     // State 0: keep a
8.     if (s + a <= M):
9.       next_dp[s + a][0] = min(dp[s][0], dp[s][1]);
10.   dp = move(next_dp).
11. For z from 1 to M:
12.   ans = min(dp[z][0], dp[z][1]);
13.   Print ans < INF ? ans : -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    // dp[sum][state]: state 0 = kept, state 1 = erased
    vector<vector<int>> dp(m + 1, vector<int>(2, INF));
    dp[0][0] = 0;

    for (int x : a) {
        vector<vector<int>> next_dp(m + 1, vector<int>(2, INF));
        for (int s = 0; s <= m; ++s) {
            // Erase x
            next_dp[s][1] = min(dp[s][1], dp[s][0] + 1);

            // Keep x
            if (s + x <= m) {
                next_dp[s + x][0] = min(dp[s][0], dp[s][1]);
            }
        }
        dp = move(next_dp);
    }

    for (int z = 1; z <= m; ++z) {
        int ans = min(dp[z][0], dp[z][1]);
        cout << (ans >= INF ? -1 : ans) << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: State-augmented knapsack DP for contiguous interval deletion penalties.
- **Reusable Pattern**: `Interval Deletion Knapsack: dp[s][0] (kept) and dp[s][1] (deleted), +1 cost when entering deleted state.`
