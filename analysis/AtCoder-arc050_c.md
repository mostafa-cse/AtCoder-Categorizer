# Problem Analysis: AtCoder-arc050_c — C. LCM 111

**Problem ID**: `AtCoder-arc050_c`  
**Contest**: `arc050`  
**Rating / Difficulty**: 2372  
**URL**: https://atcoder.jp/contests/arc050/tasks/arc050_c  
**VJudge Tag**: `[problem:AtCoder-arc050_c]`  
**Category File**: [`../categories/math/repunit_lcm_matrix_exponentiation.md`](../categories/math/repunit_lcm_matrix_exponentiation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
Compute $\text{lcm}(R_A, R_B) \pmod M$ for repunits. Using $\gcd(R_A, R_B) = R_{\gcd(A, B)}$, the LCM factors into two geometric series $R_A$ and $\sum (10^{\gcd(A, B)})^j$, each evaluated via $2 \times 2$ matrix exponentiation in $O(\log A + \log B)$.

## 2. Core Observation & Invariant
For repunits $R_k = (10^k - 1)/9$, $\gcd(R_A, R_B) = R_{\gcd(A, B)}$. Consequently, $\text{lcm}(R_A, R_B) = R_A \cdot \frac{R_B}{R_{\gcd(A, B)}} = R_A \sum_{j=0}^{B/\gcd(A, B) - 1} (10^{\gcd(A, B)})^j$. Both factors are geometric sums $\sum_{i=0}^{L-1} r^i$ evaluated modulo $M$ via $2 \times 2$ matrix exponentiation.

## 3. Step-by-Step Algorithm
1. Compute $g = \gcd(A, B)$.
2. Compute $R_A \pmod M$ as the top-right entry of $\begin{pmatrix} 10 & 1 \\ 0 & 1 \end{pmatrix}^A$.
3. Compute $S = \sum_{j=0}^{B/g - 1} (10^g)^j \pmod M$ as the top-right entry of $\begin{pmatrix} 10^g & 1 \\ 0 & 1 \end{pmatrix}^{B/g}$.
4. Multiply $(R_A \bmod M) \cdot (S \bmod M) \pmod M$ in $O(\log A + \log B)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(\log A + \log B)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

typedef unsigned __int128 u128;

long long gcd(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

struct Matrix {
    long long mat[2][2];
    Matrix() {
        mat[0][0] = mat[0][1] = mat[1][0] = mat[1][1] = 0;
    }
};

Matrix multiply(const Matrix& A, const Matrix& B, long long m) {
    Matrix C;
    for (int i = 0; i < 2; i++) {
        for (int k = 0; k < 2; k++) {
            for (int j = 0; j < 2; j++) {
                C.mat[i][j] = (C.mat[i][j] + (u128)A.mat[i][k] * B.mat[k][j]) % m;
            }
        }
    }
    return C;
}

Matrix power(Matrix A, long long p, long long m) {
    Matrix res;
    res.mat[0][0] = res.mat[1][1] = 1;
    while (p > 0) {
        if (p & 1) res = multiply(res, A, m);
        A = multiply(A, A, m);
        p >>= 1;
    }
    return res;
}

long long power_mod(long long base, long long exp, long long mod) {
    long long res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = ((u128)res * base) % mod;
        base = ((u128)base * base) % mod;
        exp /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    long long g = gcd(a, b);

    // R_A mod m: top-right entry of [10, 1; 0, 1]^A
    Matrix M1;
    M1.mat[0][0] = 10 % m;
    M1.mat[0][1] = 1;
    M1.mat[1][0] = 0;
    M1.mat[1][1] = 1;

    Matrix res1 = power(M1, a, m);
    long long r_a = res1.mat[0][1];

    // S = sum_{j=0}^{b/g - 1} (10^g)^j mod m
    long long r2 = power_mod(10, g, m);
    Matrix M2;
    M2.mat[0][0] = r2;
    M2.mat[0][1] = 1;
    M2.mat[1][0] = 0;
    M2.mat[1][1] = 1;

    Matrix res2 = power(M2, b / g, m);
    long long s = res2.mat[0][1];

    long long ans = ((u128)r_a * s) % m;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
