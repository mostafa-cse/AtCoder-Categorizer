# Problem Analysis: AtCoder-abc015_4 — Takahashi's Pain

**Problem ID**: `AtCoder-abc015_4`  
**Contest**: `abc015`  
**Rating / Difficulty**: 1388  
**URL**: https://atcoder.jp/contests/abc015/tasks/abc015_4  
**VJudge Tag**: `[problem:AtCoder-abc015_4]`  
**Category File**: [`../categories/dp/two_constraint_knapsack_dp.md`](../categories/dp/two_constraint_knapsack_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Knapsack DP`  
- **Topic (Skill)**: `2D Bound 0-1 Knapsack DP (Capacity + Item Count Limit)`  

---

## 1. Problem Statement & Key Idea
N screenshots, screenshot i has width A_i and value B_i. Select at most K screenshots with total width <= W to maximize total value (N <= 50, W <= 10000, K <= N).

**Key Idea**: Standard 0-1 Knapsack with TWO constraints: total weight <= W and total item count <= K.

## 2. Core Observation & Invariant
Define dp[k][w] = maximum value using exactly k items with total weight w. For each item (A_i, B_i), iterate backwards k from K down to 1 and w from W down to A_i: dp[k][w] = max(dp[k][w], dp[k - 1][w - A_i] + B_i).

## 3. Step-by-Step Algorithm
1. Initialize 2D table dp[K + 1][W + 1] to 0.
2. For each item (A, B):
3.   For k from K down to 1:
4.     For w from W down to A: dp[k][w] = max(dp[k][w], dp[k - 1][w - A] + B).
5. Find maximum value across all k in 1..K and w in 0..W.
6. Print the maximum.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * K * W)`
- **Space Complexity**: `O(K * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w_limit, n, k_limit;
    if (!(cin >> w_limit >> n >> k_limit)) return 0;

    vector<vector<int>> dp(k_limit + 1, vector<int>(w_limit + 1, 0));

    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;

        for (int k = k_limit; k >= 1; --k) {
            for (int w = w_limit; w >= a; --w) {
                dp[k][w] = max(dp[k][w], dp[k - 1][w - a] + b);
            }
        }
    }

    int ans = 0;
    for (int k = 1; k <= k_limit; ++k) {
        for (int w = 0; w <= w_limit; ++w) {
            ans = max(ans, dp[k][w]);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 2-dimensional capacity constraint handling in 0-1 Knapsack.
- **Reusable Pattern**: `2D constraint knapsack: reverse iterate both capacity w and count k.`
