# Problem Analysis: AtCoder-arc202_c — C. Repunits

**Problem ID**: `AtCoder-arc202_c`  
**Contest**: `arc202`  
**Rating / Difficulty**: 2274  
**URL**: https://atcoder.jp/contests/arc202/tasks/arc202_c  
**VJudge Tag**: `[problem:AtCoder-arc202_c]`  
**Category File**: [`../categories/number_theory/mobius_inversion_repunit_lcm.md`](../categories/number_theory/mobius_inversion_repunit_lcm.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Multiplicative Functions`  
- **Topic (Skill)**: `Mobius Function and Mobius Inversion`  

---

## 1. Problem Statement & Key Idea
Given an array of indices $A_1, \dots, A_N$, find the least common multiple of repunits $R_{A_1}, \dots, R_{A_k}$ modulo 998244353 for every prefix $k = 1, \dots, N$.

## 2. Core Observation & Invariant
Repunits $R_n = (10^n - 1)/9$ form a strong divisibility sequence satisfying $\gcd(R_a, R_b) = R_{\gcd(a, b)}$. By multiplicative Möbius inversion, $R_n = \prod_{d | n} f(d)$ where $f(d) = \prod_{c | d} R_c^{\mu(d/c)}$, and $\mathrm{LCM}(R_{A_1}, \dots, R_{A_k}) = \prod_{d \in \bigcup_{i=1}^k \mathrm{divisors}(A_i)} f(d)$.

## 3. Step-by-Step Algorithm
1. 1. Note that $\gcd(10^a - 1, 10^b - 1) = 10^{\gcd(a, b)} - 1$, which implies repunits $R_n = (10^n - 1)/9$ satisfy $\gcd(R_a, R_b) = R_{\gcd(a, b)}$.\n2. For any strong divisibility sequence, the lattice of elements under $\gcd$ and $\mathrm{lcm}$ is isomorphic to the divisibility poset of their indices. Decomposing $R_n$ multiplicatively via Möbius inversion yields $R_n = \prod_{d | n} f(d)$ where $f(d) = \prod_{c | d} R_c^{\mu(d/c)} \pmod{998244353}$.\n3. The least common multiple of any subset is the product of $f(d)$ over the union of all divisors of the indices: $\mathrm{LCM}(R_{A_1}, \dots, R_{A_k}) = \prod_{d \in D_k} f(d)$, where $D_k = \bigcup_{i=1}^k \mathrm{divisors}(A_i)$.\n4. Precompute $\mu(k)$, $R_k$, and $f(d)$ for all $d \le 200000$ using a linear sieve and divisor transitions in $O(M \log M)$ where $M = 2 \times 10^5$. Maintain a global boolean array `seen[d]` and running cumulative product. For each query $A_k$, factorize $A_k$ in $O(d(A_k))$, multiply in $f(d)$ for newly discovered divisors, and output the cumulative LCM in $O(1)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(M \log M + N \cdot d(M)) where M = \max(A_i) \le 2 \times 10^5`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

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

const int MAXV = 200000;
int mu[MAXV + 1];
vector<int> primes;
bool is_prime[MAXV + 1];
long long R[MAXV + 1];
long long invR[MAXV + 1];
long long f[MAXV + 1];
vector<int> divisors_list[MAXV + 1];
bool seen[MAXV + 1];

void sieve() {
    fill(is_prime + 2, is_prime + MAXV + 1, true);
    mu[1] = 1;
    for (int i = 2; i <= MAXV; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
            mu[i] = -1;
        }
        for (int p : primes) {
            if (i * p > MAXV) break;
            is_prime[i * p] = false;
            if (i % p == 0) {
                mu[i * p] = 0;
                break;
            } else {
                mu[i * p] = -mu[i];
            }
        }
    }

    long long inv9 = modInverse(9);
    for (int i = 1; i <= MAXV; i++) {
        long long num = (power(10, i) - 1 + MOD) % MOD;
        R[i] = (num * inv9) % MOD;
        invR[i] = modInverse(R[i]);
        f[i] = 1;
    }

    for (int c = 1; c <= MAXV; c++) {
        for (int d = c; d <= MAXV; d += c) {
            divisors_list[d].push_back(c);
            int k = d / c;
            if (mu[k] == 1) {
                f[d] = (f[d] * R[c]) % MOD;
            } else if (mu[k] == -1) {
                f[d] = (f[d] * invR[c]) % MOD;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    sieve();

    int n;
    if (!(cin >> n)) return 0;
    long long current_lcm = 1;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        for (int d : divisors_list[a]) {
            if (!seen[d]) {
                seen[d] = true;
                current_lcm = (current_lcm * f[d]) % MOD;
            }
        }
        cout << current_lcm << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
