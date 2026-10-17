# Problem Analysis: AtCoder-arc217_c — C. Greedy Customers 2

**Problem ID**: `AtCoder-arc217_c`  
**Contest**: `arc217`  
**Rating / Difficulty**: 2173  
**URL**: https://atcoder.jp/contests/arc217/tasks/arc217_c  
**VJudge Tag**: `[problem:AtCoder-arc217_c]`  
**Category File**: [`../categories/math/greedy_customers_hall_multinomial_prefix_dp.md`](../categories/math/greedy_customers_hall_multinomial_prefix_dp.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
N customers with random budgets in 1..C greedily purchase the most expensive available item they can afford. By Hall's condition, at least k items are sold iff for each i in 1..k, at least k - i + 1 customers have budget >= A_i. Compute tail probabilities P(>= k) via suffix DP and multinomial transitions, then recover exact probabilities P(k) = P(>= k) - P(>= k + 1).

## 2. Core Observation & Invariant
Sorting items A_1 <= A_2 <= ... <= A_k <= C, customers with budget in [A_i, A_{i+1}-1] are grouped into buckets. DP state dp[j] counts ways to assign budgets to j customers with budget >= A_i satisfying all suffix conditions up to item k. Transitioning from i+1 down to i with multinomial weights (diff)^t / t! solves each k in O(k * N^2) time, totaling O(N^4).

## 3. Step-by-Step Algorithm
1. For each k from 1 to N, calculate the probability P(>= k) that at least k items are purchased.
2. Run DP from i = k down to 1: dp[j] represents ways to distribute budgets such that j people have budget >= A_i, subject to j >= k - i + 1.
3. Transition by adding t people to bucket [A_i, A_{i+1} - 1] weighted by (A_{i+1} - A_i)^t / t!.
4. After bucket 1, multiply by remaining people choosing budgets < A_1, normalize by N! / C^N.
5. Output P(k) = P(>= k) - P(>= k + 1) for all k = 0, ..., N modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^4)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

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

void solve_case() {
    int N;
    long long C;
    cin >> N >> C;
    vector<long long> A(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    sort(A.begin(), A.end());

    vector<long long> fact(N + 1, 1), inv(N + 1, 1);
    for (int i = 1; i <= N; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    long long inv_c_n = power(power(C % MOD, N), MOD - 2);

    vector<long long> P_ge(N + 1, 0);
    P_ge[0] = 1;

    for (int k = 1; k <= N; ++k) {
        vector<long long> dp(N + 1, 0);
        dp[0] = 1;

        for (int i = k; i >= 1; --i) {
            long long p_curr = A[i - 1];
            long long p_next = (i == k ? C + 1 : A[i]);
            long long diff = (p_next - p_curr) % MOD;
            if (diff < 0) diff += MOD;

            vector<long long> term(N + 1, 1);
            for (int t = 1; t <= N; ++t) {
                term[t] = term[t - 1] * diff % MOD * inv[t] % MOD * fact[t - 1] % MOD;
            }

            vector<long long> new_dp(N + 1, 0);
            for (int j = k - i + 1; j <= N; ++j) {
                long long s = 0;
                for (int j_prev = 0; j_prev <= j; ++j_prev) {
                    if (dp[j_prev]) {
                        s = (s + dp[j_prev] * term[j - j_prev]) % MOD;
                    }
                }
                new_dp[j] = s;
            }
            dp = move(new_dp);
        }

        long long diff0 = (A[0] - 1) % MOD;
        if (diff0 < 0) diff0 += MOD;

        vector<long long> term0(N + 1, 1);
        for (int t = 1; t <= N; ++t) {
            term0[t] = term0[t - 1] * diff0 % MOD * inv[t] % MOD * fact[t - 1] % MOD;
        }

        long long total_ways = 0;
        for (int j = k; j <= N; ++j) {
            total_ways = (total_ways + dp[j] * term0[N - j]) % MOD;
        }
        total_ways = total_ways * fact[N] % MOD * inv_c_n % MOD;
        P_ge[k] = total_ways;
    }

    vector<long long> P_eq(N + 1, 0);
    for (int k = 0; k < N; ++k) {
        P_eq[k] = (P_ge[k] - P_ge[k + 1] + MOD) % MOD;
    }
    P_eq[N] = P_ge[N];

    for (int k = 0; k <= N; ++k) {
        cout << P_eq[k] << (k == N ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve_case();
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
