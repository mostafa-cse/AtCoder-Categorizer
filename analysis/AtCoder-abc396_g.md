# Problem Analysis: AtCoder-abc396_g — G. Flip Row or Col

**Problem ID**: `AtCoder-abc396_g`  
**Contest**: `abc396`  
**Rating / Difficulty**: 2195  
**URL**: https://atcoder.jp/contests/abc396/tasks/abc396_g  
**VJudge Tag**: `[problem:AtCoder-abc396_g]`  
**Category File**: [`../categories/math/fast_walsh_hadamard_transform_xor_convolution.md`](../categories/math/fast_walsh_hadamard_transform_xor_convolution.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Convolution`  
- **Topic (Skill)**: `Fast Walsh Hadamard Transform (FWHT) and its Variations`  

---

## 1. Problem Statement & Key Idea
Given an H x W grid (W <= 18), we can flip any subset of rows and columns. For column flip mask C, row i achieves min(popcount(R_i ^ C), W - popcount(R_i ^ C)). Summing over all rows is an exact XOR convolution of row mask frequencies A and weight array B[mask] = min(popcount(mask), W - popcount(mask)), computed via FWHT in O(W * 2^W) time.

## 2. Core Observation & Invariant
The total score for column mask C is sum_{u ^ v = C} A[u] * B[v]. Fast Walsh-Hadamard Transform transforms both arrays to Hadamard basis, multiplies point-wise, and inverts back in O(W * 2^W) approx 4.7e6 operations.

## 3. Step-by-Step Algorithm
1. Count row mask frequencies in array A of size 2^W.
2. Initialize array B of size 2^W with B[mask] = min(popcount(mask), W - popcount(mask)).
3. Apply forward FWHT to A and B.
4. Multiply point-wise: A[i] *= B[i] for all i in [0, 2^W - 1].
5. Apply inverse FWHT to A.
6. Output min_{C} A[C].

## 4. Complexity Analysis
- **Time Complexity**: `O(H + W * 2^W)`
- **Space Complexity**: `O(2^W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void fwht(vector<long long>& a, bool invert = false) {
    int n = a.size();
    for (int len = 1; 2 * len <= n; len <<= 1) {
        for (int i = 0; i < n; i += 2 * len) {
            for (int j = 0; j < len; ++j) {
                long long u = a[i + j];
                long long v = a[i + len + j];
                a[i + j] = u + v;
                a[i + len + j] = u - v;
            }
        }
    }
    if (invert) {
        for (int i = 0; i < n; ++i) {
            a[i] /= n;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    int size = 1 << W;
    vector<long long> A(size, 0);
    for (int i = 0; i < H; ++i) {
        string s;
        cin >> s;
        int mask = 0;
        for (int j = 0; j < W; ++j) {
            if (s[j] == '1') {
                mask |= (1 << j);
            }
        }
        A[mask]++;
    }

    vector<long long> B(size, 0);
    for (int mask = 0; mask < size; ++mask) {
        int cnt = __builtin_popcount(mask);
        B[mask] = min(cnt, W - cnt);
    }

    fwht(A);
    fwht(B);
    for (int i = 0; i < size; ++i) {
        A[i] *= B[i];
    }
    fwht(A, true);

    long long min_cost = 4e18;
    for (int c = 0; c < size; ++c) {
        min_cost = min(min_cost, A[c]);
    }

    cout << min_cost << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
