# Problem Analysis: AtCoder-abc135_d — Digits Parade

**Problem ID**: `AtCoder-abc135_d`  
**Contest**: `abc135`  
**Rating / Difficulty**: 1334  
**URL**: https://atcoder.jp/contests/abc135/tasks/abc135_d  
**VJudge Tag**: `[problem:AtCoder-abc135_d]`  
**Category File**: [`../categories/dp/digit_dp_modulo_13.md`](../categories/dp/digit_dp_modulo_13.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP Modulo 13`  

---

## 1. Problem Statement & Key Idea
Given a string S containing digits and '?'. Replace each '?' with a digit 0..9 such that the resulting integer equals 5 modulo 13. Count valid integers modulo 10^9 + 7.

**Key Idea**: Process digits from left to right, maintaining remainder modulo 13.

## 2. Core Observation & Invariant
Let dp[r] be the number of ways to form a prefix whose value is r modulo 13. Base case: dp[0] = 1. When appending digit d, remainder transitions from r to (r * 10 + d) % 13. If S[i] is a fixed digit d, only that transition is used; if '?', branch over all d in 0..9. Final answer is dp[5].

## 3. Step-by-Step Algorithm
1. Initialize dp array of size 13 to 0; dp[0] = 1.
2. For each character c in S:
3.   Initialize next_dp of size 13 to 0.
4.   If c == '?': for d in 0..9, for r in 0..12: next_dp[(r * 10 + d) % 13] += dp[r].
5.   Else: let d = c - '0'; for r in 0..12: next_dp[(r * 10 + d) % 13] += dp[r].
6.   Take modulo 10^9 + 7, dp = next_dp.
7. Output dp[5].

## 4. Complexity Analysis
- **Time Complexity**: `O(|S| * 13 * 10)`
- **Space Complexity**: `O(13)`

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

    string s;
    if (!(cin >> s)) return 0;

    vector<long long> dp(13, 0);
    dp[0] = 1;

    for (char c : s) {
        vector<long long> next_dp(13, 0);
        if (c == '?') {
            for (int d = 0; d <= 9; ++d) {
                for (int r = 0; r < 13; ++r) {
                    int nr = (r * 10 + d) % 13;
                    next_dp[nr] = (next_dp[nr] + dp[r]) % MOD;
                }
            }
        } else {
            int d = c - '0';
            for (int r = 0; r < 13; ++r) {
                int nr = (r * 10 + d) % 13;
                next_dp[nr] = (next_dp[nr] + dp[r]) % MOD;
            }
        }
        dp = move(next_dp);
    }

    cout << dp[5] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Digit DP state transition over modular equivalence classes.
- **Reusable Pattern**: `Digit modulo DP: next_dp[(r * 10 + d) % M] = (next_dp + dp[r]) % MOD.`
