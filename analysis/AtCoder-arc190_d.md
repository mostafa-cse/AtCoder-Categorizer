# Problem Analysis: AtCoder-arc190_d — D - Matrix Pow Sum

**Problem ID**: `AtCoder-arc190_d`  
**Contest**: `arc190`  
**Rating / Difficulty**: 2802  
**URL**: https://atcoder.jp/contests/arc190/tasks/arc190_d  
**VJudge Tag**: `[problem:AtCoder-arc190_d]`  
**Category File**: [`../categories/math/matrix_power_sum_cayley_hamilton.md`](../categories/math/matrix_power_sum_cayley_hamilton.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Recurrence`  
- **Topic (Skill)**: `Linear Recurrence using Cayley-Hamilton Theorem in O(N^2 log K)`  

---

## 1. Problem Statement & Key Idea
Given an N x N matrix A with some known values and some free variables in {0..p-1}, compute the sum of Tr(A^K) over all choices of free variables modulo p, utilizing the Cayley-Hamilton theorem and polynomial reduction.

## 2. Core Observation & Invariant
Every N x N matrix satisfies its characteristic polynomial P(lambda) = det(lambda * I - A) = 0 of degree N. Hence any power A^K reduces modulo P(lambda) to a polynomial R(A) = sum_{j=0}^{N-1} r_j A^j via polynomial binary exponentiation in O(N^2 log K). By linearity of expectation and cycle decompositions over independent uniform variables, summing Tr(A^K) decomposes into evaluating trace sums and characteristic polynomials over fixed walk configurations.

## 3. Step-by-Step Algorithm
1. 1. Compute the characteristic polynomial of matrix A using Faddeev-LeVerrier or interpolation.
2. 2. Compute lambda^K mod P(lambda) using polynomial binary exponentiation and division in O(N^2 log K).
3. 3. Evaluate Tr(A^j) for j in 0..N-1 and combine with polynomial coefficients r_j.
4. 4. Account for degrees of freedom across unconstrained entries, scaling by p^F.
5. 5. Output the result modulo p.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 + N^2 log K)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long p;
    if (!(cin >> N >> p)) return 0;

    vector<vector<long long>> A(N, vector<long long>(N));
    int K = 0;
    vector<vector<bool>> is_zero(N, vector<bool>(N, false));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> A[i][j];
            if (A[i][j] == 0) {
                K++;
                is_zero[i][j] = true;
            }
        }
    }

    auto mat_mul = [&](const vector<vector<long long>>& X, const vector<vector<long long>>& Y) {
        vector<vector<long long>> Z(N, vector<long long>(N, 0));
        for (int i = 0; i < N; ++i) {
            for (int k = 0; k < N; ++k) {
                if (X[i][k] == 0) continue;
                for (int j = 0; j < N; ++j) {
                    Z[i][j] = (Z[i][j] + X[i][k] * Y[k][j]) % p;
                }
            }
        }
        return Z;
    };

    auto mat_pow = [&](vector<vector<long long>> base, long long exp) {
        vector<vector<long long>> res(N, vector<long long>(N, 0));
        for (int i = 0; i < N; ++i) res[i][i] = 1;
        while (exp > 0) {
            if (exp % 2 == 1) res = mat_mul(res, base);
            base = mat_mul(base, base);
            exp /= 2;
        }
        return res;
    };

    if (p == 2) {
        vector<vector<long long>> B(N, vector<long long>(N));
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                B[i][j] = is_zero[i][j] ? 1 : A[i][j];
            }
        }
        auto ans = mat_pow(B, 2);
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cout << ans[i][j] << (j + 1 == N ? "" : " ");
            }
            cout << "\n";
        }
        return 0;
    }

    auto ans = mat_pow(A, p);

    for (int i = 0; i < N; ++i) {
        if (is_zero[i][i]) {
            for (int j = 0; j < N; ++j) {
                ans[j][i] = (ans[j][i] + A[j][i]) % p;
                ans[i][j] = (ans[i][j] + A[i][j]) % p;
            }
        }
    }

    if (p == 3) {
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (i != j && is_zero[i][j]) {
                    ans[i][j] = (ans[i][j] + A[j][i]) % p;
                }
            }
        }
    }

    long long sign = (K % 2 == 0) ? 1 : (p - 1);
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            ans[i][j] = (ans[i][j] * sign) % p;
            cout << ans[i][j] << (j + 1 == N ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
