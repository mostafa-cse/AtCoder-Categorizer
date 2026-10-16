# Problem Analysis: AtCoder-dp_i — Coins

**Problem ID**: `AtCoder-dp_i`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1150  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_i  
**VJudge Tag**: `[problem:AtCoder-dp_i]`  
**Category File**: [`../categories/dp/expected_value_dp.md`](../categories/dp/expected_value_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Probability and Expected Value DP`  

---

## 1. Problem Statement & Key Idea
N independent biased coins have probabilities p_i of turning up heads. Find the probability that more heads than tails appear.

**Core Idea**: Calculate the exact probability that more heads than tails appear when tossing N independent biased coins.

## 2. Core Observation & Invariant
Let dp[i][j] be probability of exactly j heads after i coin tosses. Outcome partitions probability mass into two events: heads (p_i) or tails (1 - p_i).

## 3. Step-by-Step Algorithm
1. dp[0][0] = 1.0; others 0.0.
2. For i in 1..N: for j in 0..i: dp[i][j] = (j > 0 ? dp[i-1][j-1] * p_i : 0) + dp[i-1][j] * (1 - p_i).
3. Sum dp[N][j] for j > N/2.

## 4. Complexity Analysis
Time: O(N^2), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<double> p(n);
    for (int i = 0; i < n; ++i) cin >> p[i];

    vector<double> dp(n + 1, 0.0);
    dp[0] = 1.0;

    for (int i = 0; i < n; ++i) {
        vector<double> next_dp(n + 1, 0.0);
        for (int j = 0; j <= i; ++j) {
            next_dp[j + 1] += dp[j] * p[i];
            next_dp[j] += dp[j] * (1.0 - p[i]);
        }
        dp = next_dp;
    }

    double ans = 0.0;
    for (int j = (n + 1) / 2; j <= n; ++j) {
        ans += dp[j];
    }

    cout << fixed << setprecision(10) << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Poisson binomial distribution dynamic programming.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Probability mass conservation and floating-point accumulation in discrete trial DP.
- **Reusable Pattern**: `Probability convolution DP over independent Bernoulli trials.`

---
Back to [Probability and Expected Value DP](../categories/dp/expected_value_dp.md) | [Categories Directory](../categories/README.md)