# Problem Analysis: AtCoder-aising2020_f — F - Two Snuke

**Problem ID**: `AtCoder-aising2020_f`  
**Contest**: `aising2020`  
**Rating / Difficulty**: 2741  
**URL**: https://atcoder.jp/contests/aising2020/tasks/aising2020_f  
**VJudge Tag**: `[problem:AtCoder-aising2020_f]`  
**Category File**: [`../categories/math/two_snuke_combinatorial_fps.md`](../categories/math/two_snuke_combinatorial_fps.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Generating Functions`  

---

## 1. Problem Statement & Key Idea
Two players simultaneously place points in a bounded region defined by linear constraints related to N, summing up values depending on geometric placements. Find the expected/total score modulo 998244353 for N <= 10^9.

## 2. Core Observation & Invariant
The combinatorial state space can be decomposed using generating functions into S(t) = t^5 / ((1 + t)^5 * (1 - t)^16). Expanding this rational function shows that the coefficient [t^N] S(t) splits into two polynomials in N of degree 15: one for even N and one for odd N. Because the degree is only 15, we can precompute the first 35 coefficients directly using formal power series truncated division, and then use Lagrange interpolation in O(d) time (d = 15) to evaluate the polynomial at N.

## 3. Step-by-Step Algorithm
1. 1. Express the generating function as P(t) / Q(t) where Q(t) = (1 + t)^5 * (1 - t)^16 and P(t) = t^5.
2. 2. Compute the expansion terms [t^k] S(t) for k up to 35 via standard polynomial division.
3. 3. Separate the sequence into even indices (2*k) and odd indices (2*k + 1).
4. 4. For a query N, select the corresponding parity, set x = (N - parity) / 2, and evaluate the degree-15 polynomial at x using Lagrange interpolation over the precomputed points in O(d) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(d^2) precomputation, O(d) per query where d = 15`
- **Space Complexity**: `O(d)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

long long interpolate(const vector<long long>& y, long long x_target) {
    int k = (int)y.size() - 1;
    if (x_target <= k) {
        return (y[x_target] % MOD + MOD) % MOD;
    }

    vector<long long> fact(k + 1, 1), inv_fact(k + 1, 1);
    for (int i = 1; i <= k; i++) fact[i] = (fact[i - 1] * i) % MOD;
    inv_fact[k] = modInverse(fact[k]);
    for (int i = k - 1; i >= 0; i--) inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;

    vector<long long> pref(k + 1, 1), suff(k + 1, 1);
    long long x_mod = (x_target % MOD + MOD) % MOD;
    for (int i = 0; i <= k; i++) {
        long long term = (x_mod - i + MOD) % MOD;
        pref[i] = ((i > 0 ? pref[i - 1] : 1LL) * term) % MOD;
    }
    for (int i = k; i >= 0; i--) {
        long long term = (x_mod - i + MOD) % MOD;
        suff[i] = ((i < k ? suff[i + 1] : 1LL) * term) % MOD;
    }

    long long ans = 0;
    for (int i = 0; i <= k; i++) {
        long long num = 1;
        if (i > 0) num = (num * pref[i - 1]) % MOD;
        if (i < k) num = (num * suff[i + 1]) % MOD;

        long long den = (inv_fact[i] * inv_fact[k - i]) % MOD;
        if ((k - i) % 2 == 1) den = (MOD - den) % MOD;

        long long term = (y[i] * num) % MOD;
        term = (term * den) % MOD;
        ans = (ans + term) % MOD;
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    const int DEG = 16; // degree of polynomial is 15, so 17 points (0..16) are sufficient
    const int MAX_TERMS = 2 * DEG + 10;
    vector<long long> coeffs(MAX_TERMS + 1, 0);
    coeffs[5] = 1;

    for (int step = 0; step < 5; step++) {
        for (int i = 1; i <= MAX_TERMS; i++) {
            coeffs[i] = (coeffs[i] - coeffs[i - 1] + MOD) % MOD;
        }
    }
    for (int step = 0; step < 16; step++) {
        for (int i = 1; i <= MAX_TERMS; i++) {
            coeffs[i] = (coeffs[i] + coeffs[i - 1]) % MOD;
        }
    }

    vector<long long> even_y(DEG + 1), odd_y(DEG + 1);
    for (int x = 0; x <= DEG; x++) {
        even_y[x] = coeffs[2 * x];
        odd_y[x] = coeffs[2 * x + 1];
    }

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long n;
        cin >> n;
        if (n % 2 == 0) {
            cout << interpolate(even_y, n / 2) << "\n";
        } else {
            cout << interpolate(odd_y, (n - 1) / 2) << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
