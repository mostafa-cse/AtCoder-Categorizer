# Problem Analysis: AtCoder-arc144_d — D. AND OR Equation

**Problem ID**: `AtCoder-arc144_d`  
**Contest**: `arc144`  
**Rating / Difficulty**: 2468  
**URL**: https://atcoder.jp/contests/arc144/tasks/arc144_d  
**VJudge Tag**: `[problem:AtCoder-arc144_d]`  
**Category File**: [`../categories/math/and_or_affine_lattice_combinations.md`](../categories/math/and_or_affine_lattice_combinations.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Vector Space and XOR Basis`  

---

## 1. Problem Statement & Key Idea
Count integer functions $f: \{0, 1\}^N \to [0, K]$ satisfying $f(x) + f(y) = f(x \land y) + f(x \lor y)$. The functional equation forces $f$ to be affine: $f(x) = a + \sum_{i=0}^{N-1} c_i x_i$. Boundedness $0 \le f(x) \le K$ implies $\sum |c_i| \le K$, with $K - \sum |c_i| + 1$ choices for $a$. Grouping by the number of non-zero $c_i$ simplifies via the double hockey stick identity to $\sum_{m=0}^{\min(N, K)} \binom{N}{m} 2^m \binom{K+1}{m+1}$.

## 2. Core Observation & Invariant
On the Boolean hypercube, modular lattice functions $f(x) + f(y) = f(x \land y) + f(x \lor y)$ are exactly linear combinations of the coordinate bits plus a constant. The extreme values of $f$ over all $2^N$ vertices are $a - \sum_{c_i < 0} |c_i|$ and $a + \sum_{c_i > 0} c_i$, making the valid interval for $a$ depend solely on $\sum |c_i|$.

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and modular inverses up to $N$.
2. 2. Initialize `ans = 0` and `cur_comb_K = (K + 1) % MOD`.
3. 3. Loop $m$ from $0$ to $\min(N, K)$:
4.    a. Compute term: $\binom{N}{m} \times 2^m \times \binom{K+1}{m+1} \pmod{998244353}$.
5.    b. Add term to `ans`.
6.    c. Transition $\binom{K+1}{m+1} \to \binom{K+1}{m+2}$ by multiplying $(K - m)$ and dividing $(m + 2)$.
7. 4. Output `ans`.

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

    long long N, K;
    if (!(cin >> N >> K)) return 0;

    int max_m = min((long long)N, K);

    vector<long long> fact(N + 1), inv(N + 1);
    fact[0] = 1;
    for (int i = 1; i <= N; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    inv[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; --i) inv[i] = (inv[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * inv[r] % MOD * inv[n - r] % MOD;
    };

    long long ans = 0;
    long long cur_comb_K = (K + 1) % MOD;
    long long pow2 = 1;

    for (int m = 0; m <= max_m; ++m) {
        long long term = nCr(N, m) * pow2 % MOD * cur_comb_K % MOD;
        ans = (ans + term) % MOD;

        if (m < max_m) {
            long long mult = (K - m) % MOD;
            long long div = modInverse(m + 2);
            cur_comb_K = cur_comb_K * mult % MOD * div % MOD;
            pow2 = (pow2 * 2) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
