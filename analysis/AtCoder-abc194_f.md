# Problem Analysis: AtCoder-abc194_f — F. Digits Paradise in Hexadecimal

**Problem ID**: `AtCoder-abc194_f`  
**Contest**: `abc194`  
**Rating / Difficulty**: 2197  
**URL**: https://atcoder.jp/contests/abc194/tasks/abc194_f  
**VJudge Tag**: `[problem:AtCoder-abc194_f]`  
**Category File**: [`../categories/dynamic_programming/hexadecimal_distinct_digits_state_compression_digit_dp.md`](../categories/dynamic_programming/hexadecimal_distinct_digits_state_compression_digit_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP`  

---

## 1. Problem Statement & Key Idea
Count integers 1 <= x <= N (length up to 2e5 hex digits) having exactly K distinct hex digits. By digit symmetry, non-tight prefixes only need to track the count c in [0, 16] of distinct digits used so far, reducing non-tight DP to 17 states per position in O(16 * |N|) time.

## 2. Core Observation & Invariant
Once a prefix is strictly less than N, choosing one of the c existing digits maintains count c (c choices), while choosing an unused digit increases count to c + 1 (16 - c choices). The single tight prefix is maintained with a bitmask.

## 3. Step-by-Step Algorithm
1. Maintain dp[c] (count of non-tight prefixes with c distinct digits) and tight_mask.
2. For each digit d = hex(N[i]):
3.   Transition non-tight: next_dp[c] += dp[c] * c, next_dp[c + 1] += dp[c] * (16 - c).
4.   For numbers of fewer digits (i > 0), add 15 to next_dp[1].
5.   Branch tight prefix: for each v < d, add 1 to next_dp[c_tight] or next_dp[c_tight + 1].
6.   Update tight_mask |= (1 << d), dp = next_dp.
7. Add 1 to dp[K] if popcount(tight_mask) == K. Output result modulo 10^9+7.

## 4. Complexity Analysis
- **Time Complexity**: `O(16 * |N|)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int hex_val(char c) {
    if (c >= '0' && c <= '9') return c - '0';
    return c - 'A' + 10;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string N;
    int K;
    if (!(cin >> N >> K)) return 0;

    int L = N.size();

    // dp[c] = number of non-tight, non-zero prefixes having c distinct digits
    vector<long long> dp(17, 0);

    // Tight state tracking
    int tight_mask = 0;

    for (int i = 0; i < L; ++i) {
        int d = hex_val(N[i]);
        vector<long long> next_dp(17, 0);

        // 1. Transitions from non-tight dp
        for (int c = 1; c <= 16; ++c) {
            if (!dp[c]) continue;
            // choose one of the c existing digits
            next_dp[c] = (next_dp[c] + dp[c] * c) % MOD;
            // choose one of the (16 - c) new digits
            if (c + 1 <= 16) {
                next_dp[c + 1] = (next_dp[c + 1] + dp[c] * (16 - c)) % MOD;
            }
        }

        // 2. Numbers with strictly fewer digits starting here (i > 0)
        // Can pick any digit from 1 to 15 as first digit (starts with 1 distinct digit)
        if (i > 0) {
            next_dp[1] = (next_dp[1] + 15) % MOD;
        }

        // 3. Branching from the tight prefix to non-tight
        int c_tight = __builtin_popcount(tight_mask);
        int start_v = (i == 0 ? 1 : 0);
        for (int v = start_v; v < d; ++v) {
            if (tight_mask & (1 << v)) {
                next_dp[c_tight] = (next_dp[c_tight] + 1) % MOD;
            } else {
                next_dp[c_tight + 1] = (next_dp[c_tight + 1] + 1) % MOD;
            }
        }

        // Update tight prefix
        tight_mask |= (1 << d);
        dp = move(next_dp);
    }

    // Finally, check the number N itself (tight state at the end)
    long long ans = dp[K];
    if (__builtin_popcount(tight_mask) == K) {
        ans = (ans + 1) % MOD;
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
