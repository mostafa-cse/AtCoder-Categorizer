# Problem Analysis: AtCoder-dp_l — Deque

**Problem ID**: `AtCoder-dp_l`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1400  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_l  
**VJudge Tag**: `[problem:AtCoder-dp_l]`  
**Category File**: [`../categories/dp/interval_dp.md`](../categories/dp/interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Two players remove numbers from either end of an array. Player 1 maximizes X - Y, Player 2 minimizes it.

**Core Idea**: Over remaining subsegment [l, r], the active player chooses either a_l or a_r: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).

## 2. Core Observation & Invariant
Zero-sum game with symmetric negation: your advantage equals your chosen element minus opponent's optimal advantage from remaining subinterval.

## 3. Step-by-Step Algorithm
1. Base: dp[i][i] = a_i.
2. Loop len from 2 to N: loop l from 1 to N-len+1: r = l+len-1: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).
3. Return dp[1][N].

## 4. Complexity Analysis
Time: O(N^2), Space: O(N^2).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) dp[i][i] = a[i];

    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l <= n - len; ++l) {
            int r = l + len - 1;
            dp[l][r] = max(a[l] - dp[l + 1][r], a[r] - dp[l][r - 1]);
        }
    }

    cout << dp[0][n - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Zero-sum minimax interval DP.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Interval dynamic programming evaluated by segment length and minimax negation.
- **Reusable Pattern**: `Minimax interval DP: dp[l][r] = max(opt_left - dp[l+1][r], opt_right - dp[l][r-1]).`

---
Back to [Interval DP / Range DP / Matrix Chain Multiplication (MCM)](../categories/dp/interval_dp.md) | [Categories Directory](../categories/README.md)