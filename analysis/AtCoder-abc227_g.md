# Problem Analysis: AtCoder-abc227_g — Divisors of Binomial Coefficient

**Problem ID**: `AtCoder-abc227_g`  
**Contest**: `abc227`  
**Rating / Difficulty**: 2207  
**URL**: https://atcoder.jp/contests/abc227/tasks/abc227_g  
**VJudge Tag**: `[problem:AtCoder-abc227_g]`  
**Category File**: [`../categories/number_theory/divisors_of_binomial_coefficient_segmented_sieve.md`](../categories/number_theory/divisors_of_binomial_coefficient_segmented_sieve.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Primes and Divisors`  
- **Topic (Skill)**: `Segmented Sieve`  

---

## 1. Problem Statement & Key Idea
Prime factorization of C(N, K) using segmented sieve over numerator interval [N - K + 1, N] and small prime trial division.

## 2. Core Observation & Invariant
C(N, K) = prod_{i=0}^{K-1} (N - i) / K!. Any prime p <= 10^6 divides terms in the interval and in K!, counted via Legendre formula. Any remaining factor > 1 in val[i] after dividing out all primes <= 10^6 must itself be a prime > 10^6, which appears at most once across the interval [N - K + 1, N] since interval length is K <= 10^6.

## 3. Step-by-Step Algorithm
1. 1. Sieve all primes up to 10^6.
2. 2. Initialize array val[0..K-1] with val[i] = N - K + 1 + i.
3. 3. For each prime p <= 10^6:
4.    - Compute exponent in K! via Legendre formula.
5.    - For each multiple of p in [N - K + 1, N], divide out p from val[idx] and accumulate exponent in numerator.
6.    - Multiply answer by (exp_num - exp_den + 1) mod 998244353.
7. 4. For every remaining val[i] > 1, multiply answer by 2 mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(K log log K + sqrt(N))`
- **Space Complexity**: `O(K)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MOD = 998244353;
const int MAX_PRIME = 1000000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll N, K;
    if (!(cin >> N >> K)) return 0;

    if (K == 0) {
        cout << 1 << "\n";
        return 0;
    }

    // Sieve up to MAX_PRIME
    vector<bool> is_prime(MAX_PRIME + 1, true);
    vector<int> primes;
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p <= MAX_PRIME; ++p) {
        if (is_prime[p]) {
            primes.push_back(p);
            for (int j = 2 * p; j <= MAX_PRIME; j += p) {
                is_prime[j] = false;
            }
        }
    }

    // Interval [N - K + 1, N]
    ll L = N - K + 1;
    vector<ll> val(K);
    for (int i = 0; i < K; ++i) {
        val[i] = L + i;
    }

    ll ans = 1;

    for (int p : primes) {
        if (p > N) break;

        // Exponent in K!
        ll exp_den = 0;
        ll temp = K;
        while (temp >= p) {
            exp_den += temp / p;
            temp /= p;
        }

        // Exponent in numerator
        ll exp_num = 0;
        // First multiple of p >= L
        ll start = ((L + p - 1) / p) * p;
        for (ll mult = start; mult <= N; mult += p) {
            int idx = mult - L;
            while (val[idx] % p == 0) {
                val[idx] /= p;
                exp_num++;
            }
        }

        ll e = exp_num - exp_den;
        if (e > 0) {
            ans = (ans * ((e + 1) % MOD)) % MOD;
        }
    }

    // Remaining val[i] > 1 must be prime factors > MAX_PRIME
    for (int i = 0; i < K; ++i) {
        if (val[i] > 1) {
            ans = (ans * 2) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
