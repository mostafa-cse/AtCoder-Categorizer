# Problem Analysis: AtCoder-typical90_o — Don't be too close

**Problem ID**: `AtCoder-typical90_o`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 015)  
**Rating / Difficulty**: 2150 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_o  
**VJudge Tag**: `[problem:AtCoder-typical90_o]`  
**Category File**: [`../categories/combinatorics/stars_and_bars_harmonic.md`](../categories/combinatorics/stars_and_bars_harmonic.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Stars and Bars & Combinatorial Bounds`  
- **Topic (Skill)**: `Spacing Constraint Combinatorics + Harmonic Series O(N log N)`  

---

## 1. Problem Statement & Key Idea
For each k from 1 to N, count non-empty subsets of {1, 2, ..., N} such that any two chosen elements have absolute difference >= k. Output modulo 10^9+7.

**Core Idea**: Choosing m elements with spacing >= k from {1..N} maps by variable transformation to choosing m elements from N - (k - 1)*(m - 1) items: C(N - (k - 1)*(m - 1), m).

## 2. Core Observation & Invariant
For fixed k, max elements m <= ceil(N/k). Summing m over all k in [1, N] gives sum_{k=1}^N (N/k) = O(N log N) total evaluations!

## 3. Step-by-Step Algorithm
1. Precompute factorials and inverse factorials up to N.
2. For each k from 1 to N:
   - ans = 0
   - for m from 1 to (N + k - 1) / k:
     - total_items = N - (k - 1) * (m - 1)
     - if total_items >= m: ans = (ans + nCr(total_items, m)) % MOD
   - Output ans.

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return res;
}

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

const int MAXN = 100005;
long long fact[MAXN], invFact[MAXN];

void precompute() {
    fact[0] = 1;
    invFact[0] = 1;
    for (int i = 1; i < MAXN; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[MAXN - 1] = modInverse(fact[MAXN - 1]);
    for (int i = MAXN - 2; i >= 1; --i) {
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

    int n;
    if (!(cin >> n)) return 0;

    precompute();

    for (int k = 1; k <= n; ++k) {
        long long ans = 0;
        int max_m = (n + k - 1) / k;
        for (int m = 1; m <= max_m; ++m) {
            long long rem = n - (long long)(k - 1) * (m - 1);
            if (rem >= m) {
                ans = (ans + nCr(rem, m)) % MOD;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Stars and bars reduction with harmonic series complexity bound.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Spacing constraint bijection to standard combinations and bounding loop iterations via harmonic series.
- **Reusable Pattern**: `Combinatorial spacing reduction + Harmonic Series loop.`

---
Back to [Spacing Constraint Combinatorics + Harmonic Series O(N log N)](../categories/combinatorics/stars_and_bars_harmonic.md) | [Categories Directory](../categories/README.md)