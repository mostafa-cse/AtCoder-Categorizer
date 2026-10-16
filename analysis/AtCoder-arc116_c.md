# Problem Analysis: AtCoder-arc116_c — Multiple Sequences

**Problem ID**: `AtCoder-arc116_c`  
**Contest**: `arc116`  
**Rating / Difficulty**: 1468  
**URL**: https://atcoder.jp/contests/arc116/tasks/arc116_c  
**VJudge Tag**: `[problem:AtCoder-arc116_c]`  
**Category File**: [`../categories/number_theory/prime_factorization_stars_and_bars.md`](../categories/number_theory/prime_factorization_stars_and_bars.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Prime Factorization`  
- **Topic (Skill)**: `Prime Factorization Combinatorics / Stars and Bars`  

---

## 1. Problem Statement & Key Idea
Find the number of integer sequences A of length N such that 1 <= A_1 <= ... <= A_N <= M and A_{i+1} is a multiple of A_i, modulo 998244353.

**Key Insight**: Iterate over the last element x = A_N (1 <= x <= M). For each prime factor p^e dividing x, the e prime factors must be distributed across the N positions in the sequence, which is independent for each prime.

## 2. Core Observation & Invariant
Distributing e factors across N non-decreasing transitions corresponds to weak compositions of e into N non-negative integers: C(e + N - 1, N - 1). For x = prod p_i^{e_i}, total sequences ending at x is prod_i C(e_i + N - 1, N - 1).

## 3. Step-by-Step Algorithm
1. Precompute combinations C(n, r) modulo 998244353.
2. Precompute smallest prime factor (SPF) up to M using a sieve in O(M).
3. ans = 0.
4. For x from 1 to M:
5.   Factorize x using SPF into prime powers p_i^{e_i}.
6.   ways = 1.
7.   For each exponent e_i: ways = ways * C(e_i + N - 1, N - 1) % MOD.
8.   ans = (ans + ways) % MOD.
9. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(M log M)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;
const int MAX = 300005;

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

    int n, m;
    if (!(cin >> n >> m)) return 0;

    // Sieve for SPF
    vector<int> spf(m + 1);
    for (int i = 1; i <= m; ++i) spf[i] = i;
    for (int i = 2; i * i <= m; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= m; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }

    long long total_ans = 0;
    for (int x = 1; x <= m; ++x) {
        int temp = x;
        long long ways = 1;
        while (temp > 1) {
            int p = spf[temp];
            int e = 0;
            while (temp % p == 0) {
                e++;
                temp /= p;
            }
            ways = (ways * nCr(e + n - 1, n - 1)) % MOD;
        }
        total_ans = (total_ans + ways) % MOD;
    }

    cout << total_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining prime factorization multi-set distribution with Stars and Bars combinatorics.
- **Reusable Pattern**: `Divisibility Chain Counting: prod_{p|x} C(exponent + N - 1, N - 1).`
