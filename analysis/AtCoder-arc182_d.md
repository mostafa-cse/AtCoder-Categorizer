# Problem Analysis: AtCoder-arc182_d — D - Increment Decrement Again

**Problem ID**: `AtCoder-arc182_d`  
**Contest**: `arc182`  
**Rating / Difficulty**: 2992  
**URL**: https://atcoder.jp/contests/arc182/tasks/arc182_d  
**VJudge Tag**: `[problem:AtCoder-arc182_d]`  
**Category File**: [`../categories/dynamic_programming/covering_space_lift_median_slope_trick.md`](../categories/dynamic_programming/covering_space_lift_median_slope_trick.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `Slope Trick`  

---

## 1. Problem Statement & Key Idea
Transform array A into B modulo M using cyclic +/-1 operations without adjacent elements ever being equal. Minimize total operations.

## 2. Core Observation & Invariant
Because adjacent elements never cross, their relative winding number on the circle is invariant. Lift B to the universal covering space (integers Z) by setting C_0 = B_0 and uniquely determining C_i such that |C_i - C_{i-1}| < M and sgn(C_i - C_{i-1}) = sgn(A_i - A_{i-1}). Any global rotation by k * M preserves winding. The total cost is \sum |(A_i + k * M) - C_i|, which is a convex piecewise linear function minimized at the median of C_i - A_i via Slope Trick.

## 3. Step-by-Step Algorithm
1. 1. Handle M = 2 corner case: return 0 if A == B, else -1.
2. 2. Lift B to universal covering array C: set C_0 = B_0. For i = 1 to N-1, find candidate j * M + B_i matching adjacent sign condition with difference < M.
3. 3. Compute difference array diff[i] = C_i - A_i and find median med = diff[N / 2].
4. 4. Test candidate multiples of M surrounding med: k in [med/M - 3, med/M + 3].
5. 5. Output the minimum total absolute deviation.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int sgn(long long x, long long y) {
    if (x < y) return -1;
    if (x == y) return 0;
    return 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long M;
    if (!(cin >> N >> M)) return 0;

    vector<long long> A(N), B(N);
    for (int i = 0; i < N; ++i) cin >> A[i];
    for (int i = 0; i < N; ++i) cin >> B[i];

    if (M == 2) {
        if (A == B) {
            cout << 0 << "\n";
        } else {
            cout << -1 << "\n";
        }
        return 0;
    }

    vector<long long> C(N);
    C[0] = B[0];
    for (int i = 1; i < N; ++i) {
        long long base_j = C[i - 1] / M;
        bool found = false;
        for (long long j = base_j - 4; j <= base_j + 4; ++j) {
            long long cand = j * M + B[i];
            if (sgn(A[i - 1], A[i]) == sgn(C[i - 1], cand) && abs(C[i - 1] - cand) < M) {
                C[i] = cand;
                found = true;
                break;
            }
        }
        if (!found) {
            cout << -1 << "\n";
            return 0;
        }
    }

    vector<long long> diff(N);
    for (int i = 0; i < N; ++i) {
        diff[i] = C[i] - A[i];
    }
    sort(diff.begin(), diff.end());
    long long med = diff[N / 2];

    long long base_k = med / M;
    long long ans = -1;
    for (long long k = base_k - 3; k <= base_k + 3; ++k) {
        long long cur = 0;
        for (int i = 0; i < N; ++i) {
            cur += abs(A[i] + k * M - C[i]);
        }
        if (ans == -1 || cur < ans) {
            ans = cur;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
