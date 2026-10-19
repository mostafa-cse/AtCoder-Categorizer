# Problem Analysis: AtCoder-tenka1_2019_e — E - Polynomial Divisors

**Problem ID**: `AtCoder-tenka1_2019_e`  
**Contest**: `tenka1_2019`  
**Rating / Difficulty**: 2742  
**URL**: https://atcoder.jp/contests/tenka1_2019/tasks/tenka1_2019_e  
**VJudge Tag**: `[problem:AtCoder-tenka1_2019_e]`  
**Category File**: [`../categories/basics/polynomial_divisors_fermat_reduction.md`](../categories/basics/polynomial_divisors_fermat_reduction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Modular Arithmetic`  
- **Topic (Skill)**: `Fermat's Little Theorem and Modular Inverse`  

---

## 1. Problem Statement & Key Idea
Given an integer polynomial f(x) = a_N x^N + ... + a_1 x + a_0, find all prime numbers p such that p divides f(x) for all integers x.

## 2. Core Observation & Invariant
By Fermat's Little Theorem, x^k = x^{1 + (k - 1) mod (p - 1)} (mod p) for all x not divisible by p (and for x = 0, x^k = 0 for all k >= 1). Thus, modulo p, any polynomial reduces to an equivalent polynomial of degree at most p - 1. A polynomial of degree < p evaluates to 0 mod p for all integers x if and only if all of its reduced coefficients are 0 mod p! For primes p <= N, we can directly compute the reduced coefficients modulo p and verify if all are divisible by p. For primes p > N, no reduction of degree can occur, so f(x) = 0 mod p for all x requires all original coefficients a_i to be divisible by p, meaning p must divide gcd(a_0, a_1, ..., a_N).

## 3. Step-by-Step Algorithm
1. 1. Sieve primes up to N.
2. 2. For each prime p <= N:
3.    a. Reduce the exponents: add a_k to bucket rem = (k == 0 ? 0 : 1 + (k - 1) % (p - 1)).
4.    b. Check if all buckets are congruent to 0 mod p. If so, p is a valid prime.
5. 3. Compute G = gcd(|a_0|, |a_1|, ..., |a_N|).
6. 4. Factor G and add any prime factor p > N to the result list.
7. 5. Sort and output all discovered primes.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log log N + N * (N / log N) + sqrt(max A))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    // A is given from a_N down to a_0
    vector<long long> raw(n + 1);
    for (int i = 0; i <= n; i++) {
        cin >> raw[i];
    }

    // coeffs[k] is coefficient of x^k
    vector<long long> coeffs(n + 1);
    for (int i = 0; i <= n; i++) {
        coeffs[i] = raw[n - i];
    }

    long long g = 0;
    for (int i = 0; i <= n; i++) {
        g = gcd(g, abs(coeffs[i]));
    }

    // Sieve up to n
    vector<int> primes;
    if (n >= 2) {
        vector<bool> is_prime(n + 1, true);
        for (int i = 2; i <= n; i++) {
            if (is_prime[i]) {
                primes.push_back(i);
                for (long long j = 1LL * i * i; j <= n; j += i) {
                    is_prime[j] = false;
                }
            }
        }
    }

    vector<long long> ans;

    // Check primes p <= n
    for (int p : primes) {
        if (coeffs[0] % p != 0) continue;
        vector<long long> b(p - 1, 0);
        for (int k = 1; k <= n; k++) {
            int r = (k - 1) % (p - 1);
            b[r] = (b[r] + coeffs[k]) % p;
        }
        bool ok = true;
        for (int r = 0; r < p - 1; r++) {
            if ((b[r] % p + p) % p != 0) {
                ok = false;
                break;
            }
        }
        if (ok) {
            ans.push_back(p);
        }
    }

    // For primes p > n, p must divide g
    long long temp_g = g;
    for (long long d = 2; d * d <= temp_g; d++) {
        if (temp_g % d == 0) {
            if (d > n) {
                ans.push_back(d);
            }
            while (temp_g % d == 0) {
                temp_g /= d;
            }
        }
    }
    if (temp_g > 1 && temp_g > n) {
        ans.push_back(temp_g);
    }

    sort(ans.begin(), ans.end());
    ans.erase(unique(ans.begin(), ans.end()), ans.end());

    for (long long p : ans) {
        cout << p << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
