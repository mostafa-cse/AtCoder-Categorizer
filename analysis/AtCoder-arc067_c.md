# Problem Analysis: AtCoder-arc067_c — E. Grouping

**Problem ID**: `AtCoder-arc067_c`  
**Contest**: `arc067`  
**Rating / Difficulty**: 2190  
**URL**: https://atcoder.jp/contests/arc067/tasks/arc067_c  
**VJudge Tag**: `[problem:AtCoder-arc067_c]`  
**Category File**: [`../categories/dp/group_size_partition_knapsack_dp.md`](../categories/dp/group_size_partition_knapsack_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Count ways to partition N people into groups of sizes s in [A, B] where group count k is either 0 or in [C, D]. Using exponential generating functions (dividing DP by j!), adding k groups of size s contributes coeff = 1 / ((s!)^k k!) to transition E[j + k*s] += E[j] * coeff in O(N^2 log N) total time.

## 2. Core Observation & Invariant
Choosing k groups of size s from k*s elements has (k*s)! / ((s!)^k k!) ways. Factoring out (k*s)! aligns with dividing states by j!, allowing knapsack-style DP over group sizes without combinatorial overcounting.

## 3. Step-by-Step Algorithm
1. Precompute factorials and inverse factorials up to N.
2. Initialize dp[0] = 1, all other dp[j] = 0.
3. For each group size s from A to B:
4.   Copy dp to next_dp (k = 0).
5.   For each k from C to min(D, N / s):
6.     Compute coeff = (invFact[s]^k * invFact[k]) % MOD.
7.     For each j with j + k*s <= N: next_dp[j + k*s] = (next_dp[j + k*s] + dp[j] * coeff) % MOD.
8.   Set dp = next_dp.
9. Output (dp[N] * fact[N]) % MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, A, B, C, D;
    if (!(cin >> N >> A >> B >> C >> D)) return 0;

    vector<long long> fact(N + 1, 1), invFact(N + 1, 1);
    for (int i = 1; i <= N; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }

    // dp[j] is the coefficient such that actual answer is dp[N] * fact[N] % MOD
    vector<long long> dp(N + 1, 0);
    dp[0] = 1;

    for (int s = A; s <= B; ++s) {
        vector<long long> next_dp = dp; // k = 0
        long long inv_s_fact = invFact[s];
        
        // Precompute (inv_s_fact)^k * invFact[k]
        // k starts at C up to min(D, N / s)
        int max_k = min(D, N / s);
        if (C <= max_k) {
            long long inv_s_pow = power(inv_s_fact, C);
            for (int k = C; k <= max_k; ++k) {
                long long coeff = (inv_s_pow * invFact[k]) % MOD;
                int shift = k * s;
                for (int j = 0; j + shift <= N; ++j) {
                    if (dp[j]) {
                        next_dp[j + shift] = (next_dp[j + shift] + dp[j] * coeff) % MOD;
                    }
                }
                inv_s_pow = (inv_s_pow * inv_s_fact) % MOD;
            }
        }
        dp = move(next_dp);
    }

    long long ans = (dp[N] * fact[N]) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
