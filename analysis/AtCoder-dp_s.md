# Problem Analysis: AtCoder-dp_s — Digit Sum

**Problem ID**: `AtCoder-dp_s`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1750  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_s  
**VJudge Tag**: `[problem:AtCoder-dp_s]`  
**Category File**: [`../categories/dp/digit_dp.md`](../categories/dp/digit_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP with Remainder State`  

---

## 1. Problem Statement & Key Idea
Count positive integers up to K (K <= 10^10000) whose sum of digits is a multiple of D.

**Core Idea**: Process K as a string of up to 10,000 digits. Maintain state (index, remainder_mod_D, tight_flag).

## 2. Core Observation & Invariant
At index i, if tight is True, the next digit can only range from 0 to K[i]. If tight is False, the next digit can range from 0 to 9 freely.

## 3. Step-by-Step Algorithm
1. dp[index][rem][tight]: count of valid prefix configurations.
2. For each digit d in 0..(tight ? K[idx] : 9): dp[idx+1][(rem + d) % D][tight and (d == K[idx])] += dp[idx][rem][tight].
3. Final count = (dp[len][0][0] + dp[len][0][1] - 1 + MOD) % MOD.

## 4. Complexity Analysis
Time: O(|K| * D * 10), Space: O(|K| * D).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int dp[10005][105][2];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string K;
    int D;
    if (!(cin >> K >> D)) return 0;

    int n = K.size();
    dp[0][0][1] = 1;

    for (int i = 0; i < n; ++i) {
        int limit = K[i] - '0';
        for (int rem = 0; rem < D; ++rem) {
            for (int tight = 0; tight < 2; ++tight) {
                if (dp[i][rem][tight] == 0) continue;
                int max_digit = tight ? limit : 9;
                for (int d = 0; d <= max_digit; ++d) {
                    int next_rem = (rem + d) % D;
                    int next_tight = tight && (d == limit);
                    dp[i + 1][next_rem][next_tight] = (dp[i + 1][next_rem][next_tight] + dp[i][rem][tight]) % MOD;
                }
            }
        }
    }

    int ans = (dp[n][0][0] + dp[n][0][1] - 1 + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Textbook Digit DP with tight bound tracking.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Digit-by-digit construction, tight prefix bound handling, and large integer parsing.
- **Reusable Pattern**: `Standard Digit DP state tuple (index, remainder, is_tight).`

---
Back to [Digit DP with Remainder State](../categories/dp/digit_dp.md) | [Categories Directory](../categories/README.md)