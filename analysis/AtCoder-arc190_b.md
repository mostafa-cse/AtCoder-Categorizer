# Problem Analysis: AtCoder-arc190_b — B. L Partition

**Problem ID**: `AtCoder-arc190_b`  
**Contest**: `arc190`  
**Rating / Difficulty**: 2273  
**URL**: https://atcoder.jp/contests/arc190/tasks/arc190_b  
**VJudge Tag**: `[problem:AtCoder-arc190_b]`  
**Category File**: [`../categories/combinatorics/prefix_sum_binomial_l_partition_bijection.md`](../categories/combinatorics/prefix_sum_binomial_l_partition_bijection.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Factorials and Binomial Coefficients (nCr)`  
- **Topic (Skill)**: `Prefix Sum Queries of Binomial Coefficients`  

---

## 1. Problem Statement & Key Idea
Partition an $N \times N$ grid ($N \le 10^7$) into $N$ L-shapes, one of each level $1, \dots, N$. For $Q \le 200,000$ queries $k_i$, count the partitions where a given cell $(a, b)$ belongs to the level $k_i$ L-shape, modulo 998244353.

## 2. Core Observation & Invariant
Level $k$ or smaller L-shapes always occupy a square subgrid $I_k \times J_k$ of size $k \times k$, where $[1, N] = I_N \supsetneq \dots \supsetneq I_1$ and $[1, N] = J_N \supsetneq \dots \supsetneq J_1$ are shrinking intervals. Cell $(a, b)$ belongs to level $\le k$ iff $a \in I_k$ and $b \in J_k$. The row and column choices are completely independent! For a 1D sequence of intervals, starting at $[1, N]$ and shrinking by 1 at each step to $[1+x, k+x]$ after $m = N - k$ steps has $\binom{m}{x}$ paths. The condition $a \in [1+x, k+x]$ gives $x \in [\max(0, a-k), \min(N-k, a-1)]$. Hence $F(a, k) = 2^{k-1} \sum_{x} \binom{N-k}{x}$. As $m = N-k$ increments, $\sum \binom{m+1}{x}$ updates in $O(1)$ from $\sum \binom{m}{x}$. The exact level $k$ answer is $F(a, k) F(b, k) - F(a, k-1) F(b, k-1)$.

## 3. Step-by-Step Algorithm
1. Precompute factorials and powers of 2 up to $N$.
2. Compute array $F(a, k)$ for $k = N$ down to $1$ ($m = N-k$ from 0 to $N-1$) by updating binomial coefficient prefix sums in $O(1)$ per step.
3. Compute array $F(b, k)$ similarly for coordinate $b$.
4. For each query $k$, output $(F(a, k) F(b, k) - F(a, k-1) F(b, k-1)) \pmod{998244353}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q)`
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

    int n, a, b, q;
    if (!(cin >> n >> a >> b >> q)) return 0;

    vector<int> queries(q);
    for (int i = 0; i < q; ++i) cin >> queries[i];

    // Precompute factorials up to n
    vector<int> fact(n + 1), invFact(n + 1), pow2(n + 1);
    fact[0] = 1;
    invFact[0] = 1;
    pow2[0] = 1;

    for (int i = 1; i <= n; ++i) {
        fact[i] = (1LL * fact[i - 1] * i) % MOD;
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }
    invFact[n] = modInverse(fact[n]);
    for (int i = n - 1; i >= 1; --i) {
        invFact[i] = (1LL * invFact[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n, int r) -> int {
        if (r < 0 || r > n) return 0;
        return 1LL * fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    };

    auto compute_F = [&](int coord) -> vector<int> {
        vector<int> F(n + 1, 0);

        long long cur_sum = (max(0, coord - n) <= 0 && 0 <= min(0, coord - 1)) ? 1 : 0;
        int cur_L = max(0, coord - n);
        int cur_R = min(0, coord - 1);

        F[n] = (cur_sum * pow2[n - 1]) % MOD;

        for (int m = 0; m < n - 1; ++m) {
            long long next_sum = (2LL * cur_sum - nCr(m, cur_R) + nCr(m, cur_L - 1)) % MOD;
            int next_L = max(0, coord - (n - (m + 1)));
            int next_R = min(m + 1, coord - 1);

            while (cur_L < next_L) {
                next_sum = (next_sum - nCr(m + 1, cur_L)) % MOD;
                cur_L++;
            }
            while (cur_L > next_L) {
                cur_L--;
                next_sum = (next_sum + nCr(m + 1, cur_L)) % MOD;
            }

            while (cur_R < next_R) {
                cur_R++;
                next_sum = (next_sum + nCr(m + 1, cur_R)) % MOD;
            }
            while (cur_R > next_R) {
                next_sum = (next_sum - nCr(m + 1, cur_R)) % MOD;
                cur_R--;
            }

            cur_sum = (next_sum % MOD + MOD) % MOD;
            int k = n - (m + 1);
            F[k] = (cur_sum * pow2[k - 1]) % MOD;
        }

        return F;
    };

    vector<int> Fa = compute_F(a);
    vector<int> Fb = compute_F(b);

    for (int k : queries) {
        long long leq_k = 1LL * Fa[k] * Fb[k] % MOD;
        long long leq_prev = (k > 1 ? 1LL * Fa[k - 1] * Fb[k - 1] % MOD : 0);
        long long exact_k = (leq_k - leq_prev + MOD) % MOD;
        cout << exact_k << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
