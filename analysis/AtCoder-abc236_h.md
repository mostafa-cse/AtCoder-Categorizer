# Problem Analysis: AtCoder-abc236_h — Ex. Distinct Multiples

**Problem ID**: `AtCoder-abc236_h`  
**Contest**: `abc236`  
**Rating / Difficulty**: 2898  
**URL**: https://atcoder.jp/contests/abc236/tasks/abc236_h  
**VJudge Tag**: `[problem:AtCoder-abc236_h]`  
**Category File**: [`../categories/combinatorics/distinct_multiples_partition_lattice.md`](../categories/combinatorics/distinct_multiples_partition_lattice.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Inclusion Exclusion on Multiples`  

---

## 1. Problem Statement & Key Idea
Given an array D of N integers and upper bound M, count sequences (x_1, ..., x_N) such that 1 <= x_i <= M, D_i divides x_i, and all x_i are pairwise distinct, modulo 998244353.

## 2. Core Observation & Invariant
The condition that all x_i are distinct can be inverted over the set partition lattice Pi_N using Möbius inversion. For any partition P of {1, ..., N}, setting all elements in block B to be equal means their common value is a multiple of lcm_{i in B}(D_i) <= M, giving floor(M / lcm(B)) choices. The Möbius weight of block B is (-1)^{|B|-1} (|B|-1)!. The problem reduces to finding the sum of products of block weights over all partitions of {1, ..., N}, which can be solved via subset DP / SOS convolution in O(3^N) time.

## 3. Step-by-Step Algorithm
1. 1. For each subset S subseteq {1, ..., N}, compute L(S) = lcm_{i in S}(D_i) (capped at M+1) and block weight w(S) = (-1)^{|S|-1} (|S|-1)! * floor(M / L(S)) mod 998244353.
2. 2. Fix lowest bit of submask to avoid permutation overcounting in partition DP.
3. 3. Compute DP[mask] = sum_{sub} DP[mask \ sub] * w(sub).
4. 4. Return DP[(1 << N) - 1] mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(3^N)`
- **Space Complexity**: `O(2^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

static const long long MOD = 998244353;

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

long long lcm_ll(long long a, long long b, long long limit) {
    if (a > limit || b > limit) return limit + 1;
    long long g = gcd_ll(a, b);
    long long a_div = a / g;
    // Check overflow: a_div * b > limit
    if ((__int128)a_div * b > limit) return limit + 1;
    return a_div * b;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> d(n);
    for (int i = 0; i < n; ++i) {
        cin >> d[i];
    }

    int total_masks = (1 << n);
    vector<long long> lcms(total_masks, 1);
    for (int mask = 1; mask < total_masks; ++mask) {
        int i = __builtin_ctz(mask);
        int prev_mask = mask ^ (1 << i);
        lcms[mask] = lcm_ll(lcms[prev_mask], d[i], m);
    }

    vector<long long> fact(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
        fact[i] = fact[i - 1] * i % MOD;
    }

    vector<long long> f(total_masks, 0);
    for (int mask = 1; mask < total_masks; ++mask) {
        int sz = __builtin_popcount(mask);
        long long mult_count = (lcms[mask] <= m ? (m / lcms[mask]) % MOD : 0);
        long long coeff = fact[sz - 1] * mult_count % MOD;
        if ((sz - 1) % 2 == 1) {
            coeff = (MOD - coeff) % MOD;
        }
        f[mask] = coeff;
    }

    vector<long long> dp(total_masks, 0);
    dp[0] = 1;

    for (int mask = 1; mask < total_masks; ++mask) {
        int low_bit = mask & (-mask);
        int rest = mask ^ low_bit;

        // Iterate through all submasks of rest
        for (int sub = rest; ; sub = (sub - 1) & rest) {
            int T = sub | low_bit;
            dp[mask] = (dp[mask] + f[T] * dp[mask ^ T]) % MOD;
            if (sub == 0) break;
        }
    }

    cout << dp[total_masks - 1] << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
