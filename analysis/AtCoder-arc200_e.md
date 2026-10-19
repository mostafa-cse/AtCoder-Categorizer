# Problem Analysis: AtCoder-arc200_e — E - popcount <= 2

**Problem ID**: `AtCoder-arc200_e`  
**Contest**: `arc200`  
**Rating / Difficulty**: 2852  
**URL**: https://atcoder.jp/contests/arc200/tasks/arc200_e  
**VJudge Tag**: `[problem:AtCoder-arc200_e]`  
**Category File**: [`../categories/combinatorics/hamming_distance_two_subsets_combinatorics.md`](../categories/combinatorics/hamming_distance_two_subsets_combinatorics.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Basic Counting`  
- **Topic (Skill)**: `Permutations, Combinations and Basic Counting Problems`  

---

## 1. Problem Statement & Key Idea
Given N and K, count the number of subsets of size K of binary strings of length N such that every pair of strings in the subset has Hamming distance at most 2, modulo 998244353.

## 2. Core Observation & Invariant
By shifting the entire set so that one string is 0^N, all strings in the set must have popcount <= 2, and the Hamming distance between any two strings must be <= 2. The intersection graph of pairs of bits forms a family of sets of size <= 2. There are only two geometric configurations that satisfy pairwise distance <= 2: (1) a star graph (all pairs share a common coordinate bit), or (2) a triangle of size 3 (three 2-element sets on 3 coordinates), plus singleton elements. By classifying the configuration into star-type families and small cliques (triangles, 4-cliques), each case can be counted independently using binomial coefficients.

## 3. Step-by-Step Algorithm
1. 1. Consider translation invariance: classify by maximal distance configuration.
2. 2. Count subsets with diameter <= 1 (all pairs distance <= 1).
3. 3. Count subsets with diameter 2: classify into star configurations (all 2-element strings share a common coordinate) and triangle/small clique configurations.
4. 4. Apply inclusion-exclusion between overlapping configurations.
5. 5. Output total modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>

using namespace std;

static const long long MOD = 998244353;

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

static const long long two_inv = modInverse(2);
static const long long six_inv = modInverse(6);

long long c2(long long n) {
    n %= MOD;
    return n * (n - 1 + MOD) % MOD * two_inv % MOD;
}

long long c3(long long n) {
    n %= MOD;
    long long term = n * (n - 1 + MOD) % MOD * (n - 2 + MOD) % MOD;
    return term * six_inv % MOD;
}

void solve() {
    long long n, m;
    if (!(cin >> n >> m)) return;

    long long n2 = power(2, n - 1);
    long long n3 = power(3, n - 1);
    long long n4 = power(4, n - 1);
    long long nm1 = power(m + 1, n - 1);

    long long ans = 0;
    // |S| = 0
    ans = (ans + nm1) % MOD;

    // |S| = 1
    long long part1 = c2(m) * ((n4 - n3 + MOD) % MOD) % MOD;
    ans = (ans + part1) % MOD;

    // |S| >= 2, total AND is 0
    long long ko2 = (n4 - 3 * n3 % MOD + 3 * n2 % MOD - 1) % MOD;
    ko2 = (ko2 + 10 * MOD) % MOD;
    long long part2 = c3(m) * ko2 % MOD;
    ans = (ans + part2) % MOD;

    // |S| >= 2, total AND is not 0 (star around bit k)
    long long ko3 = (nm1 - n2 - (m - 1) % MOD * ((n3 - n2 + MOD) % MOD)) % MOD;
    ko3 = (ko3 + 10 * MOD) % MOD;
    long long part3 = (m % MOD) * ko3 % MOD;
    ans = (ans + part3) % MOD;

    ans = (ans * power(2, m)) % MOD;
    cout << ans << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (cin >> T) {
        while (T--) {
            solve();
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
