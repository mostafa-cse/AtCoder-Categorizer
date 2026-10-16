# Problem Analysis: AtCoder-dp_a — Frog 1

**Problem ID**: `AtCoder-dp_a`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 600  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_a  
**VJudge Tag**: `[problem:AtCoder-dp_a]`  
**Category File**: [`../categories/dp/1d_dp.md`](../categories/dp/1d_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `1D State Recurrence / Bounded Lookahead`  

---

## 1. Problem Statement & Key Idea
N stones are numbered 1 to N with heights h_i. Starting from stone 1, the frog can jump to stone i+1 or i+2 with cost |h_i - h_j|. Find minimum total cost to reach stone N.

**Core Idea**: Represent the minimum cost to reach stone i using optimal substructure from the previous two stones.

## 2. Core Observation & Invariant
At stone i, arrival is possible exclusively from i-1 or i-2. The state depends only on local height differences and optimal prefix solutions. Space compresses to O(1).

## 3. Step-by-Step Algorithm
1. Initialize dp[1] = 0, dp[2] = |h_2 - h_1|.
2. For i from 3 to N: dp[i] = min(dp[i-1] + |h_i - h_{i-1}|, dp[i-2] + |h_i - h_{i-2}|).
3. Result is dp[N].

## 4. Complexity Analysis
Time: O(N), Space: O(1) rolling state.

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> h(n + 1);
    for (int i = 1; i <= n; ++i) cin >> h[i];

    vector<int> dp(n + 1, 0);
    dp[1] = 0;
    if (n >= 2) dp[2] = abs(h[2] - h[1]);

    for (int i = 3; i <= n; ++i) {
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
                    dp[i - 2] + abs(h[i] - h[i - 2]));
    }

    cout << dp[n] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Standard 1D forward relaxation recurrence.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Optimal substructure, state initialization, and memory-compressed transitions.
- **Reusable Pattern**: `Linear 1D DP with constant lookback window.`

---
Back to [1D State Recurrence / Bounded Lookahead](../categories/dp/1d_dp.md) | [Categories Directory](../categories/README.md)