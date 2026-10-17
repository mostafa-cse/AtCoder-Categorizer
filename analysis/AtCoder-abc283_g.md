# Problem Analysis: AtCoder-abc283_g — G. Partial Xor Enumeration

**Problem ID**: `AtCoder-abc283_g`  
**Contest**: `abc283`  
**Rating / Difficulty**: 2173  
**URL**: https://atcoder.jp/contests/abc283/tasks/abc283_g  
**VJudge Tag**: `[problem:AtCoder-abc283_g]`  
**Category File**: [`../categories/math/xor_basis_reduced_row_echelon_kth_query.md`](../categories/math/xor_basis_reduced_row_echelon_kth_query.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `[Technique] XOR Basis ft Reduced Row Echelon Form`  

---

## 1. Problem Statement & Key Idea
Find the k-th smallest subset XOR value for each k in [L, R]. Construct a linear basis of the given integers over F_2 and diagonalize it into Reduced Row Echelon Form (RREF). The sorted distinct subset XOR values correspond 1-to-1 with the binary representations of integers 0 <= idx < 2^d expanded over the basis.

## 2. Core Observation & Invariant
Once the basis B_0 < B_1 < ... < B_{d-1} is in canonical RREF (each basis vector has a unique pivot bit that is 0 in all other basis vectors), lexicographical order of subset XORs matches the standard integer binary order. Thus, the k-th smallest subset XOR is obtained directly by taking linear combinations matching the binary representation of k - 1.

## 3. Step-by-Step Algorithm
1. Insert each integer A_i into a linear basis using standard Gaussian elimination.
2. Diagonalize the basis into Reduced Row Echelon Form (RREF) so that the leading pivot of each basis vector is cleared from all other basis vectors.
3. Sort the basis vectors in ascending order of their pivot bits.
4. For each k in [L, R], evaluate the XOR sum of basis[b] for each bit b set in (k - 1).

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 60 + (R - L + 1) * 60)`
- **Space Complexity**: `O(N + 60)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    long long L, R;
    if (!(cin >> N >> L >> R)) return 0;

    vector<unsigned long long> A(N);
    vector<unsigned long long> basis;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        unsigned long long x = A[i];
        for (unsigned long long b : basis) {
            x = min(x, x ^ b);
        }
        if (x > 0) {
            basis.push_back(x);
            sort(basis.rbegin(), basis.rend());
        }
    }

    int d = (int)basis.size();
    for (int i = d - 1; i >= 0; --i) {
        for (int j = i - 1; j >= 0; --j) {
            basis[j] = min(basis[j], basis[j] ^ basis[i]);
        }
    }

    reverse(basis.begin(), basis.end());

    for (long long k = L; k <= R; ++k) {
        long long idx = k - 1;
        unsigned long long val = 0;
        for (int b = 0; b < d; ++b) {
            if ((idx >> b) & 1) {
                val ^= basis[b];
            }
        }
        cout << val << (k == R ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
