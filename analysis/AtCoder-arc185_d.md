# Problem Analysis: AtCoder-arc185_d — Random Walk on Tree

**Problem ID**: `AtCoder-arc185_d`  
**Contest**: `arc185`  
**Rating / Difficulty**: 2649  
**URL**: https://atcoder.jp/contests/arc185/tasks/arc185_d  
**VJudge Tag**: `[problem:AtCoder-arc185_d]`  
**Category File**: [`../categories/math/random_walk_tree_expected_visits.md`](../categories/math/random_walk_tree_expected_visits.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
The expected cover time for a random walk on a symmetric star graph with N branches of length M reduces via Markov chain linearity, gambler's ruin, and coupon collector's harmonic numbers to the exact closed form: M^2 * (2N * H_N - 1) modulo 998244353.

## 2. Core Observation & Invariant
Each branch behaves as a 1D random walk with reflecting/absorbing boundaries. The central hub is visited between branch explorations. By analyzing the expected time to explore a new branch conditioned on having already visited k distinct branches, the total expected time decomposes into branch traversal times and the coupon collector waiting time (harmonic numbers H_N = sum_{i=1}^N 1/i). The overall expected number of steps until every vertex is visited evaluates cleanly to M^2 * (2N * H_N - 1).

## 3. Step-by-Step Algorithm
1. 1. Compute the N-th harmonic number H_N = sum_{i=1}^N i^(-1) mod 998244353 in O(N) using linear modular inverses.
2. 2. Compute term = (2 * N * H_N - 1) mod 998244353.
3. 3. Multiply by M^2 modulo 998244353.
4. 4. Output the result.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, M;
    if (!(cin >> N >> M)) return 0;

    // Linear sieve / precomputation of modular inverses to compute H_N in O(N)
    // inv[i] = -(MOD / i) * inv[MOD % i] mod MOD
    long long H_N = 0;
    long long inv_cur = 0;
    // We can compute inv on the fly or with linear array
    // Since N <= 200000, linear array or linear inverse takes < 0.01s
    vector<long long> inv(N + 1, 0);
    inv[1] = 1;
    H_N = 1;
    for (int i = 2; i <= N; ++i) {
        inv[i] = (MOD - (MOD / i)) * inv[MOD % i] % MOD;
        H_N = (H_N + inv[i]) % MOD;
    }

    // Expected cover time = M^2 * (2 * N * H_N - 1) mod MOD
    long long M_sq = (M % MOD) * (M % MOD) % MOD;
    long long inner = (2 * (N % MOD) % MOD * H_N - 1 + MOD) % MOD;
    long long ans = (M_sq * inner) % MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
