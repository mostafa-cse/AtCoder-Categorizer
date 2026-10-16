# Problem Analysis: AtCoder-typical90_ap — Multiple of 9

**Problem ID**: `AtCoder-typical90_ap`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 042)  
**Rating / Difficulty**: 1150 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ap  
**VJudge Tag**: `[problem:AtCoder-typical90_ap]`  
**Category File**: [`../categories/dp/1d_dp.md`](../categories/dp/1d_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Digit Sum Divisibility Invariant & 9-Step Bounded Lookahead DP`  

---

## 1. Problem Statement & Key Idea
Count the number of positive integers whose digit sum equals K (K <= 10^5) and are multiples of 9. Modulo 10^9+7.

**Core Idea**: A number is divisible by 9 if and only if its digit sum is a multiple of 9.

## 2. Core Observation & Invariant
If K is not divisible by 9, answer is 0. If K is divisible by 9, the problem reduces to counting sequences of digits 1..9 that sum to K: dp[s] = sum_{d=1}^9 dp[s - d].

## 3. Step-by-Step Algorithm
1. If K % 9 != 0: return 0.
2. dp[0] = 1.
3. For s from 1 to K: for d from 1 to min(s, 9): dp[s] = (dp[s] + dp[s - d]) % MOD.
4. Output dp[K].

## 4. Complexity Analysis
Time: O(9 * K), Space: O(K).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    if (k % 9 != 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<int> dp(k + 1, 0);
    dp[0] = 1;

    for (int s = 1; s <= k; ++s) {
        for (int d = 1; d <= 9 && d <= s; ++d) {
            dp[s] = (dp[s] + dp[s - d]) % MOD;
        }
    }

    cout << dp[k] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Digit sum divisibility rule combined with 9-step lookahead linear DP.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Divisibility invariants and integer partition DP with restricted digit parts.
- **Reusable Pattern**: `Bounded Lookahead Linear DP.`

---
Back to [Digit Sum Divisibility Invariant & 9-Step Bounded Lookahead DP](../categories/dp/1d_dp.md) | [Categories Directory](../categories/README.md)