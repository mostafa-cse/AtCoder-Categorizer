# Problem Analysis: AtCoder-abc208_f — F - Cumulative Sum

**Problem ID**: `AtCoder-abc208_f`  
**Contest**: `abc208`  
**Rating / Difficulty**: 2772  
**URL**: https://atcoder.jp/contests/abc208/tasks/abc208_f  
**VJudge Tag**: `[problem:AtCoder-abc208_f]`  
**Category File**: [`../categories/math/grid_cumulative_sum_lagrange_interpolation.md`](../categories/math/grid_cumulative_sum_lagrange_interpolation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Lagrange Interpolation`  

---

## 1. Problem Statement & Key Idea
Given N, M, K, define sequence A^(0)_i = i^K for 0 <= i <= N. For j >= 1, A^(j)_i = sum_{p=0}^i A^(j-1)_p. Compute A^(M)_N mod (10^9 + 7) for N <= 10^18, M <= 30, K <= 2 * 10^6.

## 2. Core Observation & Invariant
Taking prefix sums of a polynomial sequence increases the polynomial degree by 1. Since A^(0)_i = i^K has degree K, the M-th cumulative sum sequence A^(M)_i is a polynomial in i of degree D = K + M. For any polynomial of degree D, its values at any point N can be recovered from its evaluations at D + 1 points using Lagrange interpolation. We can compute A^(0)_i for i = 0..D in O(D) time using a linear sieve for i^K, perform M prefix sum passes in O(M * D) time, and evaluate at N using O(D) Lagrange interpolation.

## 3. Step-by-Step Algorithm
1. 1. Set degree D = K + M. If N <= D, compute directly and output A^(M)_N.
2. 2. Compute i^K for i = 0..D in O(D) time via linear sieve.
3. 3. Compute M cumulative sum passes in-place on array f of size D + 1.
4. 4. Precompute factorials and inverse factorials up to D, as well as prefix and suffix products of (N - i) mod (10^9 + 7).
5. 5. Apply Lagrange interpolation formula:
6.    P(N) = sum_{i=0}^D f[i] * [prod_{j != i} (N - j)] / [prod_{j != i} (i - j)].
7. 6. Return P(N) mod (10^9 + 7).

## 4. Complexity Analysis
- **Time Complexity**: `O(D + M * D) = O((K + M) * M)`
- **Space Complexity**: `O(K + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 1000000007;

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

    long long N;
    int M;
    int K;
    if (!(cin >> N >> M >> K)) return 0;

    int D = K + M;
    if (N == 0) {
        cout << 0 << "\n";
        return 0;
    }

    // Linear sieve to compute i^K for i = 1..D
    vector<int> f(D + 1, 0);
    vector<int> primes;
    primes.reserve(D / 10);
    vector<bool> is_prime(D + 1, true);

    f[0] = 0;
    if (D >= 1) f[1] = 1;
    for (int i = 2; i <= D; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
            f[i] = power(i, K);
        }
        for (int p : primes) {
            if (i * 1LL * p > D) break;
            is_prime[i * p] = false;
            f[i * p] = (long long)f[i] * f[p] % MOD;
            if (i % p == 0) break;
        }
    }

    // Now compute f(n, M) for n = 0..D
    for (int step = 1; step <= M; ++step) {
        long long cur = 0;
        for (int i = 1; i <= D; ++i) {
            cur += f[i];
            if (cur >= MOD) cur -= MOD;
            f[i] = cur;
        }
    }

    if (N <= D) {
        cout << f[N] << "\n";
        return 0;
    }

    // Lagrange interpolation at N
    // P(x) = sum_{i=0}^D f[i] * prod_{j!=i} (x - j) / prod_{j!=i} (i - j)
    vector<long long> fact(D + 1), invFact(D + 1);
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i <= D; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[D] = modInverse(fact[D]);
    for (int i = D - 1; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }

    vector<long long> pref(D + 2, 1);
    vector<long long> suff(D + 2, 1);
    long long n_mod = N % MOD;

    for (int i = 0; i <= D; ++i) {
        long long diff = (n_mod - i + MOD) % MOD;
        pref[i + 1] = (pref[i] * diff) % MOD;
    }
    for (int i = D; i >= 0; --i) {
        long long diff = (n_mod - i + MOD) % MOD;
        suff[i] = (suff[i + 1] * diff) % MOD;
    }

    long long ans = 0;
    for (int i = 0; i <= D; ++i) {
        if (f[i] == 0) continue;
        long long num = (pref[i] * suff[i + 1]) % MOD;
        long long den = (invFact[i] * invFact[D - i]) % MOD;
        long long term = (f[i] * num) % MOD;
        term = (term * den) % MOD;
        if ((D - i) % 2 == 1) {
            ans = (ans - term + MOD) % MOD;
        } else {
            ans = (ans + term) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
