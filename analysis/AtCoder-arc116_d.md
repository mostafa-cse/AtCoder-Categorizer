# Problem Analysis: AtCoder-arc116_d — I Wanna Win The Game

**Problem ID**: `AtCoder-arc116_d`  
**Contest**: `arc116`  
**Rating / Difficulty**: 1718  
**URL**: https://atcoder.jp/contests/arc116/tasks/arc116_d  
**VJudge Tag**: `[problem:AtCoder-arc116_d]`  
**Category File**: [`../categories/dp/bitwise_carry_dp_xor_zero.md`](../categories/dp/bitwise_carry_dp_xor_zero.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Bitwise DP`  
- **Topic (Skill)**: `Bit-by-Bit Carry DP with XOR-Zero Parity Constraint`  

---

## 1. Problem Statement & Key Idea
Count the number of sequences of N non-negative integers A_1, ..., A_N such that A_1 XOR ... XOR A_N = 0 and sum(A_i) = M, modulo 998244353. (N, M <= 5000).

**Key Insight**: The XOR sum is zero if and only if at every bit position b, an even number of elements have the b-th bit set. Process bits from 0 to 12. At bit b, choosing 2j elements to have bit b set contributes 2j * 2^b to the sum.

## 2. Core Observation & Invariant
Transitions: dp[s + 2j * 2^b] = (dp[s + 2j * 2^b] + dp[s] * C(N, 2j)) % MOD. Total operations bounded by sum_{b} (M / 2^b) * (N / 2) ~ N * M ~ 2.5 * 10^7.

## 3. Step-by-Step Algorithm
1. Precompute combinations C(N, k) modulo 998244353.
2. Initialize dp[M + 1] = 0, dp[0] = 1.
3. For bit b = 0 to 12:
4.   weight = 1 << b.
5.   if weight > M: break.
6.   next_dp[M + 1] = 0.
7.   For 2j = 0 to N step 2:
8.     add_val = 2j * weight.
9.     if add_val > M: break.
10.     ways = C(N, 2j).
11.     For s = 0 to M - add_val:
12.       next_dp[s + add_val] = (next_dp[s + add_val] + dp[s] * ways) % MOD.
13.   dp = next_dp.
14. Print dp[M].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<long long>> C(n + 1, vector<long long>(n + 1, 0));
    for (int i = 0; i <= n; ++i) {
        C[i][0] = 1;
        for (int j = 1; j <= i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }

    vector<long long> dp(m + 1, 0);
    dp[0] = 1;

    for (int b = 0; (1 << b) <= m; ++b) {
        int weight = 1 << b;
        vector<long long> next_dp(m + 1, 0);

        for (int j = 0; 2 * j <= n; ++j) {
            int count_set = 2 * j;
            int add = count_set * weight;
            if (add > m) break;
            long long ways = C[n][count_set];

            for (int s = 0; s + add <= m; ++s) {
                if (dp[s] > 0) {
                    next_dp[s + add] = (next_dp[s + add] + dp[s] * ways) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    cout << dp[m] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bit-by-bit dynamic programming with parity constraints and combinatoric coefficient multiplier.
- **Reusable Pattern**: `Bitwise Zero-XOR Sum DP: Iterate bit levels with even subset choice C(N, 2j).`
