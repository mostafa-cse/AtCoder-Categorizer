# Problem Analysis: AtCoder-arc138_d — Differ by K bits

**Problem ID**: `AtCoder-arc138_d`  
**Contest**: `arc138`  
**Rating / Difficulty**: 2080  
**URL**: https://atcoder.jp/contests/arc138/tasks/arc138_d  
**VJudge Tag**: `[problem:AtCoder-arc138_d]`  
**Category File**: [`../categories/math/linear_basis_hypercube_gray_code.md`](../categories/math/linear_basis_hypercube_gray_code.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Vector Space and XOR Basis`  

---

## 1. Problem Statement & Key Idea
Given integers N and K, construct a permutation P of 0, 1, ..., 2^N - 1 such that P_0 = 0 and each adjacent pair of elements (including P_{2^N - 1} and P_0) differs by exactly K bits. If no such permutation exists, report it.

**Key Insight**: A cycle of length 2^N where each step flips K bits is a Hamiltonian cycle on a generalized hypercube graph. The parity of the number of 1s in the binary representation changes by K mod 2 at each step. Since 2^N is even, visiting all vertices and returning to 0 requires an even number of steps, but if K is even, the parity of the number of set bits never changes, making it bipartite-partitioned and impossible to visit odd-weight states! Thus K must be odd and 1 <= K < N. When K is odd, we can find N linearly independent vectors v_1, ..., v_N in (F_2)^N each having popcount K. Using the standard reflected binary Gray code G_i, we map each element to sum_{j=0}^{N-1} ((G_i >> j) & 1) * v_j.

## 2. Core Observation & Invariant
Even K creates a parity obstruction on popcount. For odd K, the problem reduces via linear isomorphism to standard Gray code over an F_2 basis of K-weight vectors.

## 3. Step-by-Step Algorithm
1. If K is even or K > N: output No (if K == N, only N=1 is valid).
2. Find N linearly independent vectors in {0, 1}^N each with popcount K using Gaussian elimination over F_2.
3. Generate standard reflected binary Gray code g_i = i ^ (i >> 1) for 0 <= i < 2^N.
4. For each i, P[i] = sum of basis vectors corresponding to set bits of g_i.
5. Output Yes and the sequence P.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: F_2 linear basis construction and linear isomorphism of hypercube Gray codes.
- **Reusable Pattern**: Constructing Hamiltonian cycles with constrained XOR differences by finding an F_2 basis of valid deltas and applying Gray code.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>

using namespace std;

int count_bits(int x) {
    return __builtin_popcount(x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    if (k % 2 == 0 || k > n) {
        cout << "No\n";
        return 0;
    }

    if (k == n) {
        if (n == 1) {
            cout << "Yes\n0 1\n";
        } else {
            cout << "No\n";
        }
        return 0;
    }

    vector<int> basis;
    vector<int> original;

    for (int mask = 1; mask < (1 << n); ++mask) {
        if (count_bits(mask) == k) {
            int cur = mask;
            for (int b : basis) {
                cur = min(cur, cur ^ b);
            }
            if (cur > 0) {
                basis.push_back(cur);
                original.push_back(mask);
                // Maintain reduced basis
                for (int i = (int)basis.size() - 1; i > 0; --i) {
                    if (basis[i] > basis[i - 1]) {
                        swap(basis[i], basis[i - 1]);
                    }
                }
                if ((int)original.size() == n) break;
            }
        }
    }

    if ((int)original.size() < n) {
        cout << "No\n";
        return 0;
    }

    cout << "Yes\n";
    int total = 1 << n;
    for (int i = 0; i < total; ++i) {
        int gray = i ^ (i >> 1);
        int val = 0;
        for (int j = 0; j < n; ++j) {
            if ((gray >> j) & 1) {
                val ^= original[j];
            }
        }
        cout << val << (i + 1 == total ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```
