# Problem Analysis: AtCoder-abc235_g — G. Gardens

**Problem ID**: `AtCoder-abc235_g`  
**Contest**: `abc235`  
**Rating / Difficulty**: 2462  
**URL**: https://atcoder.jp/contests/abc235/tasks/abc235_g  
**VJudge Tag**: `[problem:AtCoder-abc235_g]`  
**Category File**: [`../categories/combinatorics/gardens_pie_prefix_binomial.md`](../categories/combinatorics/gardens_pie_prefix_binomial.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Count the number of ways to plant at most $A$ apple, $B$ banana, and $C$ cherry seedlings across $N$ gardens such that every garden receives at least one seedling and at most one of each kind.

## 2. Core Observation & Invariant
By PIE over gardens receiving no seedlings: $\sum_{m=0}^N (-1)^{N-m} \binom{N}{m} f(m, A) f(m, B) f(m, C)$, where $f(m, K) = \sum_{k=0}^K \binom{m}{k}$. Using Pascal's identity, $f(m, K) = \sum_{k=0}^K (\binom{m-1}{k} + \binom{m-1}{k-1}) = 2 f(m-1, K) - \binom{m-1}{K}$. This enables $O(1)$ state transitions as $m$ advances.

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and modular inverses up to $N$.
2. 2. Initialize $f(0, A) = f(0, B) = f(0, C) = 1$.
3. 3. Iterate $m$ from 1 to $N$, updating $f(m, K) = (2 f(m-1, K) - \binom{m-1}{K}) \pmod{998244353}$.
4. 4. Accumulate $(-1)^{N-m} \binom{N}{m} f(m, A) f(m, B) f(m, C) \pmod{998244353}$.
5. 5. Output the result modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, A, B, C;
    if (!(cin >> N >> A >> B >> C)) return 0;

    vector<long long> fact(N + 1, 1), inv(N + 1, 1);
    for (int i = 1; i <= N; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[N] = power(fact[N], MOD - 2);
    for (int i = N - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    long long fA = 1, fB = 1, fC = 1;
    long long ans = 0;

    long long sign = (N % 2 == 0 ? 1 : -1);
    ans = (ans + sign * nCr(N, 0) % MOD * fA % MOD * fB % MOD * fC) % MOD;

    for (int m = 1; m <= N; ++m) {
        fA = (2 * fA - nCr(m - 1, A)) % MOD;
        fB = (2 * fB - nCr(m - 1, B)) % MOD;
        fC = (2 * fC - nCr(m - 1, C)) % MOD;

        sign = ((N - m) % 2 == 0 ? 1 : -1);
        long long term = sign * nCr(N, m) % MOD * fA % MOD * fB % MOD * fC % MOD;
        ans = (ans + term) % MOD;
    }

    ans = (ans % MOD + MOD) % MOD;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
