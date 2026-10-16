# Problem Analysis: AtCoder-abc152_e — Flatten

**Problem ID**: `AtCoder-abc152_e`  
**Contest**: `abc152`  
**Rating / Difficulty**: 1348  
**URL**: https://atcoder.jp/contests/abc152/tasks/abc152_e  
**VJudge Tag**: `[problem:AtCoder-abc152_e]`  
**Category File**: [`../categories/number_theory/array_lcm_prime_exponent_maxima.md`](../categories/number_theory/array_lcm_prime_exponent_maxima.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Prime Factorization`  
- **Topic (Skill)**: `LCM of Array Modulo 10^9+7 via Prime Exponent Maxima`  

---

## 1. Problem Statement & Key Idea
Given an array A of N positive integers (A_i <= 10^6). Find positive integers B_1..B_N such that A_1*B_1 = A_2*B_2 = ... = A_N*B_N and sum B_i is minimized. Output sum B_i modulo 10^9 + 7.

**Key Idea**: The common product L = A_i * B_i must equal the Least Common Multiple: L = lcm(A_1, ..., A_N). Then B_i = L / A_i, and sum B_i = L * sum_{i=1}^N A_i^(-1) (mod 10^9 + 7).

## 2. Core Observation & Invariant
L can be enormous (thousands of digits), so we cannot compute L directly. Instead, prime factorize each A_i using SPF sieve and track the maximum exponent of each prime: max_exp[p] = max_i v_p(A_i). Then L = prod p^{max_exp[p]} (mod 10^9 + 7). Finally, compute sum (L * A_i^(-1)) modulo 10^9 + 7.

## 3. Step-by-Step Algorithm
1. Compute SPF array up to MAX = 10^6 via Sieve.
2. Factorize each A_i, tracking max_exp[p] = max(max_exp[p], count_p).
3. Compute L = prod p^{max_exp[p]} modulo 10^9 + 7.
4. Compute sum B_i = sum (L * mod_inv(A_i)) modulo 10^9 + 7.
5. Output sum B_i.

## 4. Complexity Analysis
- **Time Complexity**: `O(MAX log log MAX + N log MAX)`
- **Space Complexity**: `O(MAX + N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1000000;
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    vector<int> spf(MAX + 1);
    for (int i = 0; i <= MAX; ++i) spf[i] = i;
    for (int i = 2; i * i <= MAX; ++i) {
        if (spf[i] == i) {
            for (int j = i * i; j <= MAX; j += i) {
                if (spf[j] == j) spf[j] = i;
            }
        }
    }

    vector<int> max_exp(MAX + 1, 0);

    for (int i = 0; i < n; ++i) {
        int temp = a[i];
        while (temp > 1) {
            int p = spf[temp];
            int count = 0;
            while (temp % p == 0) {
                count++;
                temp /= p;
            }
            if (count > max_exp[p]) {
                max_exp[p] = count;
            }
        }
    }

    long long L = 1;
    for (int p = 2; p <= MAX; ++p) {
        if (max_exp[p] > 0) {
            L = (L * power_mod(p, max_exp[p])) % MOD;
        }
    }

    long long sum_b = 0;
    for (int i = 0; i < n; ++i) {
        long long b_i = (L * mod_inv(a[i])) % MOD;
        sum_b = (sum_b + b_i) % MOD;
    }

    cout << sum_b << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Computing huge LCM of array modulo prime via prime exponent upper envelopes.
- **Reusable Pattern**: `LCM of array mod MOD: L = prod p^{max_exp[p]}, then B_i = L * inv(A_i).`
