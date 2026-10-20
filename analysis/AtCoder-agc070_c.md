# Problem Analysis: AtCoder-agc070_c — C - No Streak

**Problem ID**: `AtCoder-agc070_c`  
**Contest**: `agc070`  
**Rating / Difficulty**: 2983  
**URL**: https://atcoder.jp/contests/agc070/tasks/agc070_c  
**VJudge Tag**: `[problem:AtCoder-agc070_c]`  
**Category File**: [`../categories/combinatorics/catalan_reflection_streak_avoidance_pie.md`](../categories/combinatorics/catalan_reflection_streak_avoidance_pie.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Count the number of rock-paper-scissors sequences of length N with A wins for Alice, B wins for Bob, and X = N - A - B draws such that Alice's cumulative wins are always >= Bob's wins, and neither player wins twice consecutively without an intervening draw.

## 2. Core Observation & Invariant
Formulate as strings of A, B, X. Using the reflection principle across the diagonal, subtracting paths that violate the prefix condition requires tracking whether the violation step is followed by BB or BX. The base function f(a, b, x) counts arrangements without AA and without BB using stars and bars / PIE on adjacent pairs: f(a, b, x) = \sum_{k=0}^{a-1} \binom{a-1}{k} \binom{x+1}{a-k} \binom{a+x+1-k}{b-k}. The total valid strings is f(A, B, x) - f(B-1, A, x) - f(B-1, A, x-1) - f(B-1, A+1, x-1).

## 3. Step-by-Step Algorithm
1. 1. Precompute factorials and inverse factorials up to N+5 in O(N).
2. 2. Implement combinatorial function f(a, b, x) in O(\min(a, b)) time.
3. 3. Handle base cases when a=0 or b=0.
4. 4. Evaluate t1 = f(A, B, x), t2 = f(B-1, A, x), t3 = f(B-1, A, x-1), t4 = f(B-1, A+1, x-1).
5. 5. Compute ans = (t1 - t2 - t3 - t4) mod (10^9 + 7).

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

int max_n;
vector<int> fact;
vector<int> invFact;

void precompute(int n) {
    max_n = n;
    fact.resize(max_n + 1);
    invFact.resize(max_n + 1);
    fact[0] = 1;
    for (int i = 1; i <= max_n; i++) {
        fact[i] = (1LL * fact[i - 1] * i) % MOD;
    }
    invFact[max_n] = modInverse(fact[max_n]);
    for (int i = max_n - 1; i >= 0; i--) {
        invFact[i] = (1LL * invFact[i + 1] * (i + 1)) % MOD;
    }
}

inline long long comb(int n, int k) {
    if (k < 0 || k > n) return 0;
    return 1LL * fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
}

long long f(int a, int b, int x) {
    if (a < 0 || b < 0 || x < 0) return 0;
    if (a == 0) {
        if (b == 0) return 1;
        return comb(x + 1, b);
    }
    long long res = 0;
    int max_k = min(a - 1, b);
    for (int k = 0; k <= max_k; ++k) {
        if (a - k > x + 1) continue;
        long long c1 = comb(a - 1, k);
        long long c2 = comb(x + 1, a - k);
        long long c3 = comb(a + x + 1 - k, b - k);
        long long term = (c1 * c2) % MOD * c3 % MOD;
        res += term;
        if (res >= MOD) res -= MOD;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, A, B;
    if (!(cin >> N >> A >> B)) return 0;

    int max_val = N + 5;
    precompute(max_val);

    int x = N - A - B;

    long long t1 = f(A, B, x);
    long long t2 = f(B - 1, A, x);
    long long t3 = f(B - 1, A, x - 1);
    long long t4 = f(B - 1, A + 1, x - 1);

    long long ans = (t1 - t2 - t3 - t4) % MOD;
    if (ans < 0) ans += MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
