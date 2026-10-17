# Problem Analysis: AtCoder-abc009_4 — 漸化式

**Problem ID**: `AtCoder-abc009_4`  
**Contest**: `abc009`  
**Rating / Difficulty**: 2213  
**URL**: https://atcoder.jp/contests/abc009/tasks/abc009_4  
**VJudge Tag**: `[problem:AtCoder-abc009_4]`  
**Category File**: [`../categories/math/recurrence_matrix_exponentiation_bitwise_and_xor_semiring.md`](../categories/math/recurrence_matrix_exponentiation_bitwise_and_xor_semiring.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
Matrix exponentiation over the bitwise (AND, XOR) semiring to compute linear recurrence in logarithmic time.

## 2. Core Observation & Invariant
The recurrence A_{N+K} = bigoplus (C_j AND A_{N+K-j}) is a linear recurrence over the semiring (S, XOR, AND), where addition is XOR and multiplication is bitwise AND. The additive identity (zero) is 0, and the multiplicative identity (one) is ~0U (all 1s, 2^32 - 1).

## 3. Step-by-Step Algorithm
1. 1. If M <= K, answer is A[M-1].
2. 2. Construct K x K transition matrix T: row 0 has C_1, ..., C_K, and row i has ~0U at column i - 1 and 0 elsewhere.
3. 3. Compute T^{M - K} using binary matrix exponentiation under (AND, XOR) matrix multiplication.
4. 4. Multiply the first row of T^{M - K} by vector [A_K, ..., A_1]^T to obtain A_M.

## 4. Complexity Analysis
- **Time Complexity**: `O(K^3 log M)`
- **Space Complexity**: `O(K^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using uint = unsigned int;

int K;
using Matrix = vector<vector<uint>>;

Matrix multiply(const Matrix& A, const Matrix& B) {
    Matrix C(K, vector<uint>(K, 0));
    for (int i = 0; i < K; ++i) {
        for (int k = 0; k < K; ++k) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < K; ++j) {
                C[i][j] ^= (A[i][k] & B[k][j]);
            }
        }
    }
    return C;
}

Matrix power(Matrix A, long long exp) {
    Matrix res(K, vector<uint>(K, 0));
    for (int i = 0; i < K; ++i) {
        res[i][i] = ~0U;
    }
    while (exp > 0) {
        if (exp & 1) res = multiply(res, A);
        A = multiply(A, A);
        exp >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long M;
    if (!(cin >> K >> M)) return 0;

    vector<uint> A(K), C(K);
    for (int i = 0; i < K; ++i) cin >> A[i];
    for (int i = 0; i < K; ++i) cin >> C[i];

    if (M <= K) {
        cout << A[M - 1] << "\n";
        return 0;
    }

    Matrix T(K, vector<uint>(K, 0));
    for (int j = 0; j < K; ++j) {
        T[0][j] = C[j];
    }
    for (int i = 1; i < K; ++i) {
        T[i][i - 1] = ~0U;
    }

    Matrix TM = power(T, M - K);

    uint ans = 0;
    for (int j = 0; j < K; ++j) {
        ans ^= (TM[0][j] & A[K - 1 - j]);
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
