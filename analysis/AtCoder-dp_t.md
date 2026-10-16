# Problem Analysis: AtCoder-dp_t — Permutation

**Problem ID**: `AtCoder-dp_t`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1950  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_t  
**VJudge Tag**: `[problem:AtCoder-dp_t]`  
**Category File**: [`../categories/dp/prefix_sum_dp.md`](../categories/dp/prefix_sum_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Relative Order Insertion DP with Prefix Sums`  

---

## 1. Problem Statement & Key Idea
Given a signature string S of length N-1 with characters '<' and '>', count permutations p of 1..N satisfying p_i < p_{i+1} if S_i == '<' and p_i > p_{i+1} if S_i == '>'.

**Core Idea**: Construct permutation of 1..N element by element. When inserting element i, insert it into relative rank j in [1, i] among previously placed elements.

## 2. Core Observation & Invariant
If S[i-1] == '<', j must be greater than previous element's rank k. If '>', j must be <= k. Prefix sums evaluate the transition sum in O(1).

## 3. Step-by-Step Algorithm
1. dp[1][1] = 1.
2. For i from 2 to N: compute prefix sums pref of dp[i-1].
3. If S[i-2] == '<': dp[i][j] = pref[j-1]. If S[i-2] == '>': dp[i][j] = pref[i-1] - pref[j-1].
4. Return sum_{j=1}^N dp[N][j] mod MOD.

## 4. Complexity Analysis
Time: O(N^2), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    vector<int> dp(2, 0);
    dp[1] = 1;

    for (int i = 2; i <= n; ++i) {
        vector<int> pref(i, 0);
        for (int j = 1; j < i; ++j) {
            pref[j] = (pref[j - 1] + dp[j]) % MOD;
        }

        vector<int> next_dp(i + 1, 0);
        char cond = s[i - 2];
        for (int j = 1; j <= i; ++j) {
            if (cond == '<') {
                next_dp[j] = pref[j - 1];
            } else {
                next_dp[j] = (pref[i - 1] - pref[j - 1] + MOD) % MOD;
            }
        }
        dp = next_dp;
    }

    int ans = 0;
    for (int j = 1; j <= n; ++j) {
        ans = (ans + dp[j]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Relative order insertion DP with prefix sum acceleration.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Constructing permutations by inserting elements into relative rank slots and optimizing transitions with prefix sums.
- **Reusable Pattern**: `Relative rank insertion DP + prefix sum acceleration.`

---
Back to [Relative Order Insertion DP with Prefix Sums](../categories/dp/prefix_sum_dp.md) | [Categories Directory](../categories/README.md)