# Problem Analysis: AtCoder-m_solutions2019_e — E. Product of Arithmetic Progression

**Problem ID**: `AtCoder-m_solutions2019_e`  
**Contest**: `m_solutions2019`  
**Rating / Difficulty**: 2261  
**URL**: https://atcoder.jp/contests/m_solutions2019/tasks/m_solutions2019_e  
**VJudge Tag**: `[problem:AtCoder-m_solutions2019_e]`  
**Category File**: [`../categories/number_theory/arithmetic_progression_product_factorial_mod_prime.md`](../categories/number_theory/arithmetic_progression_product_factorial_mod_prime.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Primes and Divisors`  
- **Topic (Skill)**: `Wilson's Theorem`  

---

## 1. Problem Statement & Key Idea
Answer $Q$ queries: compute the product of an arithmetic progression $\prod_{i=0}^{n-1} (x + i d) \pmod{1000003}$.

## 2. Core Observation & Invariant
Let $P = 1000003$ (prime). If $d = 0$, the answer is $x^n \pmod P$. If $n \ge P$, at least one term is $0 \pmod P$, so the product is 0. If $n < P$ and $d \ne 0$, factor out $d$: $\prod (x + i d) = d^n \prod_{i=0}^{n-1} (k + i) \pmod P$ where $k = x d^{-1} \pmod P$. If $k + n - 1 \ge P$, the product wraps through $0 \pmod P$ and is 0; otherwise it is $d^n \frac{(k+n-1)!}{(k-1)!} \pmod P$, evaluated in $O(1)$ after $O(P)$ precomputation.

## 3. Step-by-Step Algorithm
1. Precompute factorials and modular inverse factorials up to $P = 1000003$.
2. For each query $(x, d, n)$:
3. If $d = 0$, output $x^n \bmod P$.
4. If $n \ge P$, output 0.
5. Compute $k = x d^{-1} \bmod P$. If $k = 0$ or $k + n - 1 \ge P$, output 0.
6. Otherwise, output $d^n \cdot fact[k + n - 1] \cdot inv\_fact[k - 1] \bmod P$.

## 4. Complexity Analysis
- **Time Complexity**: `O(P + Q \log P)`
- **Space Complexity**: `O(P)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000003;

long long fact[MOD], inv_fact[MOD];

long long mod_pow(long long a, long long b) {
    long long res = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) res = (res * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return res;
}

long long mod_inv(long long a) {
    return mod_pow(a, MOD - 2);
}

void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MOD; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv_fact[MOD - 1] = mod_inv(fact[MOD - 1]);
    for (int i = MOD - 2; i >= 0; --i) {
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    int Q;
    if (!(cin >> Q)) return 0;

    while (Q--) {
        long long x, d, n;
        cin >> x >> d >> n;

        if (d % MOD == 0) {
            cout << mod_pow(x, n) << "\n";
            continue;
        }

        if (n >= MOD) {
            cout << 0 << "\n";
            continue;
        }

        long long d_inv = mod_inv(d);
        long long k = (x % MOD * d_inv) % MOD;

        if (k == 0) {
            // First term is x = 0 mod MOD
            cout << 0 << "\n";
            continue;
        }

        if (k + n - 1 >= MOD) {
            cout << 0 << "\n";
            continue;
        }

        long long prod = fact[k + n - 1] * inv_fact[k - 1] % MOD;
        long long ans = prod * mod_pow(d, n) % MOD;
        cout << ans << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
