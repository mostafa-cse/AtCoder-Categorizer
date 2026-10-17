# Problem Analysis: AtCoder-abc450_g — Random Subtraction

**Problem ID**: `AtCoder-abc450_g`  
**Contest**: `abc450`  
**Rating / Difficulty**: 2227  
**URL**: https://atcoder.jp/contests/abc450/tasks/abc450_g  
**VJudge Tag**: `[problem:AtCoder-abc450_g]`  
**Category File**: [`../categories/math/expected_value_quadratic_forms_random_subtraction.md`](../categories/math/expected_value_quadratic_forms_random_subtraction.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Find the expected value of x^2 modulo 998244353 where x is the remaining element after repeatedly picking two random elements a, b and replacing them with a - b.

## 2. Core Observation & Invariant
The final element x is a linear combination x = sum c_i A_i with signs c_i in {-1, +1}. Expanding the square gives x^2 = sum A_i^2 + 2 sum_{i < j} c_i c_j A_i A_j. By symmetry, E[c_i c_j] = rho_N is identical for all pairs i != j. A martingale / tree recurrence shows sum_{i < j} E[c_i c_j] = -N / 3 for N >= 3, giving rho_N = -2 / (3 * (N - 1)). Thus, E[x^2] = sum A_i^2 + rho_N * ((sum A_i)^2 - sum A_i^2).

## 3. Step-by-Step Algorithm
1. 1. If N == 1, return A_0^2 % MOD.
2. 2. If N == 2, return (A_0 - A_1)^2 % MOD.
3. 3. For N >= 3, compute sum_A = sum(A) % MOD and sum_sq = sum(A_i^2) % MOD.
4. 4. Compute cross = (sum_A^2 - sum_sq) % MOD.
5. 5. Compute rho_N = -2 * inv(3 * (N - 1)) % MOD.
6. 6. Return (sum_sq + rho_N * cross) % MOD.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 998244353;

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

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    long long sum_A = 0;
    long long sum_sq = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        sum_A = (sum_A + a[i]) % MOD;
        sum_sq = (sum_sq + a[i] * a[i]) % MOD;
    }

    if (n == 1) {
        cout << (a[0] * a[0]) % MOD << "\n";
        return 0;
    }
    if (n == 2) {
        long long diff = (a[0] - a[1]) % MOD;
        diff = (diff + MOD) % MOD;
        cout << (diff * diff) % MOD << "\n";
        return 0;
    }

    long long cross = (sum_A * sum_A % MOD - sum_sq + MOD) % MOD;
    long long denom = (3LL * (n - 1)) % MOD;
    long long inv_denom = modInverse(denom);
    long long rho = (-2LL * inv_denom % MOD + MOD) % MOD;

    long long ans = (sum_sq + rho * cross) % MOD;
    cout << ans << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
