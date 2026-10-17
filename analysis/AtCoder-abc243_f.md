# Problem Analysis: AtCoder-abc243_f — Lottery

**Problem ID**: `AtCoder-abc243_f`  
**Contest**: `abc243`  
**Rating / Difficulty**: 2125  
**URL**: https://atcoder.jp/contests/abc243/tasks/abc243_f  
**VJudge Tag**: `[problem:AtCoder-abc243_f]`  
**Category File**: [`../categories/dynamic_programming/multinomial_prize_distribution_dp.md`](../categories/dynamic_programming/multinomial_prize_distribution_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
There are N prizes, with prize i chosen with probability p_i = W_i / sum W. In K draws, find the probability of obtaining exactly M distinct prizes modulo 998244353.

**Key Insight**: The probability of drawing prize i exactly c_i times is K! * prod_{i=1}^N (p_i^{c_i} / c_i!). To count states with exactly M non-zero counts c_i and sum c_i = K, we define dp[cnt][drawn] = sum of prod (p_i^{c_i} / c_i!) using cnt distinct prizes and drawn total draws. At prize i, we either skip it (c = 0), or pick c in [1, K - drawn] items, multiplying by p_i^c / c!. Finally, multiply dp[M][K] by K!.

## 2. Core Observation & Invariant
Multinomial coupon distribution probabilities factor into independent polynomial weight terms p_i^c / c!, solved via knapsack-style DP.

## 3. Step-by-Step Algorithm
1. Compute normalized probabilities p_i = W_i * inv(sum W) mod MOD.
2. Initialize dp[0][0] = 1.
3. For each prize i from 1 to N:
4.   For cnt from M-1 down to 0:
5.     For drawn from K-1 down to 0:
6.       For c from 1 to K - drawn:
7.         dp[cnt + 1][drawn + c] += dp[cnt][drawn] * (p_i^c / c!).
8. Output dp[M][K] * K! mod MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M * K^2)`
- **Space Complexity**: `O(M * K)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Multinomial coefficient factorization and knapsack DP for coupon collector probabilities.
- **Reusable Pattern**: Multinomial probability distributions computed via DP maintaining (distinct_categories, total_items) with factorials factored out.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<long long> w(n);
    long long sum_w = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i];
        sum_w = (sum_w + w[i]) % MOD;
    }

    long long inv_sum = modInverse(sum_w);
    vector<long long> p(n);
    for (int i = 0; i < n; ++i) {
        p[i] = (w[i] * inv_sum) % MOD;
    }

    vector<long long> fact(k + 1, 1), invFact(k + 1, 1);
    for (int i = 1; i <= k; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[k] = modInverse(fact[k]);
    for (int i = k - 1; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;

    vector<vector<long long>> dp(m + 1, vector<long long>(k + 1, 0));
    dp[0][0] = 1;

    for (int i = 0; i < n; ++i) {
        vector<vector<long long>> next_dp = dp;
        for (int cnt = 0; cnt < m; ++cnt) {
            for (int drawn = 0; drawn < k; ++drawn) {
                if (!dp[cnt][drawn]) continue;

                long long p_pow = p[i];
                for (int c = 1; drawn + c <= k; ++c) {
                    long long term = (p_pow * invFact[c]) % MOD;
                    next_dp[cnt + 1][drawn + c] = (next_dp[cnt + 1][drawn + c] + dp[cnt][drawn] * term) % MOD;
                    p_pow = (p_pow * p[i]) % MOD;
                }
            }
        }
        dp = next_dp;
    }

    long long ans = (dp[m][k] * fact[k]) % MOD;
    cout << ans << "\n";
    return 0;
}
```
