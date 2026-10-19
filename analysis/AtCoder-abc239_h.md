# Problem Analysis: AtCoder-abc239_h — Dice Product 2

**Problem ID**: `AtCoder-abc239_h`  
**Contest**: `abc239`  
**Rating / Difficulty**: 2686  
**URL**: https://atcoder.jp/contests/abc239/tasks/abc239_h  
**VJudge Tag**: `[problem:AtCoder-abc239_h]`  
**Category File**: [`../categories/number_theory/dice_product_dirichlet_convolution.md`](../categories/number_theory/dice_product_dirichlet_convolution.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Multiplicative Functions`  
- **Topic (Skill)**: `Dirichlet convolution`  

---

## 1. Problem Statement & Key Idea
An N-sided die with faces 1..N multiplies an initial product P=1 until P > M. Find expected turns modulo 10^9+7. The expected remaining turns f(v) with target threshold v = floor(M / P) satisfies (N - 1) f(v) = N + sum_{X=2}^{min(N, v)} f(floor(v / X)). Because floor(v / X) takes at most 2*sqrt(v) distinct values, quotient chunking computes f(M) across all O(sqrt(M)) states in O(M^{3/4}) time.

## 2. Core Observation & Invariant
The state space consists only of integers of the form floor(M / k). For M <= 10^9, there are at most 2*sqrt(M) approx 63245 such states. In the sum over X, intervals of X where floor(v / X) = q are handled simultaneously as (r - l + 1) * f(q). Using dual-array indexing provides O(1) state lookups with zero hash collisions.

## 3. Step-by-Step Algorithm
1. 1. Precompute modular inverse (N - 1)^{-1} mod (10^9+7).
2. 2. Allocate memo tables dp_1 and dp_2 of size sqrt(M) + 5.
3. 3. Recursive function get_f(v): check memo, iterate in quotient blocks l..r with q = floor(v / l), accumulate (r - l + 1) * get_f(q).
4. 4. Return and memoize f(v) = (N + total) * (N - 1)^{-1} mod (10^9+7).
5. 5. Output get_f(M).

## 4. Complexity Analysis
- **Time Complexity**: `O(M^{3/4})`
- **Space Complexity**: `O(sqrt(M))`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const long long MOD = 1000000007;

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

long long N, M;
long long inv_N_minus_1;
int K;
vector<long long> dp1, dp2;

long long get_f(long long v) {
    if (v == 0) return 0;
    if (v <= K) {
        if (dp1[v] != -1) return dp1[v];
    } else {
        long long q = M / v;
        if (dp2[q] != -1) return dp2[q];
    }

    long long limit = min(N, v);
    long long total = 0;
    long long l = 2;
    while (l <= limit) {
        long long q = v / l;
        long long r = min(v / q, limit);
        long long cnt = (r - l + 1) % MOD;
        total = (total + cnt * get_f(q)) % MOD;
        l = r + 1;
    }

    long long res = (N + total) % MOD * inv_N_minus_1 % MOD;
    if (v <= K) {
        dp1[v] = res;
    } else {
        dp2[M / v] = res;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> M)) return 0;

    inv_N_minus_1 = modInverse(N - 1);
    K = sqrt(M) + 5;
    dp1.assign(K + 1, -1);
    dp2.assign(K + 1, -1);

    cout << get_f(M) << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
