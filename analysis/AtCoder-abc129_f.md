# Problem Analysis: AtCoder-abc129_f — F - Takahashi's Basics in Education and Learning

**Problem ID**: `AtCoder-abc129_f`  
**Contest**: `abc129`  
**Rating / Difficulty**: 2621  
**URL**: https://atcoder.jp/contests/abc129/tasks/abc129_f  
**VJudge Tag**: `[problem:AtCoder-abc129_f]`  
**Category File**: [`../categories/math/takahashi_education_matrix_exponentiation.md`](../categories/math/takahashi_education_matrix_exponentiation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
Concatenate the first L terms of an arithmetic progression A, A+B, ..., A+(L-1)B into a decimal integer and compute its value modulo M.

## 2. Core Observation & Invariant
The decimal length d of terms ranges from 1 to 18. Within each block of terms having the same number of digits d, appending term s_i = s_0 + i B transforms running value V as V <- V * 10^d + s_i. The state vector (V, i, 1)^T transitions linearly via a 3x3 matrix T_d. Binary matrix exponentiation allows computing the transition over cnt terms in O(log cnt).

## 3. Step-by-Step Algorithm
1. For each digit length d in [1, 18]: determine the index interval [l, r] where 10^(d-1) <= A + i B < 10^d.
2. Intersect [l, r] with [0, L - 1] to obtain count cnt.
3. Construct the 3x3 transition matrix T for digit length d.
4. Compute T^cnt modulo M using binary matrix exponentiation.
5. Apply T^cnt to the state vector (V, 0, 1)^T.
6. Output the accumulated value V modulo M.

## 4. Complexity Analysis
- **Time Complexity**: `O(\text{digits} \log L)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

using ll = long long;

struct Matrix {
    ll mat[3][3];
    Matrix() {
        for (int i = 0; i < 3; ++i)
            for (int j = 0; j < 3; ++j)
                mat[i][j] = 0;
    }
};

Matrix multiply(const Matrix& A, const Matrix& B, ll M) {
    Matrix C;
    for (int i = 0; i < 3; ++i) {
        for (int k = 0; k < 3; ++k) {
            if (A.mat[i][k] == 0) continue;
            for (int j = 0; j < 3; ++j) {
                C.mat[i][j] = (C.mat[i][j] + (__int128)A.mat[i][k] * B.mat[k][j]) % M;
            }
        }
    }
    return C;
}

Matrix power(Matrix A, ll p, ll M) {
    Matrix res;
    for (int i = 0; i < 3; ++i) res.mat[i][i] = 1;
    while (p > 0) {
        if (p & 1) res = multiply(res, A, M);
        A = multiply(A, A, M);
        p >>= 1;
    }
    return res;
}

ll power_mod(ll base, ll exp, ll mod) {
    ll res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = (__int128)res * base % mod;
        base = (__int128)base * base % mod;
        exp >>= 1;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll L, A, B, M;
    if (!(cin >> L >> A >> B >> M)) return 0;

    ll V = 0;
    ll cur_idx = 0;
    __int128 pow10 = 1;

    for (int d = 1; d <= 18; ++d) {
        __int128 low = pow10;
        __int128 high = pow10 * 10 - 1;
        pow10 *= 10;

        ll l = 0;
        if (low > A) {
            l = (ll)((low - A + B - 1) / B);
        }

        if (high < A) continue;
        ll r = (ll)((high - A) / B);

        l = max(l, cur_idx);
        r = min(r, L - 1);
        if (l > r) continue;

        ll cnt = r - l + 1;
        ll ten_d = power_mod(10, d, M);
        ll S0 = (A + (__int128)B * l) % M;
        ll b_mod = B % M;

        Matrix T;
        T.mat[0][0] = ten_d;
        T.mat[0][1] = b_mod;
        T.mat[0][2] = S0;
        T.mat[1][1] = 1;
        T.mat[1][2] = 1;
        T.mat[2][2] = 1;

        Matrix T_pow = power(T, cnt, M);
        V = ((__int128)T_pow.mat[0][0] * V + T_pow.mat[0][2]) % M;

        cur_idx = r + 1;
        if (cur_idx >= L) break;
    }

    cout << (V % M + M) % M << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
