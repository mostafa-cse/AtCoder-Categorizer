# Problem Analysis: AtCoder-abc258_h — Odd Steps

**Problem ID**: `AtCoder-abc258_h`  
**Contest**: `abc258`  
**Rating / Difficulty**: 2708  
**URL**: https://atcoder.jp/contests/abc258/tasks/abc258_h  
**VJudge Tag**: `[problem:AtCoder-abc258_h]`  
**Category File**: [`../categories/math/odd_steps_forbidden_points_matrix_exp.md`](../categories/math/odd_steps_forbidden_points_matrix_exp.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Matrices`  
- **Topic (Skill)**: `Matrix Exponentiation`  

---

## 1. Problem Statement & Key Idea
Sequences of odd steps summing to S without hitting forbidden prefix sums A_1..A_N. dp[k] = sum_{odd x} dp[k-x] = S_even(k-1) if k odd, and S_odd(k-1) if k even. The state vector [S_odd(k), S_even(k)] updates via 2x2 matrices M_odd and M_even for normal points, and identity matrix I for forbidden points. Consecutive normal intervals are accelerated via 2x2 matrix exponentiation.

## 2. Core Observation & Invariant
Two consecutive normal steps advance the state vector by T = M_even * M_odd = [[1, 1], [1, 2]], identical to the Fibonacci transformation matrix. For any uninhibited interval of length L, the transition is computed in O(log L) via matrix power.

## 3. Step-by-Step Algorithm
1. 1. Initialize state vector [S_odd(0), S_even(0)] = [0, 1] at k = 0.
2. 2. Filter forbidden points A_i <= S - 1.
3. 3. For each segment of normal points between consecutive forbidden points, apply 2x2 matrix power T^{pairs} with boundary matrix adjustments.
4. 4. At forbidden points A_i, the state vector is unchanged (dp[A_i] = 0).
5. 5. After reaching S - 1, output S_even(S - 1) if S is odd, or S_odd(S - 1) if S is even.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log S)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

static const long long MOD = 998244353;

struct Mat2 {
    long long a[2][2];
    Mat2() {
        a[0][0] = a[0][1] = a[1][0] = a[1][1] = 0;
    }
};

Mat2 mat_mul(const Mat2& A, const Mat2& B) {
    Mat2 C;
    for (int i = 0; i < 2; ++i) {
        for (int k = 0; k < 2; ++k) {
            for (int j = 0; j < 2; ++j) {
                C.a[i][j] = (C.a[i][j] + A.a[i][k] * B.a[k][j]) % MOD;
            }
        }
    }
    return C;
}

Mat2 mat_pow(Mat2 base, long long p) {
    Mat2 res;
    res.a[0][0] = res.a[1][1] = 1;
    while (p > 0) {
        if (p % 2 == 1) res = mat_mul(res, base);
        base = mat_mul(base, base);
        p /= 2;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long S;
    if (!(cin >> n >> S)) return 0;

    vector<long long> A(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    Mat2 M_odd, M_even;
    M_odd.a[0][0] = 1; M_odd.a[0][1] = 1;
    M_odd.a[1][0] = 0; M_odd.a[1][1] = 1;

    M_even.a[0][0] = 1; M_even.a[0][1] = 0;
    M_even.a[1][0] = 1; M_even.a[1][1] = 1;

    Mat2 T_odd_start = mat_mul(M_even, M_odd);
    Mat2 T_even_start = mat_mul(M_odd, M_even);

    auto apply_range = [&](pair<long long, long long>& cur_v, long long start_k, long long end_k) {
        if (start_k > end_k) return;
        long long length = end_k - start_k + 1;
        long long pairs = length / 2;
        Mat2 M_trans;
        if (start_k % 2 == 1) {
            M_trans = mat_pow(T_odd_start, pairs);
            if (length % 2 == 1) {
                M_trans = mat_mul(M_odd, M_trans);
            }
        } else {
            M_trans = mat_pow(T_even_start, pairs);
            if (length % 2 == 1) {
                M_trans = mat_mul(M_even, M_trans);
            }
        }

        long long new_v0 = (M_trans.a[0][0] * cur_v.first + M_trans.a[0][1] * cur_v.second) % MOD;
        long long new_v1 = (M_trans.a[1][0] * cur_v.first + M_trans.a[1][1] * cur_v.second) % MOD;
        cur_v = {new_v0, new_v1};
    };

    pair<long long, long long> cur_v = {0, 1}; // k = 0: S_odd = 0, S_even = 1
    long long cur_k = 1;

    for (int i = 0; i < n; ++i) {
        long long a = A[i];
        if (a > S - 1) break;
        if (a >= cur_k) {
            apply_range(cur_v, cur_k, a - 1);
            cur_k = a + 1; // at k = a: forbidden, no change
        }
    }

    if (cur_k <= S - 1) {
        apply_range(cur_v, cur_k, S - 1);
    }

    long long ans = 0;
    if (S % 2 == 1) {
        ans = cur_v.second; // S_even(S - 1)
    } else {
        ans = cur_v.first;  // S_odd(S - 1)
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
