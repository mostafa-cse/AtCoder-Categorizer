# Problem Analysis: AtCoder-arc173_e — E - Rearrange and Adjacent XOR

**Problem ID**: `AtCoder-arc173_e`  
**Contest**: `arc173`  
**Rating / Difficulty**: 2869  
**URL**: https://atcoder.jp/contests/arc173/tasks/arc173_e  
**VJudge Tag**: `[problem:AtCoder-arc173_e]`  
**Category File**: [`../categories/math/adjacent_xor_binomial_parity_linear_basis.md`](../categories/math/adjacent_xor_binomial_parity_linear_basis.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Vector Space and XOR Basis`  

---

## 1. Problem Statement & Key Idea
Given array A of N integers (N <= 100, A_i < 2^60), repeatedly rearrange A and replace with adjacent XORs until length 1. Find the maximum possible value of the final element.

## 2. Core Observation & Invariant
After 1 step, all popcounts become even. For N = 2 or N not equiv 2 mod 4, ANY non-empty even subset of A can be achieved as the final element, which is the vector space spanned by {A_1 ^ A_i}_{i=2}^N. When N > 2 and N equiv 2 mod 4, all even subsets EXCEPT the full set of all N elements are achievable. In that case, we can omit each element A_j one by one and take the maximum over the basis of the remaining N-1 elements.

## 3. Step-by-Step Algorithm
1. 1. If N = 2 or N not equiv 2 mod 4, build an XOR linear basis from {A_1 ^ A_i}_{i=2}^N and greedily maximize the value.
2. 2. If N > 2 and N equiv 2 mod 4, iterate over all j in [0, N-1] (the element omitted), build an XOR linear basis from the remaining N-1 elements, and greedily maximize.
3. 3. Output the overall maximum value.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * 60)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

unsigned long long max_basis(const vector<unsigned long long>& vecs) {
    unsigned long long basis[64] = {0};
    for (unsigned long long v : vecs) {
        for (int b = 62; b >= 0; --b) {
            if ((v >> b) & 1ULL) {
                if (!basis[b]) {
                    basis[b] = v;
                    break;
                }
                v ^= basis[b];
            }
        }
    }
    unsigned long long ans = 0;
    for (int b = 62; b >= 0; --b) {
        if ((ans ^ basis[b]) > ans) {
            ans ^= basis[b];
        }
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<unsigned long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    if (N == 2 || N % 4 != 2) {
        vector<unsigned long long> vecs;
        for (int i = 1; i < N; ++i) {
            vecs.push_back(A[0] ^ A[i]);
        }
        cout << max_basis(vecs) << "\n";
    } else {
        unsigned long long best = 0;
        for (int j = 0; j < N; ++j) {
            vector<unsigned long long> A_sub;
            for (int i = 0; i < N; ++i) {
                if (i != j) A_sub.push_back(A[i]);
            }
            vector<unsigned long long> vecs;
            for (size_t i = 1; i < A_sub.size(); ++i) {
                vecs.push_back(A_sub[0] ^ A_sub[i]);
            }
            best = max(best, max_basis(vecs));
        }
        cout << best << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
