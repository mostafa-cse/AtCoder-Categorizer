# Problem Analysis: AtCoder-arc020_3 — A mod B Problem

**Problem ID**: `AtCoder-arc020_3`  
**Contest**: `arc020`  
**Rating / Difficulty**: 2141  
**URL**: https://atcoder.jp/contests/arc020/tasks/arc020_3  
**VJudge Tag**: `[problem:AtCoder-arc020_3]`  
**Category File**: [`../categories/math/matrix_exponentiation_concatenated_digits.md`](../categories/math/matrix_exponentiation_concatenated_digits.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
Given N pairs (A_i, L_i), concatenate number A_i repeated L_i times for all i = 1..N. Find the value of the resulting huge integer modulo B.

**Key Insight**: Repeating an integer A with d digits L times transforms a current value x via x' = x * 10^{dL} + A * (10^{dL} - 1) / (10^d - 1). Because B may not be coprime to 10^d - 1, modular division is invalid. Instead, we express the affine state transition [x, 1]^T -> [x * 10^d + A, 1]^T as multiplication by a 2x2 matrix M = [[10^d, A], [0, 1]]. Repeating L times is computing M^L via standard 2x2 matrix exponentiation modulo B.

## 2. Core Observation & Invariant
Repeated decimal concatenation under arbitrary composite modulus B corresponds to 2x2 affine matrix exponentiation.

## 3. Step-by-Step Algorithm
1. Initialize current value x = 0.
2. For each block (A_i, L_i):
3.   Let d be the number of digits of A_i, and p = 10^d mod B.
4.   Construct matrix M = [[p, A_i mod B], [0, 1]].
5.   Compute M_pow = M^{L_i} mod B using binary exponentiation.
6.   Update x = (M_pow[0][0] * x + M_pow[0][1]) mod B.
7. Output x.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * log L)`
- **Space Complexity**: `O(1)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: 2x2 affine matrix exponentiation for concatenated repeated base-10 blocks under arbitrary composite modulus.
- **Reusable Pattern**: Evaluating repeated string-number repetitions modulo arbitrary non-prime B via affine transfer matrices.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>

using namespace std;

long long B;

struct Matrix {
    long long mat[2][2];
    Matrix() {
        mat[0][0] = mat[0][1] = mat[1][0] = mat[1][1] = 0;
    }
};

Matrix multiply(const Matrix& a, const Matrix& b) {
    Matrix c;
    for (int i = 0; i < 2; ++i) {
        for (int k = 0; k < 2; ++k) {
            for (int j = 0; j < 2; ++j) {
                c.mat[i][j] = (c.mat[i][j] + (__int128)a.mat[i][k] * b.mat[k][j]) % B;
            }
        }
    }
    return c;
}

Matrix power(Matrix a, long long exp) {
    Matrix res;
    res.mat[0][0] = res.mat[1][1] = 1;
    while (exp > 0) {
        if (exp & 1) res = multiply(res, a);
        a = multiply(a, a);
        exp >>= 1;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n), l(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i] >> l[i];
    }
    cin >> B;

    long long cur_x = 0;

    for (int i = 0; i < n; ++i) {
        long long temp = a[i];
        long long p10 = 1;
        while (temp > 0) {
            p10 = (p10 * 10) % B;
            temp /= 10;
        }

        Matrix m;
        m.mat[0][0] = p10;
        m.mat[0][1] = a[i] % B;
        m.mat[1][0] = 0;
        m.mat[1][1] = 1;

        Matrix m_pow = power(m, l[i]);
        cur_x = ((__int128)m_pow.mat[0][0] * cur_x + m_pow.mat[0][1]) % B;
    }

    cout << cur_x << "\n";
    return 0;
}
```
