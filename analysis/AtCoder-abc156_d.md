# Problem Analysis: AtCoder-abc156_d — Bouquet

**Problem ID**: `AtCoder-abc156_d`  
**Contest**: `abc156`  
**Rating / Difficulty**: 1014  
**URL**: https://atcoder.jp/contests/abc156/tasks/abc156_d  
**VJudge Tag**: `[problem:AtCoder-abc156_d]`  
**Category File**: [`../categories/combinatorics/subsets_minus_forbidden_combinations.md`](../categories/combinatorics/subsets_minus_forbidden_combinations.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Total Subsets minus Forbidden Combinations (Fermat Mod Inv)`  

---

## 1. Problem Statement & Key Idea
Given N flowers (N <= 10^9). Make a bouquet with at least 1 flower, but the number of flowers cannot be exactly a or b. Find the number of valid bouquets modulo 10^9 + 7.

**Key Idea**: Total possible non-empty subsets of N flowers is 2^N - 1. The forbidden choices are exactly C(N, a) and C(N, b).

## 2. Core Observation & Invariant
Answer is (2^N - 1 - C(N, a) - C(N, b)) mod (10^9 + 7). Because N <= 10^9, we cannot compute factorials up to N; however, a, b <= 2 * 10^5, so C(N, k) can be computed in O(k) steps using falling factorials: C(N, k) = prod_{i=0}^{k-1} (N - i) / k!.

## 3. Step-by-Step Algorithm
1. Compute total = (2^N - 1) % MOD.
2. Compute C(N, a) in O(a) using falling product divided by a!.
3. Compute C(N, b) in O(b) using falling product divided by b!.
4. Output (total - C(N, a) - C(N, b)) % MOD (adding 2 * MOD before modulo).

## 4. Complexity Analysis
- **Time Complexity**: `O(a + b + log N)`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

const int MOD = 1e9 + 7;

long long power_mod(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long mod_inv(long long n) {
    return power_mod(n, MOD - 2);
}

long long nCr_large_n(long long n, long long r) {
    if (r < 0 || r > n) return 0;
    long long num = 1;
    long long den = 1;
    for (long long i = 0; i < r; ++i) {
        num = (num * ((n - i) % MOD)) % MOD;
        den = (den * (i + 1)) % MOD;
    }
    return (num * mod_inv(den)) % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, a, b;
    if (!(cin >> n >> a >> b)) return 0;

    long long total = (power_mod(2, n) - 1 + MOD) % MOD;
    long long nCa = nCr_large_n(n, a);
    long long nCb = nCr_large_n(n, b);

    long long ans = (total - nCa - nCb) % MOD;
    ans = (ans + MOD + MOD) % MOD;

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Calculating binomial coefficients with large N and small k modulo prime.
- **Reusable Pattern**: `C(N, k) with N up to 10^9: product of (N - i) / (i + 1) for i in 0..k-1.`
