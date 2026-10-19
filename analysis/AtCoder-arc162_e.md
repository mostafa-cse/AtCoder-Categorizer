# Problem Analysis: AtCoder-arc162_e — E - Small Multiple Permutation

**Problem ID**: `AtCoder-arc162_e`  
**Contest**: `arc162`  
**Rating / Difficulty**: 2780  
**URL**: https://atcoder.jp/contests/arc162/tasks/arc162_e  
**VJudge Tag**: `[problem:AtCoder-arc162_e]`  
**Category File**: [`../categories/dynamic_programming_dp/distinct_subsequences_frequency_knapsack_dp.md`](../categories/dynamic_programming_dp/distinct_subsequences_frequency_knapsack_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Given an array A of length N with some elements already fixed and others 0, count the number of completions such that for every value x, its frequency in the completion does not exceed B_x, and the number of elements with frequency >= f satisfies given constraints.

## 2. Core Observation & Invariant
Process frequencies in descending order i = N, N-1, ..., 1. When transitioning from frequency i + 1 to i, decide how many values l will have frequency exactly i. Since each such value contributes i occurrences, the total frequency is bounded by N, meaning at most N / i values can have frequency >= i. The DP state is dp[j][k], where j values have frequency >= i and k total positions are filled. Transitions use combinations for choosing which values and positions receive frequency i, leading to a harmonic DP running in O(N^2 log N).

## 3. Step-by-Step Algorithm
1. 1. Count initial frequencies of fixed elements in A and identify available positions.
2. 2. Precompute factorials and binomial coefficients up to N.
3. 3. Iterate frequency i from N down to 1. State: dp[j][k] = number of valid partial assignments with j values having frequency >= i and k total slots filled.
4. 4. Transition: iterate over l, the number of distinct values assigned frequency exactly i.
5. 5. Multiply by C(available_values - j, l) * multinomial factor for allocating slots.
6. 6. Result is dp[total_values][N] modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long MOD = 998244353;

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

    int N;
    if (!(cin >> N)) return 0;

    vector<int> A(N);
    vector<int> C_cnt(N + 2, 0);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        if (A[i] <= N) C_cnt[A[i]]++;
        else C_cnt[N]++;
    }

    for (int i = N; i >= 1; --i) {
        C_cnt[i] += C_cnt[i + 1];
    }

    int max_fact = N + 5;
    vector<long long> fact(max_fact, 1), inv(max_fact, 1);
    for (int i = 1; i < max_fact; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv[max_fact - 1] = modInverse(fact[max_fact - 1]);
    for (int i = max_fact - 2; i >= 0; --i) {
        inv[i] = (inv[i + 1] * (i + 1)) % MOD;
    }

    auto C = [&](int n, int k) -> long long {
        if (k < 0 || k > n) return 0;
        return fact[n] * inv[k] % MOD * inv[n - k] % MOD;
    };

    // dp[j][k]: j distinct values chosen so far, k total elements placed
    vector<vector<int>> dp(N + 1, vector<int>(N + 1, 0));
    dp[0][0] = 1;

    for (int i = N; i >= 1; --i) {
        if (C_cnt[i] == 0) continue;

        vector<vector<int>> next_dp(N + 1, vector<int>(N + 1, 0));
        long long inv_fact_i = inv[i];

        int max_j = N / (i + 1);

        for (int j = 0; j <= max_j && j <= C_cnt[i]; ++j) {
            for (int k = 0; k <= N; ++k) {
                if (dp[j][k] == 0) continue;

                long long ways = dp[j][k];
                // l = 0
                next_dp[j][k] = (next_dp[j][k] + ways) % MOD;

                int max_l = min(C_cnt[i] - j, (N - k) / i);
                int cur_avail = C_cnt[i] - k;
                long long pow_inv = 1;

                for (int l = 1; l <= max_l; ++l) {
                    if (cur_avail < i * l) break;
                    pow_inv = (pow_inv * inv_fact_i) % MOD;

                    long long comb_val = C(C_cnt[i] - j, l);
                    long long pos_ways = fact[cur_avail] * inv[cur_avail - i * l] % MOD * pow_inv % MOD;
                    long long add_ways = ways * comb_val % MOD * pos_ways % MOD;

                    int nj = j + l;
                    int nk = k + i * l;
                    next_dp[nj][nk] = (next_dp[nj][nk] + add_ways) % MOD;
                }
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int j = 0; j <= N; ++j) {
        ans = (ans + dp[j][N]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
