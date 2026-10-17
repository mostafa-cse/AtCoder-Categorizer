# Problem Analysis: AtCoder-abc295_e — Kth Number

**Problem ID**: `AtCoder-abc295_e`  
**Contest**: `abc295`  
**Rating / Difficulty**: 2157  
**URL**: https://atcoder.jp/contests/abc295/tasks/abc295_e  
**VJudge Tag**: `[problem:AtCoder-abc295_e]`  
**Category File**: [`../categories/math/tail_sum_expectation_binomial_order_statistics.md`](../categories/math/tail_sum_expectation_binomial_order_statistics.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Sequence A has zeros replaced uniformly at random with integers in 1..M. Compute the expected value of the K-th smallest element of sorted A modulo 998244353 using the tail sum formula E[X] = sum_{x=1}^M P(X >= x).

## 2. Core Observation & Invariant
A_K >= x if and only if the total count of elements strictly less than x is at most K - 1. Fixed non-zero elements contribute a deterministic count C_{< x}. The remaining Z zeros independently land in [1, x-1] with probability p = (x-1)/M. The count of zeros < x follows a Binomial distribution B(Z, p), evaluated in O(Z) per x.

## 3. Step-by-Step Algorithm
1. Count total zeros Z in array A. Precompute factorials and inverses for combinations nCr.
2. For each threshold x from 1 to M, count fixed non-zero elements with A[i] < x (let this be c_less).
3. If c_less > K - 1, P(A_K >= x) = 0.
4. Otherwise, sum the binomial probabilities sum_{j=0}^{min(Z, K - 1 - c_less)} nCr(Z, j) * p^j * (1-p)^{Z-j} where p = (x-1)/M.
5. Accumulate P(A_K >= x) over all x in 1..M modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code (Verified & Clean)
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

const int MAXF = 4005;
long long fact[MAXF], invFact[MAXF];

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAXF; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAXF - 1] = modInverse(fact[MAXF - 1]);
    for (int i = MAXF - 2; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<int> a(n);
    int Z = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] == 0) Z++;
    }

    long long invM = modInverse(m);
    long long total_exp = 0;

    for (int x = 1; x <= m; ++x) {
        int c_less = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] != 0 && a[i] < x) {
                c_less++;
            }
        }

        if (c_less > k - 1) continue;

        int max_j = min(Z, k - 1 - c_less);
        long long p = (1LL * (x - 1) * invM) % MOD;
        long long q_prob = (1LL * (m - x + 1) * invM) % MOD;

        long long p_prob = 0;
        for (int j = 0; j <= max_j; ++j) {
            long long ways = nCr(Z, j);
            long long term = ways * power(p, j) % MOD * power(q_prob, Z - j) % MOD;
            p_prob = (p_prob + term) % MOD;
        }

        total_exp = (total_exp + p_prob) % MOD;
    }

    cout << total_exp << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
