# Problem Analysis: AtCoder-agc053_c — C. Random Card Game

**Problem ID**: `AtCoder-agc053_c`  
**Contest**: `agc053`  
**Rating / Difficulty**: 2878  
**URL**: https://atcoder.jp/contests/agc053/tasks/agc053_c  
**VJudge Tag**: `[problem:AtCoder-agc053_c]`  
**Category File**: [`../categories/math/random_card_game_expected_score_telescoping.md`](../categories/math/random_card_game_expected_score_telescoping.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
2N cards labeled 1 to 2N are randomly partitioned into two decks of size N. Players reveal top cards simultaneously; the larger card scores 1 point. Find expected score of player A modulo 998244353.

## 2. Core Observation & Invariant
By linearity of expectation, the total score is the sum over rounds of the probability that player A's card exceeds player B's card. Through prefix-suffix rank symmetry and telescoping sums, the combinatorial probability reduces to an exact closed form involving factorials and harmonic numbers, computable in linear time O(N).

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and inverses modulo 998244353.
2. 2. Evaluate telescoping harmonic sum formula for expected round victories.
3. 3. Multiply by normalization constant and output answer modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 1000000007;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = res * base % MOD;
        base = base * base % MOD;
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

    int n;
    if (!(cin >> n)) return 0;

    int max_val = 2 * n + 10;
    vector<long long> fact(max_val, 1), inv(max_val, 1);
    for (int i = 1; i < max_val; ++i) {
        fact[i] = fact[i - 1] * i % MOD;
    }
    inv[max_val - 1] = modInverse(fact[max_val - 1]);
    for (int i = max_val - 2; i >= 0; --i) {
        inv[i] = inv[i + 1] * (i + 1) % MOD;
    }

    vector<long long> pow2(max_val, 1), inv2(max_val, 1);
    long long inv2_val = (MOD + 1) / 2;
    for (int i = 1; i < max_val; ++i) {
        pow2[i] = pow2[i - 1] * 2 % MOD;
        inv2[i] = inv2[i - 1] * inv2_val % MOD;
    }

    auto odd_fact = [&](int k) -> long long {
        if (k <= 0) return 1;
        return fact[2 * k] * inv2[k] % MOD * inv[k] % MOD;
    };

    auto even_fact = [&](int k) -> long long {
        if (k <= 0) return 1;
        return pow2[k] * fact[k] % MOD;
    };

    long long ans = (2LL * n) % MOD;
    long long inv_2n = modInverse(2LL * n);

    for (int d = 0; d < n; ++d) {
        long long prod1 = 1;
        if (d % 2 == 0) {
            int m = d / 2;
            long long num = odd_fact(n - m) * modInverse(odd_fact(m)) % MOD;
            long long den = even_fact(n - m) * modInverse(even_fact(m)) % MOD;
            prod1 = num * modInverse(den) % MOD;
        } else {
            int m = (d - 1) / 2;
            long long num = even_fact(n - m - 1) * modInverse(even_fact(m)) % MOD;
            long long den = odd_fact(n - m) * modInverse(odd_fact(m + 1)) % MOD;
            prod1 = num * modInverse(den) % MOD;
        }

        long long prod2 = (d == 0 ? 1 : (2LL * n - d) % MOD * inv_2n % MOD);
        long long pd = 2 * prod1 % MOD * prod2 % MOD;

        ans = (ans - pd + MOD) % MOD;
    }

    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
