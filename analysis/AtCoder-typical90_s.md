# Problem Analysis: AtCoder-typical90_s — Pick Two

**Problem ID**: `AtCoder-typical90_s`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 019)  
**Rating / Difficulty**: 2100 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_s  
**VJudge Tag**: `[problem:AtCoder-typical90_s]`  
**Category File**: [`../categories/dp/interval_dp.md`](../categories/dp/interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Elimination and Outer Pairing`  

---

## 1. Problem Statement & Key Idea
2N integers are arranged in a row. Repeatedly remove an adjacent pair (x, y) with cost |x - y| until all numbers are removed. Find minimum total cost.

**Core Idea**: The operation is equivalent to nested parenthesis matching on 2N elements. Solve with Interval DP by increasing interval length.

## 2. Core Observation & Invariant
For an interval [l, r] of even length, either the boundary elements l and r are matched together at cost |A[l] - A[r]| + dp[l+1][r-1], or the interval decomposes into two independent sub-eliminations dp[l][k] + dp[k+1][r].

## 3. Step-by-Step Algorithm
1. dp[l][r]: min cost to eliminate subarray A[l..r].
2. Base: dp[i][i+1] = |A[i] - A[i+1]|.
3. Loop len from 4 to 2N by 2:
   - Loop l from 1 to 2N - len + 1, r = l + len - 1:
     - dp[l][r] = |A[l] - A[r]| + dp[l+1][r-1]
     - for k in l+1..r-2 step 2: dp[l][r] = min(dp[l][r], dp[l][k] + dp[k+1][r])
4. Output dp[1][2N].

## 4. Complexity Analysis
Time: O((2N)^3) = O(N^3), Space: O(N^2).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    int m = 2 * n;
    vector<long long> a(m + 1);
    for (int i = 1; i <= m; ++i) cin >> a[i];

    vector<vector<long long>> dp(m + 2, vector<long long>(m + 2, INF));

    for (int i = 1; i <= m + 1; ++i) {
        dp[i][i - 1] = 0; // empty interval
    }

    for (int i = 1; i < m; ++i) {
        dp[i][i + 1] = abs(a[i] - a[i + 1]);
    }

    for (int len = 4; len <= m; len += 2) {
        for (int l = 1; l <= m - len + 1; ++l) {
            int r = l + len - 1;
            // Case 1: Match outer elements l and r
            dp[l][r] = abs(a[l] - a[r]) + dp[l + 1][r - 1];
            // Case 2: Split point k
            for (int k = l + 1; k < r; k += 2) {
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r]);
            }
        }
    }

    cout << dp[1][m] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Interval dynamic programming with boundary pairing and split-point relaxation.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Interval DP formulation for nested reduction problems and optimal pairing structures.
- **Reusable Pattern**: `Boundary Pairing & Split Interval DP.`

---
Back to [Interval DP / Elimination and Outer Pairing](../categories/dp/interval_dp.md) | [Categories Directory](../categories/README.md)