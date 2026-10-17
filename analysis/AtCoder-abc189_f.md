# Problem Analysis: AtCoder-abc189_f — Sugoroku2

**Problem ID**: `AtCoder-abc189_f`  
**Contest**: `abc189`  
**Rating / Difficulty**: 2154  
**URL**: https://atcoder.jp/contests/abc189/tasks/abc189_f  
**VJudge Tag**: `[problem:AtCoder-abc189_f]`  
**Category File**: [`../categories/math/expected_value_dp_reset_squares_affine.md`](../categories/math/expected_value_dp_reset_squares_affine.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Probabilities and Expected Values`  
- **Topic (Skill)**: `Probabilities and Expected Values`  

---

## 1. Problem Statement & Key Idea
Compute the expected number of turns to reach square >= N on a 1D board with dice rolls 1..M, where landing on designated trap squares resets Takahashi back to square 0. Express each state expected value as an affine function of E[0] and maintain sliding window sums.

## 2. Core Observation & Invariant
If M consecutive squares are reset squares, the game cannot terminate (output -1). For each state i, the expected steps to finish satisfies E[i] = 1 + (1/M) sum_{d=1}^M E[i+d]. Landing on a reset square gives E[i] = E[0]. Since the recurrence is linear, every state can be expressed as E[i] = a_i * E[0] + b_i. Sliding window sums compute coefficients in O(1) backwards, and E[0] is solved directly from E[0] = a_0 * E[0] + b_0.

## 3. Step-by-Step Algorithm
1. Check if any sequence of M consecutive squares are reset squares; if so, output -1.
2. Represent each state as E[i] = A[i] * E[0] + B[i]. For i >= N, A[i] = 0, B[i] = 0. For reset squares, A[i] = 1, B[i] = 0.
3. Maintain sliding window sums of A and B of length M from i = N - 1 down to 0.
4. For non-reset squares, set A[i] = sumA / M and B[i] = sumB / M + 1.
5. Solve for E[0] = B[0] / (1 - A[0]). If |1 - A[0]| < 1e-9, output -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<bool> send_back(n + 1, false);
    for (int i = 0; i < k; ++i) {
        int a;
        cin >> a;
        send_back[a] = true;
    }

    int consecutive = 0;
    for (int i = 0; i <= n; ++i) {
        if (send_back[i]) {
            consecutive++;
            if (consecutive >= m) {
                cout << -1 << "\n";
                return 0;
            }
        } else {
            consecutive = 0;
        }
    }

    vector<double> A(n + m + 1, 0.0);
    vector<double> B(n + m + 1, 0.0);

    double sumA = 0.0;
    double sumB = 0.0;

    for (int i = n - 1; i >= 0; --i) {
        if (send_back[i]) {
            A[i] = 1.0;
            B[i] = 0.0;
        } else {
            A[i] = sumA / m;
            B[i] = sumB / m + 1.0;
        }

        sumA += A[i];
        sumB += B[i];

        if (i + m <= n + m) {
            sumA -= A[i + m];
            sumB -= B[i + m];
        }
    }

    if (abs(1.0 - A[0]) < 1e-9) {
        cout << -1 << "\n";
    } else {
        double ans = B[0] / (1.0 - A[0]);
        cout << fixed << setprecision(10) << ans << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
