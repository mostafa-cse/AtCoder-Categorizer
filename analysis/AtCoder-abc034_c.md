# Problem Analysis: AtCoder-abc034_c — Grid Paths

**Problem ID**: `AtCoder-abc034_c`  
**Contest**: `abc034`  
**Rating / Difficulty**: 1440  
**URL**: https://atcoder.jp/contests/abc034/tasks/abc034_c  
**VJudge Tag**: `[problem:AtCoder-abc034_c]`  
**Category File**: [`../categories/combinatorics/grid_path_combinations_mod_inverse.md`](../categories/combinatorics/grid_path_combinations_mod_inverse.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Classic Combinatorics`  
- **Topic (Skill)**: `Large Grid Path Combinations via Modular Inverse Factorials`  

---

## 1. Problem Statement & Key Idea
In a W x H grid, find the number of shortest paths from cell (1, 1) to (W, H) moving only right and down, modulo 10^9 + 7. W, H <= 10^5.

**Key Insight**: The total number of right moves is W - 1 and down moves is H - 1. Total moves = (W - 1) + (H - 1). The answer is C(W + H - 2, W - 1) mod (10^9 + 7).

## 2. Core Observation & Invariant
Precomputing factorials and inverse factorials up to 2 * 10^5 in O(W + H) time using Fermat's Little Theorem allows O(1) combination evaluation.

## 3. Step-by-Step Algorithm
1. Precompute factorial table fact[i] = fact[i-1] * i % MOD up to 200,000.
2. Compute modular inverse of fact[MAX] using binary exponentiation (Fermat's Little Theorem): power(fact[MAX], MOD - 2).
3. Precompute invFact[i-1] = invFact[i] * i % MOD down to 0.
4. Compute C(n, k) = fact[n] * invFact[k] % MOD * invFact[n-k] % MOD.
5. Evaluate C(W + H - 2, W - 1) and print result.

## 4. Complexity Analysis
- **Time Complexity**: `O(W + H)`
- **Space Complexity**: `O(W + H)`

## 5. Complete C++ Solution
```cpp
#include <iostream>

using namespace std;

const int MOD = 1000000007;
const int MAX = 200005;

long long fact[MAX], invFact[MAX];

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

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAX; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAX - 1] = modInverse(fact[MAX - 1]);
    for (int i = MAX - 2; i >= 1; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int w, h;
    if (!(cin >> w >> h)) return 0;

    cout << nCr(w + h - 2, w - 1) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Modular inverse factorial precomputation for O(1) combination queries.
- **Reusable Pattern**: `Combinatorics Boilerplate: fact[] and invFact[] with Fermat's Little Theorem.`
