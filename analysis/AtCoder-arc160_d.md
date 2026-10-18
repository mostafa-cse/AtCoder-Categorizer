# Problem Analysis: AtCoder-arc160_d — D. Mahjong

**Problem ID**: `AtCoder-arc160_d`  
**Contest**: `arc160`  
**Rating / Difficulty**: 2485  
**URL**: https://atcoder.jp/contests/arc160/tasks/arc160_d  
**VJudge Tag**: `[problem:AtCoder-arc160_d]`  
**Category File**: [`../categories/math/mahjong_canonical_decomposition_generating_functions.md`](../categories/math/mahjong_canonical_decomposition_generating_functions.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Polynomial`  
- **Topic (Skill)**: `Generating Functions`  

---

## 1. Problem Statement & Key Idea
Count sequences $A_1, \dots, A_N$ reachable from all zeros by two operations: adding $K$ to a single element $A_i$ (Op 1), or adding 1 to a contiguous subsegment of length $K$ (Op 2), such that $\sum A_i = M$. An operation of adding $K$ to the same contiguous subsegment of length $K$ is equivalent to performing Op 1 on each element in that segment. Thus, a canonical representation restricts Op 2 on any subsegment to be applied at most $K - 1$ times. The remaining operations are Op 1 on individual elements.

## 2. Core Observation & Invariant
Total operations satisfy $\sum_{j=1}^{N - K + 1} x_j + \sum_{i=1}^N y_i = M / K$, with $0 \le x_j < K$ and $y_i \ge 0$. The number of ways to choose non-negative integers is given by the coefficient of $t^{M/K}$ in the generating function $\frac{(1 - t^K)^{N - K + 1}}{(1 - t)^{2N - K + 1}}$, extracted in $O(N)$ time via binomial expansion.

## 3. Step-by-Step Algorithm
1. 1. If $M \pmod K \ne 0$, output 0 immediately.
2. 2. Let $S = M / K$ and $L = N - K + 1$.
3. 3. The generating function is $(1 - t^K)^L (1 - t)^{-(N + L)}$.
4. 4. Expand $(1 - t^K)^L = \sum_{j=0}^L (-1)^j \binom{L}{j} t^{jK}$.
5. 5. For each $j$ such that $jK \le S$, the remaining power $S - jK$ draws from $(1 - t)^{-(N + L)}$ with coefficient $\binom{S - jK + N + L - 1}{N + L - 1}$.
6. 6. Sum $(-1)^j \binom{L}{j} \binom{S - jK + N + L - 1}{N + L - 1} \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, M, K;
    if (!(cin >> N >> M >> K)) return 0;

    if (M % K != 0) {
        cout << 0 << "\n";
        return 0;
    }

    long long S = M / K;
    long long L = N - K + 1;
    long long D = N + L - 1;

    int max_fact = max(L, D) + 10;
    vector<long long> fact(max_fact), inv(max_fact);
    fact[0] = 1;
    for (int i = 1; i < max_fact; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[max_fact - 1] = modInverse(fact[max_fact - 1]);
    for (int i = max_fact - 2; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](long long n, long long r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    auto comb_large = [&](long long n, long long r) -> long long {
        if (r < 0 || n < r) return 0;
        long long res = 1;
        for (int i = 0; i < r; ++i) {
            res = (res * (((n - i) % MOD + MOD) % MOD)) % MOD;
        }
        return res * inv[r] % MOD;
    };

    long long ans = 0;
    long long max_r = min(L, S / K);

    for (long long r = 0; r <= max_r; ++r) {
        long long sign = (r % 2 == 1) ? (MOD - 1) : 1;
        long long c1 = nCr(L, r);
        long long n_val = S - r * K + D;
        long long c2 = comb_large(n_val, D);
        long long term = sign * c1 % MOD * c2 % MOD;
        ans = (ans + term) % MOD;
    }

    cout << (ans % MOD + MOD) % MOD << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
