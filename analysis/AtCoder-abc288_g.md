# Problem Analysis: AtCoder-abc288_g — G. 3^N Minesweeper

**Problem ID**: `AtCoder-abc288_g`  
**Contest**: `abc288`  
**Rating / Difficulty**: 2606  
**URL**: https://atcoder.jp/contests/abc288/tasks/abc288_g  
**VJudge Tag**: `[problem:AtCoder-abc288_g]`  
**Category File**: [`../categories/math/minesweeper_ternary_fwht.md`](../categories/math/minesweeper_ternary_fwht.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Fast Walsh Hadamard Transform (FWHT) and its Variations`  

---

## 1. Problem Statement & Key Idea
In a ternary hypercube of size 3^N, A_x is the sum of bombs at positions y differing by at most 1 in each ternary coordinate. Recover the bomb configuration B from A.

## 2. Core Observation & Invariant
The adjacency matrix along each 1D coordinate is M = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]. Its exact inverse is M^{-1} = [[0, 1, -1], [-1, 1, -1], [-1, 1, 0]]. The full N-dimensional operator is the Kronecker product of N copies of M.

## 3. Step-by-Step Algorithm
1. Apply the 1D inverse transform (x, y, z) -> (y - z, x - y + z, y - x) independently across all N ternary dimensions using Fast Walsh-Hadamard Transform (FWHT / SOS DP) structure in O(N * 3^N) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 3^N)`
- **Space Complexity**: `O(3^N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    int total = 1;
    for (int i = 0; i < N; ++i) total *= 3;

    vector<long long> A(total);
    for (int i = 0; i < total; ++i) {
        cin >> A[i];
    }

    int pw = 1;
    for (int dim = 0; dim < N; ++dim) {
        int step = pw * 3;
        for (int i = 0; i < total; i += step) {
            for (int j = 0; j < pw; ++j) {
                long long x = A[i + j];
                long long y = A[i + pw + j];
                long long z = A[i + 2 * pw + j];

                A[i + j] = y - z;
                A[i + pw + j] = x - y + z;
                A[i + 2 * pw + j] = y - x;
            }
        }
        pw *= 3;
    }

    for (int i = 0; i < total; ++i) {
        cout << A[i] << (i + 1 == total ? "" : " ");
    }
    cout << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
