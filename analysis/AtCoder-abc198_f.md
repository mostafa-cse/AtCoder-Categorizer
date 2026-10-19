# Problem Analysis: AtCoder-abc198_f — F - Cube

**Problem ID**: `AtCoder-abc198_f`  
**Contest**: `abc198`  
**Rating / Difficulty**: 2769  
**URL**: https://atcoder.jp/contests/abc198/tasks/abc198_f  
**VJudge Tag**: `[problem:AtCoder-abc198_f]`  
**Category File**: [`../categories/miscellaneous/cube_face_coloring_burnside_polya.md`](../categories/miscellaneous/cube_face_coloring_burnside_polya.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `General`  
- **Topic (Skill)**: `Burnside's Lemma / Polya Enumeration Theorem`  

---

## 1. Problem Statement & Key Idea
Given an integer S, compute the number of ways to write a positive integer on each of the six faces of a cube such that their sum equals S, modulo 998244353. Two cubes are considered identical if one can be rotated in 3D space to match the other.

## 2. Core Observation & Invariant
By Burnside's Lemma / Polya Enumeration Theorem, the number of distinct rotational orbits under the cube's rotation group G (of order 24) equals (1/24) * sum_{g in G} Fix(g). The 24 symmetries fall into 5 conjugacy classes according to cycle partitions of the 6 faces:
1. Identity (1 rotation): cycle type 1^6 -> x1 + x2 + x3 + x4 + x5 + x6 = S with xi >= 1. Solutions: C(S - 1, 5).
2. 90-degree and 270-degree face rotations (6 rotations): cycle type 1^2 4^1 -> x1 + x2 + 4*x3 = S with xi >= 1.
3. 180-degree face rotations (3 rotations): cycle type 1^2 2^2 -> x1 + x2 + 2*x3 + 2*x4 = S with xi >= 1.
4. 120-degree vertex rotations (8 rotations): cycle type 3^2 -> 3*x1 + 3*x2 = S with xi >= 1 (non-zero iff 3 | S, count = S/3 - 1).
5. 180-degree edge rotations (6 rotations): cycle type 2^3 -> 2*x1 + 2*x2 + 2*x3 = S with xi >= 1 (non-zero iff 2 | S, count = C(S/2 - 1, 2)).
Each equation sum ci * xi = S with xi >= 1 can be counted using generating functions, binomial coefficients, or closed arithmetic series in O(1) or small loops.

## 3. Step-by-Step Algorithm
1. 1. Compute combinations C(S - 1, 5) for the identity rotation.
2. 2. For 90-degree face rotations, iterate x3 from 1 to (S - 2)/4 and sum (S - 1 - 4*x3) using arithmetic sum formulas.
3. 3. For 180-degree face rotations, express x1 + x2 + 2*(x3 + x4) = S. Let k = x3 + x4 >= 2, ways for (x1, x2) is S - 1 - 2*k, and ways for (x3, x4) is k - 1. Sum over k in closed form.
4. 4. For 120-degree vertex rotations, if S % 3 == 0 and S >= 6, ways is S/3 - 1; else 0.
5. 5. For 180-degree edge rotations, if S % 2 == 0 and S >= 6, ways is C(S/2 - 1, 2); else 0.
6. 6. Multiply each term by its conjugacy class size (1, 6, 3, 8, 6), sum modulo 998244353, and multiply by 24^(-1) mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

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

// C(n, k) mod MOD where n can be large, k is small
long long comb(long long n, int k) {
    if (n < k || k < 0) return 0;
    long long num = 1, den = 1;
    for (int i = 1; i <= k; ++i) {
        num = (num * ((n - i + 1) % MOD)) % MOD;
        den = (den * i) % MOD;
    }
    return (num * modInverse(den)) % MOD;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long S;
    if (!(cin >> S)) return 0;

    // 1. Identity (1 rotation): C(S - 1, 5)
    long long term_id = comb(S - 1, 5);

    // 2. 90/270 deg face rotations (6 rotations): x1 + x2 + 4*x3 = S
    // x1 + x2 = S - 4*x3. For each x3 >= 1, ways = S - 1 - 4*x3.
    // x3 from 1 to K = (S - 2) / 4.
    long long term_90 = 0;
    if (S >= 6) {
        long long K = (S - 2) / 4;
        if (K >= 1) {
            long long k_mod = K % MOD;
            long long s1_mod = (S - 1) % MOD;
            long long sum_1 = (k_mod * s1_mod) % MOD;
            long long sum_i = (k_mod * ((K + 1) % MOD)) % MOD;
            sum_i = (sum_i * modInverse(2)) % MOD;
            long long sum_4i = (4 * sum_i) % MOD;
            term_90 = (sum_1 - sum_4i + MOD) % MOD;
        }
    }
    term_90 = (term_90 * 6) % MOD;

    // 3. 180 deg face rotations (3 rotations): x1 + x2 + 2*(x3 + x4) = S
    // Let B = x3 + x4 >= 2. A = x1 + x2 = S - 2*B >= 2.
    // Ways = (A - 1)*(B - 1) = (S - 1 - 2*B)*(B - 1).
    // Let j = B - 1, then B = j + 1.
    // S - 1 - 2*(j + 1) = S - 3 - 2*j.
    // j runs from 1 to M = (S - 2)/2 - 1.
    long long term_180_face = 0;
    if (S >= 6) {
        long long B_max = (S - 2) / 2;
        long long M = B_max - 1;
        if (M >= 1) {
            long long m_mod = M % MOD;
            long long s3_mod = (S - 3) % MOD;
            // sum of j: M*(M+1)/2
            long long sum_j = (m_mod * ((M + 1) % MOD)) % MOD;
            sum_j = (sum_j * modInverse(2)) % MOD;
            // sum of j^2: M*(M+1)*(2M+1)/6
            long long sum_j2 = (m_mod * ((M + 1) % MOD)) % MOD;
            sum_j2 = (sum_j2 * ((2 * M + 1) % MOD)) % MOD;
            sum_j2 = (sum_j2 * modInverse(6)) % MOD;

            long long part1 = (s3_mod * sum_j) % MOD;
            long long part2 = (2 * sum_j2) % MOD;
            term_180_face = (part1 - part2 + MOD) % MOD;
        }
    }
    term_180_face = (term_180_face * 3) % MOD;

    // 4. 120/240 deg vertex rotations (8 rotations): 3*x1 + 3*x2 = S
    // S must be div by 3. If S % 3 == 0: x1 + x2 = S/3, ways = S/3 - 1.
    long long term_120_vert = 0;
    if (S % 3 == 0) {
        long long s_div = S / 3;
        if (s_div >= 2) {
            term_120_vert = (s_div - 1) % MOD;
        }
    }
    term_120_vert = (term_120_vert * 8) % MOD;

    // 5. 180 deg edge rotations (6 rotations): 2*x1 + 2*x2 + 2*x3 = S
    // S must be div by 2. If S % 2 == 0: x1 + x2 + x3 = S/2, ways = C(S/2 - 1, 2).
    long long term_180_edge = 0;
    if (S % 2 == 0) {
        long long s_div = S / 2;
        if (s_div >= 3) {
            term_180_edge = comb(s_div - 1, 2);
        }
    }
    term_180_edge = (term_180_edge * 6) % MOD;

    long long total = (term_id + term_90 + term_180_face + term_120_vert + term_180_edge) % MOD;
    long long ans = (total * modInverse(24)) % MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
