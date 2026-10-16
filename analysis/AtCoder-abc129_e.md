# Problem Analysis: AtCoder-abc129_e — Sum Equals Xor

**Problem ID**: `AtCoder-abc129_e`  
**Contest**: `abc129`  
**Rating / Difficulty**: 1547  
**URL**: https://atcoder.jp/contests/abc129/tasks/abc129_e  
**VJudge Tag**: `[problem:AtCoder-abc129_e]`  
**Category File**: [`../categories/dp/digit_dp_disjoint_bits_sum_xor.md`](../categories/dp/digit_dp_disjoint_bits_sum_xor.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP on Bitwise Condition a + b = a ^ b (Disjoint Bits)`  

---

## 1. Problem Statement & Key Idea
Given an integer N in binary (length up to 10^5). Count pairs of non-negative integers (a, b) such that a + b <= N and a + b = a ^ b, modulo 10^9 + 7.

**Key Insight**: a + b = a ^ b holds iff a AND b = 0 (no carry in binary addition). At each bit position, the pair of bits (a_bit, b_bit) can be (0, 0) [1 choice, sum bit 0], or (1, 0) / (0, 1) [2 choices, sum bit 1].

## 2. Core Observation & Invariant
Digit DP on binary string L: `dp[i][less]` where less is boolean. At position i: if sum bit is 0 (1 choice), next_less = less || (L[i] == '1'). If sum bit is 1 (2 choices), valid only if less || (L[i] == '1').

## 3. Step-by-Step Algorithm
1. dp[0] = 1 (equal to prefix), dp[1] = 0 (strictly less).
2. For each character c in L:
3.   next_0 = 0, next_1 = 0.
4.   If c == '1':
5.     next_0 = (2LL * dp[0]) % MOD; // choose sum bit 1, stays equal
6.     next_1 = (dp[0] + 3LL * dp[1]) % MOD; // choose sum bit 0 (becomes less) or extend less with 3 choices
7.   Else (c == '0'):
8.     next_0 = dp[0]; // choose sum bit 0, stays equal
9.     next_1 = (3LL * dp[1]) % MOD; // extend less with 3 choices
10.   dp[0] = next_0, dp[1] = next_1.
11. Print (dp[0] + dp[1]) % MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(|L|)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string L;
    if (!(cin >> L)) return 0;

    long long dp_eq = 1, dp_less = 0;

    for (char c : L) {
        long long next_eq = 0, next_less = 0;
        if (c == '1') {
            // Choice 1: sum bit = 1 (2 choices: (1,0) or (0,1)), stays equal
            next_eq = (dp_eq * 2) % MOD;
            // Choice 2: sum bit = 0 (1 choice: (0,0)), transitions from equal to less
            // Plus all 3 choices for existing less
            next_less = (dp_eq + dp_less * 3) % MOD;
        } else {
            // Choice 1: sum bit = 0 (1 choice: (0,0)), stays equal
            next_eq = dp_eq;
            // Choice 2: all 3 choices for existing less
            next_less = (dp_less * 3) % MOD;
        }
        dp_eq = next_eq;
        dp_less = next_less;
    }

    cout << (dp_eq + dp_less) % MOD << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Digit DP state transition encoding over carry-free bitwise constraints.
- **Reusable Pattern**: `Sum Equals XOR Digit DP: 1 choice for bit 0, 2 choices for bit 1, 3 total branch choices.`
