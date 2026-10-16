# Problem Analysis: AtCoder-typical90_h — AtCounter

**Problem ID**: `AtCoder-typical90_h`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 008)  
**Rating / Difficulty**: 1150 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_h  
**VJudge Tag**: `[problem:AtCoder-typical90_h]`  
**Category File**: [`../categories/dp/string_dp.md`](../categories/dp/string_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Subsequence Matching DP / Automaton DP`  

---

## 1. Problem Statement & Key Idea
Given string S of length N, count the number of subsequences equal to 'atcoder' modulo 10^9+7.

**Core Idea**: Track progress of matching target string 'atcoder' (length 7) using 1D state array.

## 2. Core Observation & Invariant
Each character S[i] can either be skipped or, if it matches target[j], can advance all existing prefixes of length j to length j+1.

## 3. Step-by-Step Algorithm
1. dp[0] = 1, dp[1..7] = 0.
2. Target T = 'atcoder'.
3. For char c in S: for j from 0 to 6: if c == T[j]: dp[j+1] = (dp[j+1] + dp[j]) % MOD.
4. Output dp[7].

## 4. Complexity Analysis
Time: O(|T| * N) = O(7N), Space: O(|T|) = O(1).

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

    string target = "atcoder";
    vector<int> dp(8, 0);
    dp[0] = 1;

    for (char c : s) {
        for (int j = 0; j < 7; ++j) {
            if (c == target[j]) {
                dp[j + 1] = (dp[j + 1] + dp[j]) % MOD;
            }
        }
    }

    cout << dp[7] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Linear string prefix matching dynamic programming.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting pattern subsequences in linear time using state transition arrays.
- **Reusable Pattern**: `Pattern-Prefix Subsequence DP.`

---
Back to [Subsequence Matching DP / Automaton DP](../categories/dp/string_dp.md) | [Categories Directory](../categories/README.md)