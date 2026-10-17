# Problem Analysis: AtCoder-arc004_4 — D. 表現の自由 ( Freedom of expression )

**Problem ID**: `AtCoder-arc004_4`  
**Contest**: `arc004`  
**Rating / Difficulty**: 2267  
**URL**: https://atcoder.jp/contests/arc004/tasks/arc004_4  
**VJudge Tag**: `[problem:AtCoder-arc004_4]`  
**Category File**: [`../categories/basics/stars_and_bars_signed_factor_partition.md`](../categories/basics/stars_and_bars_signed_factor_partition.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Stars and Bars`  

---

## 1. Problem Statement & Key Idea
Given integers $N$ ($1 \le |N| \le 10^9$) and $M$ ($1 \le M \le 10^5$). Count the number of ways to express $N$ as the product of $M$ integers: $N = a_1 \times a_2 \times \dots \times a_M$, with $a_i \in \mathbb{Z}$. Output the result modulo $10^9 + 7$.

## 2. Core Observation & Invariant
Decompose the problem into magnitudes and signs independently:
1. Magnitudes: Factorize $|N| = \prod_{i=1}^k p_i^{e_i}$. Each prime factor $p_i$ has its exponent $e_i$ partitioned among $M$ factors ($e_{i, 1} + \dots + e_{i, M} = e_i$). By stars and bars, the number of ways is $\binom{e_i + M - 1}{M - 1}$.
2. Signs: Exactly $M$ factors each have a sign $\in \{+1, -1\}$. If $N > 0$, an even number of factors must be negative; if $N < 0$, an odd number of factors must be negative. In either case, the number of valid sign assignments is precisely $\sum \binom{M}{s} = 2^{M - 1}$.
The total answer is $2^{M - 1} \times \prod_{i=1}^k \binom{e_i + M - 1}{M - 1} \pmod{10^9 + 7}$.

## 3. Step-by-Step Algorithm
1. Precompute factorials and modular inverse factorials up to $M + 100$.
2. Factorize $|N|$ by trial division up to $\sqrt{|N|}$ into prime powers $(p_i, e_i)$.
3. Compute base answer as $2^{M - 1} \pmod{10^9 + 7}$.
4. For each prime exponent $e_i$, multiply answer by $\binom{e_i + M - 1}{M - 1} \pmod{10^9 + 7}$.
5. Output the final product.

## 4. Complexity Analysis
- **Time Complexity**: `O(\sqrt{|N|} + M)`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>

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

// Precompute factorials up to M + 100
const int MAX_FACT = 200005;
vector<long long> fact(MAX_FACT), invFact(MAX_FACT);

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAX_FACT; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX_FACT - 1] = modInverse(fact[MAX_FACT - 1]);
    for (int i = MAX_FACT - 2; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    precompute();

    long long n, m;
    if (!(cin >> n >> m)) return 0;

    long long abs_n = llabs(n);
    vector<pair<long long, int>> factors;

    for (long long d = 2; d * d <= abs_n; ++d) {
        if (abs_n % d == 0) {
            int cnt = 0;
            while (abs_n % d == 0) {
                cnt++;
                abs_n /= d;
            }
            factors.push_back({d, cnt});
        }
    }
    if (abs_n > 1) {
        factors.push_back({abs_n, 1});
    }

    long long ans = power(2, m - 1);
    for (auto [p, e] : factors) {
        // distribute e identical exponents to m distinct factors: C(e + m - 1, m - 1)
        long long ways = nCr(e + m - 1, m - 1);
        ans = (ans * ways) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
