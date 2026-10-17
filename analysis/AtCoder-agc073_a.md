# Problem Analysis: AtCoder-agc073_a — Chords and Checkered

**Problem ID**: `AtCoder-agc073_a`  
**Contest**: `agc073`  
**Rating / Difficulty**: 2219  
**URL**: https://atcoder.jp/contests/agc073/tasks/agc073_a  
**VJudge Tag**: `[problem:AtCoder-agc073_a]`  
**Category File**: [`../categories/math/chords_and_checkered_euler_characteristic_expectation.md`](../categories/math/chords_and_checkered_euler_characteristic_expectation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Given circle circumference L, chord length K (2K < L), and N chords starting at coordinates A_i, find the total number of black regions across all 2^N chord subsets colored in chessboard fashion starting with center region white.

## 2. Core Observation & Invariant
By Euler characteristic and region weighting: assign weight 1/2 to chord endpoints along circular arcs and weight 1 to the unique deepest vertex of interior black regions. In a random chord subset, endpoints receive expected weight 1/4 (total 3N/8), and chord intersections receive expected weight 1/8 if another chord separates them from the center. The total expected weight simplifies to (3N + I + V) / 8, where I is intersecting chord pairs and V counts A_i + K <= A_{i+1}.

## 3. Step-by-Step Algorithm
1. 1. Count V: the number of i in [1, N] such that A_i + K <= A_{i+1} (with A_{N+1} = A_1 + L).
2. 2. Count I: pairs of intersecting chords. Two equal-length chords intersect iff circular clockwise distance between their starting points is < K, computed in O(N) using two pointers on the duplicated sequence.
3. 3. Total answer is 2^{N - 3} * (3N + I + V) mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N) or O(N) after sort`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
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

long long modInverse(long long n) {
    return power(n, MOD - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, K;
    int n;
    if (!(cin >> L >> K >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    // V: count of i such that A[i] + K <= A[i+1]
    long long V = 0;
    for (int i = 0; i < n; i++) {
        long long next_val = (i + 1 < n ? a[i + 1] : a[0] + L);
        if (a[i] + K <= next_val) {
            V++;
        }
    }

    // I: number of pairs of intersecting chords
    // Chords intersect iff clockwise distance between starts is < K
    vector<long long> a2 = a;
    for (int i = 0; i < n; i++) a2.push_back(a[i] + L);

    long long I = 0;
    int r = 0;
    for (int i = 0; i < n; i++) {
        while (r < (int)a2.size() && a2[r] - a[i] < K) {
            r++;
        }
        I = (I + max(0, r - 1 - i)) % MOD;
    }

    long long sum_val = (3LL * n + I + V) % MOD;
    long long inv8 = modInverse(8);
    long long pow2 = power(2, n);
    long long ans = (pow2 * inv8) % MOD;
    ans = (ans * sum_val) % MOD;

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
