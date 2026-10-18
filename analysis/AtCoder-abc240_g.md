# Problem Analysis: AtCoder-abc240_g — G. Teleporting Takahashi

**Problem ID**: `AtCoder-abc240_g`  
**Contest**: `abc240`  
**Rating / Difficulty**: 2462  
**URL**: https://atcoder.jp/contests/abc240/tasks/abc240_g  
**VJudge Tag**: `[problem:AtCoder-abc240_g]`  
**Category File**: [`../categories/combinatorics/teleporting_takahashi_3d_walk_combinatorics.md`](../categories/combinatorics/teleporting_takahashi_3d_walk_combinatorics.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Factorials and Binomial Coefficients (nCr)`  
- **Topic (Skill)**: `Large Factorials and Binomial Coefficients`  

---

## 1. Problem Statement & Key Idea
Count $N$-step 3D lattice walks from $(0, 0, 0)$ to $(X, Y, Z)$ where each step changes one coordinate by $\pm 1$. Iterate over the number of steps $C$ allocated to the $Z$-axis. The remaining $M = N - C$ steps in 2D rotate by 45 degrees: $(x, y) \to (x+y, x-y)$, decomposing the 2D walk into two independent 1D walks of length $M$ with steps in $\{+1, -1\}$.

## 2. Core Observation & Invariant
In 3D, choosing which $C$ of the $N$ steps move in $Z$ leaves $M = N - C$ steps for the $XY$-plane. In each of the $M$ steps, exactly one of $X$ or $Y$ moves by $\pm 1$. Rotating coordinates via $U = X + Y$ and $V = X - Y$ means in every step $(U, V)$ changes by $(\pm 1, \pm 1)$ independently, decoupling $U$ and $V$ into independent binomial distributions.

## 3. Step-by-Step Algorithm
1. 1. Verify parity and reachability: if $|X| + |Y| + |Z| > N$ or $(|X| + |Y| + |Z|) \not\equiv N \pmod 2$, output 0.
2. 2. Precompute factorials and inverses up to $N$.
3. 3. Iterate over the number of $Z$-steps $C$ from $|Z|$ to $N$ with $C \equiv |Z| \pmod 2$.
4. 4. Compute $ways_Z = \binom{N}{C} \binom{C}{(C + |Z|) / 2}$.
5. 5. For $M = N - C$, let $U = |X| + |Y|$ and $V = ||X| - |Y||$. Verify $|U| \le M, |V| \le M$, and $(M + U) \equiv (M + V) \equiv 0 \pmod 2$.
6. 6. Compute $ways_{XY} = \binom{M}{(M + U) / 2} \binom{M}{(M + V) / 2}$.
7. 7. Accumulate $\sum ways_Z \times ways_{XY} \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

const int MOD = 998244353;
const int MAXN = 10000005;

vector<long long> fact, inv_fact;

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

void precompute(int n) {
    fact.resize(n + 1);
    inv_fact.resize(n + 1);
    fact[0] = 1;
    inv_fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = (fact[i - 1] * i) % MOD;
    inv_fact[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 1; i--) inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long N, X, Y, Z;
    if (!(cin >> N >> X >> Y >> Z)) return 0;

    X = abs(X); Y = abs(Y); Z = abs(Z);
    if (X + Y + Z > N || (X + Y + Z) % 2 != N % 2) {
        cout << 0 << "\n";
        return 0;
    }

    precompute(N);

    long long ans = 0;
    for (long long C = Z; C <= N; ++C) {
        if ((C - Z) % 2 != 0) continue;
        long long M = N - C;
        long long U = X + Y;
        long long V = X - Y;
        if (abs(U) > M || abs(V) > M) continue;
        if ((M + U) % 2 != 0 || (M + V) % 2 != 0) continue;

        long long ways_Z = nCr(N, C) * nCr(C, (C + Z) / 2) % MOD;
        long long ways_XY = nCr(M, (M + U) / 2) * nCr(M, (M + V) / 2) % MOD;
        ans = (ans + ways_Z * ways_XY) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
