# Problem Analysis: AtCoder-agc023_c — C. Painting Machines

**Problem ID**: `AtCoder-agc023_c`  
**Contest**: `agc023`  
**Rating / Difficulty**: 2568  
**URL**: https://atcoder.jp/contests/agc023/tasks/agc023_c  
**VJudge Tag**: `[problem:AtCoder-agc023_c]`  
**Category File**: [`../categories/combinatorics/painting_machines_non_adjacent_subsets_factorial.md`](../categories/combinatorics/painting_machines_non_adjacent_subsets_factorial.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Factorials and Binomial Coefficients (nCr)`  
- **Topic (Skill)**: `Large Factorials and Binomial Coefficients`  

---

## 1. Problem Statement & Key Idea
Evaluate the sum of operation counts across all $(N-1)!$ permutations of painting machines until all $N$ squares are painted black.

## 2. Core Observation & Invariant
Operating machines in subset $S$ covers all $N$ squares iff machines 1 and $N-1$ are selected and no two unchosen machines in $\{2, \dots, N-2\}$ are adjacent. For $|S| = k$, the number of valid subsets is $\binom{k - 1}{N - 1 - k}$. The number of permutations where all squares are covered within the first $k$ steps is $F(k) = \binom{k - 1}{N - 1 - k} k! (N - 1 - k)!$.

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and inverse factorials up to $N$.
2. 2. For each $k \in [1, N-1]$, let $m = N - 1 - k$. If $m \ge 0$, compute $F(k) = \binom{k - 1}{m} k! m!$.
3. 3. The number of permutations reaching full coverage precisely at step $k$ is $F(k) - F(k - 1)$.
4. 4. Accumulate $\sum_{k=1}^{N-1} k \cdot (F(k) - F(k - 1)) \pmod{10^9+7}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> fact(N + 1), invFact(N + 1);
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i <= N; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    };

    vector<long long> F(N, 0);
    for (int k = 1; k <= N - 1; ++k) {
        int m = N - 1 - k;
        if (m < 0) continue;
        long long ways = nCr(k - 1, m);
        if (ways > 0) {
            F[k] = ways * fact[k] % MOD * fact[N - 1 - k] % MOD;
        }
    }

    long long ans = 0;
    for (int k = 1; k <= N - 1; ++k) {
        long long count_k = (F[k] - F[k - 1] + MOD) % MOD;
        ans = (ans + (long long)k * count_k) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
