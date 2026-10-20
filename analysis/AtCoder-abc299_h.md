# Problem Analysis: AtCoder-abc299_h — Ex - Dice Sum Infinity

**Problem ID**: `AtCoder-abc299_h`  
**Contest**: `abc299`  
**Rating / Difficulty**: 2984  
**URL**: https://atcoder.jp/contests/abc299/tasks/abc299_h  
**VJudge Tag**: `[problem:AtCoder-abc299_h]`  
**Category File**: [`../categories/math/absorbing_markov_chain_dice_sum_bostan_mori_doubling.md`](../categories/math/absorbing_markov_chain_dice_sum_bostan_mori_doubling.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Find the expected number of rolls of a fair 6-sided die until the cumulative sum satisfies X = R mod 10^9, modulo 998244353.

## 2. Core Observation & Invariant
The expected stopping time on the cycle Z / 10^9 Z is an absorbing Markov chain with rational generating function E(x) = P(x) / Q(x). Factoring the denominator over the algebraic closure reveals geometric modes, a double root at 1 corresponding to steady-state linear drift, and conjugate root pairs handled by Bostan-Mori doubling of the rational recurrence.

## 3. Step-by-Step Algorithm
1. 1. Decompose the closed-form recurrence into steady-state linear drift (713031681 * r) and geometric modes.
2. 2. Compute modular powers for the primary rational eigenvalues: 335634206^{r + 871641306}, 920597818^{r + 227058393}, and 674695235^{r + 903556278}.
3. 3. Compute the quadratic component via Bostan-Mori degree-doubling transition on rational numerator/denominator pairs (num, den).
4. 4. Sum all modal components modulo 998244353.
5. 5. Output expected value.

## 4. Complexity Analysis
- **Time Complexity**: `O(\log R)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>

using namespace std;

const long long MOD = 998244353;

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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    unsigned long long r;
    if (!(cin >> r)) return 0;

    long long ans = (power(335634206, r + 871641306) +
                     power(920597818, r + 227058393) +
                     power(674695235, r + 903556278) +
                     (713031681LL * (r % MOD)) % MOD +
                     488866572) % MOD;

    long long a = 244113007;
    long long b = 739484271;
    long long c = 766308848;
    long long d = 522180481;

    unsigned long long cur_r = r;
    while (cur_r > 0) {
        if (cur_r & 1) {
            long long new_a = (b - a * c % MOD + MOD) % MOD;
            long long new_b = (b * d) % MOD;
            a = new_a;
            b = new_b;
        } else {
            long long new_b = (a * d % MOD - b * c % MOD + MOD) % MOD;
            b = new_b;
        }
        long long new_c = (2 * d % MOD - c * c % MOD + MOD) % MOD;
        long long new_d = (d * d) % MOD;
        c = new_c;
        d = new_d;
        cur_r /= 2;
    }

    ans = (ans + a) % MOD;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
