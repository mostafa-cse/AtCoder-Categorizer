# Problem Analysis: AtCoder-arc110_d — Binomial Coefficient is Fun

**Problem ID**: `AtCoder-arc110_d`  
**Contest**: `arc110`  
**Rating / Difficulty**: 2075  
**URL**: https://atcoder.jp/contests/arc110/tasks/arc110_d  
**VJudge Tag**: `[problem:AtCoder-arc110_d]`  
**Category File**: [`../categories/basics/stars_and_bars_product_binomial_bijection.md`](../categories/basics/stars_and_bars_product_binomial_bijection.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Stars and Bars`  

---

## 1. Problem Statement & Key Idea
Given a sequence A = (A_1, A_2, ..., A_N) and an integer M, calculate the sum of prod_{i=1}^N binom(B_i, A_i) over all non-negative integer sequences B of length N such that sum_{i=1}^N B_i <= M, modulo 10^9 + 7.

**Key Insight**: Consider a row of M balls. Let S = sum_{i=1}^N A_i. The product prod binom(B_i, A_i) asks us to partition a prefix of length sum B_i <= M into N segments of lengths B_1, ..., B_N, and choose A_i items from the i-th segment. By introducing a slack variable B_{N+1} = M - sum B_i, this corresponds to partitioning M items into N+1 bins and choosing A_i items from bin i (for 1 <= i <= N). This is combinatorially isomorphic to choosing N delimiters and S chosen elements from a total sequence of M + N positions! Therefore, the entire sum collapses into a single binomial coefficient: binom(M + N, S + N).

## 2. Core Observation & Invariant
Sums of products of binomial coefficients over partition configurations collapse to a single global choice via stars-and-bars bijection.

## 3. Step-by-Step Algorithm
1. Compute S = sum_{i=1}^N A_i.
2. If S > M, output 0.
3. The answer is binom(M + N, S + N) modulo 10^9 + 7.
4. Since S + N <= 4 * 10^6 and M <= 10^9, compute binom(M + N, S + N) in O(S + N) using modular inverse.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + sum A_i)`
- **Space Complexity**: `O(1)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Combinatorial bijection collapsing multivariable binomial convolutions into single stars-and-bars choices.
- **Reusable Pattern**: sum_{sum B_i <= M} prod binom(B_i, A_i) = binom(M + N, N + sum A_i).

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

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

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    long long sumA = 0;
    for (int i = 0; i < n; ++i) {
        long long a;
        cin >> a;
        sumA += a;
    }

    if (sumA > m) {
        cout << 0 << "\n";
        return 0;
    }

    long long top = n + m;
    long long k = sumA + n;

    long long num = 1, den = 1;
    for (long long i = 0; i < k; ++i) {
        num = (num * ((top - i) % MOD)) % MOD;
        den = (den * ((i + 1) % MOD)) % MOD;
    }

    long long ans = (num * modInverse(den)) % MOD;
    cout << ans << "\n";

    return 0;
}
```
