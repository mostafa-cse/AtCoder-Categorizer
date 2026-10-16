# Problem Analysis: AtCoder-abc110_d — Factorization

**Problem ID**: `AtCoder-abc110_d`  
**Contest**: `abc110`  
**Rating / Difficulty**: 1695  
**URL**: https://atcoder.jp/contests/abc110/tasks/abc110_d  
**VJudge Tag**: `[problem:AtCoder-abc110_d]`  
**Category File**: [`../categories/number_theory/prime_factorization_stars_and_bars_factorization.md`](../categories/number_theory/prime_factorization_stars_and_bars_factorization.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Prime Factorization`  
- **Topic (Skill)**: `Prime Factorization + Stars and Bars on Exponents`  

---

## 1. Problem Statement & Key Idea
Given N and M. Find the number of sequences of N positive integers (a_1, ..., a_N) such that a_1 * a_2 * ... * a_N = M, modulo 10^9 + 7.

**Key Insight**: Prime factorize M = prod p_i^{e_i}. Because prime factorizations are unique, the exponent e_i of each prime p_i must be distributed across the N variables independently.

## 2. Core Observation & Invariant
Distributing e_i identical prime factors among N variables corresponds to weak compositions of e_i into N parts: Stars and Bars C(e_i + N - 1, N - 1). The total sequences is prod_i C(e_i + N - 1, N - 1) modulo 10^9 + 7.

## 3. Step-by-Step Algorithm
1. Factorize M in O(sqrt(M)) into prime powers p_i^{e_i}.
2. Precompute factorials and inverse factorials up to N + 100.
3. ans = 1.
4. For each prime power with exponent e_i:
5.   ans = (ans * nCr(e_i + N - 1, N - 1)) % MOD.
6. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(sqrt(M) + log(MOD))`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
const int MAX = 200005;

long long fact[MAX], invFact[MAX];

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

void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MAX; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[MAX - 1] = power(fact[MAX - 1], MOD - 2);
    for (int i = MAX - 2; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    long long ans = 1;
    long long temp = m;

    for (long long d = 2; d * d <= temp; ++d) {
        if (temp % d == 0) {
            int e = 0;
            while (temp % d == 0) {
                e++;
                temp /= d;
            }
            ans = (ans * nCr(e + n - 1, n - 1)) % MOD;
        }
    }

    if (temp > 1) {
        ans = (ans * nCr(1 + n - 1, n - 1)) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multiplicative decomposition into independent additive exponent stars and bars.
- **Reusable Pattern**: `Product Factorization Sequences: prod_{p|M} C(e + N - 1, N - 1).`
