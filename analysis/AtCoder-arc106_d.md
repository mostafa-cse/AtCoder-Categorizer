# Problem Analysis: AtCoder-arc106_d — Powers

**Problem ID**: `AtCoder-arc106_d`  
**Contest**: `arc106`  
**Rating / Difficulty**: 1988  
**URL**: https://atcoder.jp/contests/arc106/tasks/arc106_d  
**VJudge Tag**: `[problem:AtCoder-arc106_d]`  
**Category File**: [`../categories/math/binomial_expansion_power_sum_moments.md`](../categories/math/binomial_expansion_power_sum_moments.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomials / Binomial Theorem`  
- **Topic (Skill)**: `Binomial Expansion Decoupling of Pairwise Sum Powers via Power-Sum Moments`  

---

## 1. Problem Statement & Key Idea
Given array A of length N. For each X from 1 to K (K <= 300), compute sum_{1 <= i < j <= N} (A_i + A_j)^X modulo 998244353.

By Binomial Theorem, (A_i + A_j)^X = sum_{p=0}^X binom(X, p) A_i^p A_j^{X-p}. Summing over all 1 <= i, j <= N decouples the pair sum into products of independent power sums: sum_{i, j} (A_i + A_j)^X = sum_{p=0}^X binom(X, p) (sum A_i^p) (sum A_j^{X-p}) = sum_{p=0}^X binom(X, p) S_p S_{X-p}, where S_p = sum_{i=1}^N A_i^p mod 998244353. Precompute S_0..S_K in O(N K). For each X, subtract the self-pairs sum_{i=1}^N (2 A_i)^X = 2^X S_X and divide by 2.

## 2. Core Observation & Invariant
Binomial theorem decouples coupled pairwise powers (A_i + A_j)^X into 1D power-sum moments.

## 3. Step-by-Step Algorithm
1. Precompute factorials and powers of A_i up to K.
2. Compute power sums S_p = sum_{i=1}^N A_i^p % MOD for 0 <= p <= K.
3. For each X = 1..K:
4.   total = sum_{p=0}^X binom(X, p) * S_p * S_{X - p} % MOD.
5.   self_sum = 2^X * S_X % MOD.
6.   ans = (total - self_sum + MOD) * inv(2) % MOD.
7.   Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * K + K^2)`
- **Space Complexity**: `O(N + K)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
const int MAXK = 305;

long long fact[MAXK], invFact[MAXK];

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

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAXK; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAXK - 1] = modInverse(fact[MAXK - 1]);
    for (int i = MAXK - 2; i >= 1; i--) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<long long> S(k + 1, 0);
    for (int i = 0; i < n; ++i) {
        long long cur = 1;
        for (int p = 0; p <= k; ++p) {
            S[p] = (S[p] + cur) % MOD;
            cur = (cur * a[i]) % MOD;
        }
    }

    long long inv2 = modInverse(2);

    for (int x = 1; x <= k; ++x) {
        long long total = 0;
        for (int p = 0; p <= x; ++p) {
            long long ways = nCr(x, p);
            long long term = ways * S[p] % MOD * S[x - p] % MOD;
            total = (total + term) % MOD;
        }

        long long self_term = power(2, x) * S[x] % MOD;
        long long ans = (total - self_term + MOD) % MOD * inv2 % MOD;
        cout << ans << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Binomial expansion for axis decoupling in symmetric polynomial power sums.
- **Reusable Pattern**: `Pairwise Power Sums: sum_{i<j} (A_i + A_j)^X = 1/2 [sum_{p=0}^X binom(X, p) S_p S_{X-p} - 2^X S_X].`
