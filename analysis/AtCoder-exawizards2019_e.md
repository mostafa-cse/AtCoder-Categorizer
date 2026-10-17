# Problem Analysis: AtCoder-exawizards2019_e — E. Black or White

**Problem ID**: `AtCoder-exawizards2019_e`  
**Contest**: `exawizards2019`  
**Rating / Difficulty**: 2309  
**URL**: https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_e  
**VJudge Tag**: `[problem:AtCoder-exawizards2019_e]`  
**Category File**: [`../categories/math/exhaustion_boundary_incremental_binomial_tails.md`](../categories/math/exhaustion_boundary_incremental_binomial_tails.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Gambler's Ruin`  

---

## 1. Problem Statement & Key Idea
Given $B$ black and $W$ white chocolates, repeatedly choose Black or White with equal probability and eat one if available. Find the probability that the $i$-th chocolate eaten is Black for all $i = 1, \dots, B+W$.

## 2. Core Observation & Invariant
Before either color is exhausted, each chocolate chosen is Black with probability $1/2$. Once White is exhausted, all remaining chocolates are Black with probability 1; once Black is exhausted, Black has probability 0.

## 3. Step-by-Step Algorithm
1. Express $P(i\text{-th is Black}) = 1/2 + 1/2 [P(\text{White exhausted before } i) - P(\text{Black exhausted before } i)]$.
2. The probability that White was exhausted in the first $n = i-1$ flips is the binomial tail $\sum_{k=W}^n \binom{n}{k} (1/2)^n$.
3. Update tail sums incrementally via $S(n) = S(n-1) + \binom{n-1}{W-1} (1/2)^n$ in $O(1)$ per step.

## 4. Complexity Analysis
- **Time Complexity**: `O(B + W)`
- **Space Complexity**: `O(B + W)`

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

    int B, W;
    if (!(cin >> B >> W)) return 0;

    int N = B + W;

    vector<long long> fact(N + 1, 1), invFact(N + 1, 1);
    for (int i = 1; i <= N; ++i) fact[i] = (fact[i - 1] * i) % MOD;
    invFact[N] = modInverse(fact[N]);
    for (int i = N - 1; i >= 0; --i) invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;

    auto nCr = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    };

    vector<long long> pow_half(N + 1, 1);
    long long half = modInverse(2);
    for (int i = 1; i <= N; ++i) pow_half[i] = (pow_half[i - 1] * half) % MOD;

    long long S_W = 0, S_B = 0;

    for (int i = 1; i <= N; ++i) {
        int n = i - 1;
        if (n >= 1) {
            if (n - 1 >= W - 1) {
                long long term = nCr(n - 1, W - 1) * pow_half[n] % MOD;
                S_W = (S_W + term) % MOD;
            }
            if (n - 1 >= B - 1) {
                long long term = nCr(n - 1, B - 1) * pow_half[n] % MOD;
                S_B = (S_B + term) % MOD;
            }
        }

        long long diff = (S_W - S_B) % MOD;
        if (diff < 0) diff += MOD;

        long long ans = (half + half * diff) % MOD;
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
