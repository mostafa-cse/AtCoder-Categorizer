# Problem Analysis: AtCoder-abc178_d — Redistribution

**Problem ID**: `AtCoder-abc178_d`  
**Contest**: `abc178`  
**Rating / Difficulty**: 875  
**URL**: https://atcoder.jp/contests/abc178/tasks/abc178_d  
**VJudge Tag**: `[problem:AtCoder-abc178_d]`  
**Category File**: [`../categories/dp/prefix_sum_partition_dp.md`](../categories/dp/prefix_sum_partition_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Linear DP`  
- **Topic (Skill)**: `Prefix Sum Transition Acceleration on Partition DP`  

---

## 1. Problem Statement & Key Idea
Find the number of sequences of positive integers >= 3 whose sum is S (S <= 2000), modulo 10^9 + 7.

**Key Idea**: Let dp[i] be the number of valid sequences summing to i. Base case: dp[0] = 1. Transition: dp[i] = sum_{j >= 3} dp[i - j] = sum_{k=0}^{i-3} dp[k].

## 2. Core Observation & Invariant
Notice that sum_{k=0}^{i-3} dp[k] = (sum_{k=0}^{i-4} dp[k]) + dp[i-3] = dp[i-1] + dp[i-3]. Thus, dp[i] = dp[i-1] + dp[i-3] for all i >= 3, reducing naive O(S^2) transitions to O(1) per state!

## 3. Step-by-Step Algorithm
1. Initialize dp array of size S + 1 to 0; dp[0] = 1.
2. For i from 3 to S: dp[i] = (dp[i-1] + dp[i-3]) % MOD.
3. Output dp[S].

## 4. Complexity Analysis
- **Time Complexity**: `O(S)`
- **Space Complexity**: `O(S)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int s;
    if (!(cin >> s)) return 0;

    const int MOD = 1e9 + 7;
    vector<int> dp(s + 1, 0);
    dp[0] = 1;

    for (int i = 3; i <= s; ++i) {
        dp[i] = (dp[i - 1] + dp[i - 3]) % MOD;
    }

    cout << dp[s] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Accelerating range-sum DP transitions via difference recurrence.
- **Reusable Pattern**: `dp[i] = sum_{j >= K} dp[i - j] simplifies to dp[i] = dp[i-1] + dp[i-K].`
