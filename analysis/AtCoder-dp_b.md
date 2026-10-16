# Problem Analysis: AtCoder-dp_b — Frog 2

**Problem ID**: `AtCoder-dp_b`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 700  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_b  
**VJudge Tag**: `[problem:AtCoder-dp_b]`  
**Category File**: [`../categories/dp/1d_dp.md`](../categories/dp/1d_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `1D DP with K-Step Transitions`  

---

## 1. Problem Statement & Key Idea
Similar to Frog 1, but the frog can jump up to K stones forward (from i to i+j for 1 <= j <= K). Find min cost to reach stone N.

**Core Idea**: Generalize jumps to up to K stones with minimum total energy cost.

## 2. Core Observation & Invariant
Each state dp[i] is relaxed over a sliding window of the previous K states: dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).

## 3. Step-by-Step Algorithm
1. Set dp[1] = 0, others INF.
2. For i from 1 to N-1: for step in 1..K with i+step <= N: dp[i+step] = min(dp[i+step], dp[i] + |h_{i+step} - h_i|).
3. Result is dp[N].

## 4. Complexity Analysis
Time: O(N * K), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> h(n + 1);
    for (int i = 1; i <= n; ++i) cin >> h[i];

    vector<int> dp(n + 1, INF);
    dp[1] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k && i + j <= n; ++j) {
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]));
        }
    }

    cout << dp[n] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Standard push-based relaxation over parameterized lookahead.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Parameterized transition loops and boundary-bounded relaxation.
- **Reusable Pattern**: `Push DP over variable-sized transition intervals.`

---
Back to [1D DP with K-Step Transitions](../categories/dp/1d_dp.md) | [Categories Directory](../categories/README.md)