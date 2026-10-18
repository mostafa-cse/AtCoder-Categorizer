# Problem Analysis: AtCoder-dwacon6th_prelims_c — C. Cookie Distribution

**Problem ID**: `AtCoder-dwacon6th_prelims_c`  
**Contest**: `dwacon6th-prelims`  
**Rating / Difficulty**: 2618  
**URL**: https://atcoder.jp/contests/dwacon6th-prelims/tasks/dwacon6th_prelims_c  
**VJudge Tag**: `[problem:AtCoder-dwacon6th_prelims_c]`  
**Category File**: [`../categories/combinatorics/cookie_distribution_product_trick.md`](../categories/combinatorics/cookie_distribution_product_trick.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Product Trick`  

---

## 1. Problem Statement & Key Idea
In K days, give cookies to a_i children among N. Happiness is the product of cookies received prod c_j. Find the expected happiness multiplied by prod binom(N, a_i) modulo 10^9+7.

## 2. Core Observation & Invariant
Product Trick: each child independently chooses one day they received a cookie. This completely decouples days into choosing cnt[i] children per day with weight W_i(c) = 1/c! * binom(N - c, a_i - c). The total answer is N! times the coefficient of x^N in prod_{i=1}^K (sum_c W_i(c) x^c).

## 3. Step-by-Step Algorithm
1. Compute polynomial DP multiplying K factors of degree <= N.
2. DP state: dp[s] is sum of weights for chosen children.
3. For each day a_i, transition dp[s + c] += dp[s] * W_i(c).
4. Multiply dp[N] by N! modulo 10^9+7.

## 4. Complexity Analysis
- **Time Complexity**: `O(K * N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 1000000007;

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

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    vector<int> A(K);
    for (int i = 0; i < K; ++i) {
        cin >> A[i];
    }

    int MAX = N + 5;
    vector<long long> fact(MAX, 1), inv(MAX, 1);
    for (int i = 1; i < MAX; ++i) fact[i] = fact[i - 1] * i % MOD;
    inv[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 0; --i) inv[i] = inv[i + 1] * (i + 1) % MOD;

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    vector<long long> dp(N + 1, 0);
    dp[0] = 1;

    for (int a : A) {
        vector<long long> new_dp(N + 1, 0);
        vector<long long> weights(a + 1, 0);
        for (int c = 0; c <= a; ++c) {
            weights[c] = inv[c] * nCr(N - c, a - c) % MOD;
        }

        for (int s = 0; s <= N; ++s) {
            if (dp[s] == 0) continue;
            int limit = min(a, N - s);
            for (int c = 0; c <= limit; ++c) {
                new_dp[s + c] = (new_dp[s + c] + dp[s] * weights[c]) % MOD;
            }
        }
        dp = move(new_dp);
    }

    long long ans = dp[N] * fact[N] % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
