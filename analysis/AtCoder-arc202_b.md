# Problem Analysis: AtCoder-arc202_b — B. Tour

**Problem ID**: `AtCoder-arc202_b`  
**Contest**: `arc202`  
**Rating / Difficulty**: 2340  
**URL**: https://atcoder.jp/contests/arc202/tasks/arc202_b  
**VJudge Tag**: `[problem:AtCoder-arc202_b]`  
**Category File**: [`../categories/combinatorics/torus_knight_cycle_bipartite_gcd.md`](../categories/combinatorics/torus_knight_cycle_bipartite_gcd.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Factorials and Binomial Coefficients (nCr)`  
- **Topic (Skill)**: `Large Factorials and Binomial Coefficients`  

---

## 1. Problem Statement & Key Idea
Count the number of tours visiting every cell of an $H \times W$ torus chessboard under knight moves $(i-2, j \pm 1)$. If $H$ is even, answer is 0. If $H$ is odd, row visits are periodic and column shifts must be coprime to $W$ or $W/2$, solved in $O(H \log W)$.

## 2. Core Observation & Invariant
The row move $(i - 2) \bmod H$ is deterministic. If $H$ is even, odd rows are unreachable, yielding 0 tours. If $H$ is odd, row visits are periodic. When $W$ is odd, all cells in row $r$ must choose the same direction, requiring $\gcd((2a - H) \bmod W, W) = 1$. When $W$ is even, direction is uniform on $2H$ buckets $(r, c \bmod 2)$, requiring $\gcd((a - H) \bmod (W/2), W/2) = 1$.

## 3. Step-by-Step Algorithm
1. If $H$ is even, output 0.
2. If $W$ is odd, precompute factorials up to $H$ and evaluate $\sum_{a=0}^H [\gcd((2a - H) \bmod W, W) = 1] \binom{H}{a} \pmod{998244353}$.
3. If $W$ is even, precompute factorials up to $2H$ and evaluate $\sum_{a=0}^{2H} [\gcd((a - H) \bmod (W/2), W/2) = 1] \binom{2H}{a} \pmod{998244353}$ in $O(H \log W)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(H \log W)`
- **Space Complexity**: `O(H)`

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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long h, w;
    if (!(cin >> h >> w)) return 0;

    if (h % 2 == 0) {
        cout << 0 << "\n";
        return 0;
    }

    if (w % 2 != 0) {
        // W is odd
        vector<long long> fact(h + 1, 1), inv(h + 1, 1);
        for (int i = 1; i <= h; ++i) fact[i] = (fact[i - 1] * i) % MOD;
        inv[h] = modInverse(fact[h]);
        for (int i = h - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

        auto nCr = [&](int n, int r) -> long long {
            if (r < 0 || r > n) return 0;
            return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
        };

        long long ans = 0;
        for (int a = 0; a <= h; ++a) {
            long long delta = (2LL * a - h) % w;
            if (delta < 0) delta += w;
            if (std::gcd(delta, w) == 1) {
                ans = (ans + nCr(h, a)) % MOD;
            }
        }
        cout << ans << "\n";
    } else {
        // W is even
        long long w2 = w / 2;
        int n_steps = 2 * h;
        vector<long long> fact(n_steps + 1, 1), inv(n_steps + 1, 1);
        for (int i = 1; i <= n_steps; ++i) fact[i] = (fact[i - 1] * i) % MOD;
        inv[n_steps] = modInverse(fact[n_steps]);
        for (int i = n_steps - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

        auto nCr = [&](int n, int r) -> long long {
            if (r < 0 || r > n) return 0;
            return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
        };

        long long ans = 0;
        for (int a = 0; a <= n_steps; ++a) {
            long long delta = (a - h) % w2;
            if (delta < 0) delta += w2;
            if (std::gcd(delta, w2) == 1) {
                ans = (ans + nCr(n_steps, a)) % MOD;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
