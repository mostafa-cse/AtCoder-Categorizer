# Problem Analysis: AtCoder-agc038_c — C. LCMs

**Problem ID**: `AtCoder-agc038_c`  
**Contest**: `agc038`  
**Rating / Difficulty**: 2327  
**URL**: https://atcoder.jp/contests/agc038/tasks/agc038_c  
**VJudge Tag**: `[problem:AtCoder-agc038_c]`  
**Category File**: [`../categories/number_theory/lcm_sum_dirichlet_mobius_inversion.md`](../categories/number_theory/lcm_sum_dirichlet_mobius_inversion.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Multiplicative Functions`  
- **Topic (Skill)**: `Mobius Function and Mobius Inversion`  

---

## 1. Problem Statement & Key Idea
Given array $A$ of length $N$, compute $\sum_{1 \le i < j \le N} \text{lcm}(A_i, A_j) \pmod{998244353}$.

## 2. Core Observation & Invariant
Expressing $\frac{1}{\gcd(x, y)} = \sum_{d \mid \gcd(x, y)} c(d)$ via Dirichlet inversion yields $c(d) = d^{-1} \prod_{p \mid d} (1 - p)$, completely decoupling the pair summation into independent multiple sums.

## 3. Step-by-Step Algorithm
1. Precompute the multiplicative function $c(d) = d^{-1} \prod_{p \mid d} (1 - p)$ using a linear sieve up to $M = \max(A) \le 10^6$.
2. Compute $S(d) = \sum_{A_i \equiv 0 \pmod d} A_i$ for all $d$ via harmonic multiple iteration in $O(M \log M)$ time.
3. Evaluate the double sum $\sum_{d=1}^M c(d) (S(d))^2$, subtract the diagonal $\sum A_i$, and multiply by $2^{-1} \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(M \log M + N)`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    int max_a = 0;
    long long diag = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] > max_a) max_a = a[i];
        diag = (diag + a[i]) % MOD;
    }

    vector<long long> sum_val(max_a + 1, 0);
    for (int x : a) {
        sum_val[x] = (sum_val[x] + x) % MOD;
    }

    vector<int> primes;
    vector<bool> is_prime(max_a + 1, true);
    vector<long long> g(max_a + 1, 1);

    for (int i = 2; i <= max_a; ++i) {
        if (is_prime[i]) {
            primes.push_back(i);
            g[i] = (1 - i + MOD) % MOD;
        }
        for (int p : primes) {
            if (1LL * i * p > max_a) break;
            is_prime[i * p] = false;
            if (i % p == 0) {
                g[i * p] = g[i];
                break;
            } else {
                g[i * p] = (g[i] * (1 - p + MOD)) % MOD;
            }
        }
    }

    vector<long long> inv(max_a + 1, 1);
    for (int i = 2; i <= max_a; ++i) {
        inv[i] = 1LL * (MOD - MOD / i) * inv[MOD % i] % MOD;
    }

    vector<long long> c(max_a + 1, 0);
    for (int d = 1; d <= max_a; ++d) {
        c[d] = (inv[d] * g[d]) % MOD;
    }

    long long total = 0;
    for (int d = 1; d <= max_a; ++d) {
        long long s = 0;
        for (int kd = d; kd <= max_a; kd += d) {
            s += sum_val[kd];
            if (s >= MOD) s -= MOD;
        }
        if (s == 0) continue;
        long long term = (c[d] * s % MOD * s) % MOD;
        total = (total + term) % MOD;
    }

    long long ans = (total - diag + MOD) % MOD;
    ans = (ans * inv[2]) % MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
