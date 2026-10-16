# Problem Analysis: AtCoder-arc060_a — Tak and Cards

**Problem ID**: `AtCoder-arc060_a`  
**Contest**: `abc044`  
**Rating / Difficulty**: 1583  
**URL**: https://atcoder.jp/contests/abc044/tasks/arc060_a  
**VJudge Tag**: `[problem:AtCoder-arc060_a]`  
**Category File**: [`../categories/dp/shifted_zero_sum_knapsack_average.md`](../categories/dp/shifted_zero_sum_knapsack_average.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Subset Average Equals A via Shifted Zero-Sum Knapsack DP`  

---

## 1. Problem Statement & Key Idea
Given N cards x_1, ..., x_N and an integer A. Find the number of non-empty subsets of cards whose arithmetic mean equals A.

**Key Insight**: The average of a subset equals A iff sum_{i in S} x_i = |S| * A iff sum_{i in S} (x_i - A) = 0. Shift each card value by -A: y_i = x_i - A. The problem becomes counting non-empty subsets with sum = 0.

## 2. Core Observation & Invariant
Because -50 <= y_i <= 50, the sum of any subset lies in [-2500, 2500]. Offset by 2500 to store in a standard 1D/2D DP table. At the end, dp[offset] - 1 (excluding empty subset) is the exact answer.

## 3. Step-by-Step Algorithm
1. Let OFFSET = 2500. dp[2 * OFFSET + 1] initialized to 0. dp[OFFSET] = 1.
2. For each card x:
3.   y = x - A.
4.   next_dp = dp.
5.   For s from 0 to 2 * OFFSET:
6.     If dp[s] > 0 and 0 <= s + y <= 2 * OFFSET:
7.       next_dp[s + y] += dp[s].
8.   dp = move(next_dp).
9. Print dp[OFFSET] - 1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * max(X))`
- **Space Complexity**: `O(N * max(X))`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int OFFSET = 2500;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, a;
    if (!(cin >> n >> a)) return 0;

    vector<long long> dp(2 * OFFSET + 1, 0);
    dp[OFFSET] = 1;

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        int y = x - a;
        vector<long long> next_dp = dp;

        for (int s = 0; s <= 2 * OFFSET; ++s) {
            if (dp[s] > 0) {
                int ns = s + y;
                if (ns >= 0 && ns <= 2 * OFFSET) {
                    next_dp[ns] += dp[s];
                }
            }
        }
        dp = move(next_dp);
    }

    cout << dp[OFFSET] - 1 << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Mean-target transformation into shifted zero-sum knapsack DP.
- **Reusable Pattern**: `Average Equals Target: shift elements by y_i = x_i - Target, count subsets summing to 0.`
