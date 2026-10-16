# Problem Analysis: AtCoder-dp_r — Walk

**Problem ID**: `AtCoder-dp_r`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1700  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_r  
**VJudge Tag**: `[problem:AtCoder-dp_r]`  
**Category File**: [`../categories/dp/matrix_exponentiation.md`](../categories/dp/matrix_exponentiation.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Matrix Exponentiation DP`  

---

## 1. Problem Statement & Key Idea
Given a directed graph with N vertices (N <= 50), count the number of directed paths of exact length K (K <= 10^18) modulo 10^9+7.

**Core Idea**: The number of paths of length K between all pairs of vertices is given by A^K, where A is the adjacency matrix.

## 2. Core Observation & Invariant
Matrix multiplication computes transitions; binary exponentiation solves K <= 10^18 in O(N^3 log K) steps.

## 3. Step-by-Step Algorithm
1. Construct adjacency matrix A.
2. Compute M = A^K mod (10^9+7) using binary matrix exponentiation.
3. Total paths = sum_{i, j} M[i][j] mod MOD.

## 4. Complexity Analysis
Time: O(N^3 log K), Space: O(N^2).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;
using Matrix = vector<vector<long long>>;

Matrix multiply(const Matrix& A, const Matrix& B, int n) {
    Matrix C(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < n; ++j) {
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
            }
        }
    }
    return C;
}

Matrix power(Matrix A, long long p, int n) {
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; ++i) res[i][i] = 1;
    while (p > 0) {
        if (p & 1) res = multiply(res, A, n);
        A = multiply(A, A, n);
        p >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    Matrix A(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> A[i][j];
    }

    Matrix Ak = power(A, k, n);
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            ans = (ans + Ak[i][j]) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matrix exponentiation for path counting on graphs.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Formulating linear state recurrences as matrix products and exponentiating large step counts.
- **Reusable Pattern**: `Matrix exponentiation DP for enormous transition steps.`

---
Back to [Matrix Exponentiation DP](../categories/dp/matrix_exponentiation.md) | [Categories Directory](../categories/README.md)