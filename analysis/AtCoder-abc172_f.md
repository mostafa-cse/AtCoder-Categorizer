# Problem Analysis: AtCoder-abc172_f — Unfair Nim

**Problem ID**: `AtCoder-abc172_f`  
**Contest**: `abc172`  
**Rating / Difficulty**: 2216  
**URL**: https://atcoder.jp/contests/abc172/tasks/abc172_f  
**VJudge Tag**: `[problem:AtCoder-abc172_f]`  
**Category File**: [`../categories/game_theory/unfair_nim_bitwise_sum_xor_reduction.md`](../categories/game_theory/unfair_nim_bitwise_sum_xor_reduction.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
Transfer minimum d stones (0 <= d < A_1) from pile 1 to pile 2 so that Takahashi wins Nim (overall XOR sum of all N piles becomes 0).

## 2. Core Observation & Invariant
Let u = A_1 - d, v = A_2 + d. We need u ^ v = XOR(A_3..A_N) = X and u + v = A_1 + A_2 = S. Since (u + v) - (u ^ v) = 2(u & v), we obtain u & v = D = (S - X) / 2. This requires S >= X, (S - X) even, and (D & X) == 0. To minimize d = A_1 - u, we greedily set bits of X in u from most significant to least while keeping u <= A_1.

## 3. Step-by-Step Algorithm
1. 1. Compute X = XOR(A_3..A_N) and S = A_1 + A_2.
2. 2. Check feasibility: S >= X, (S - X) % 2 == 0, and ((S - X) / 2 & X) == 0. If not, output -1.
3. 3. Initialize u = D = (S - X) / 2. If u > A_1, output -1.
4. 4. Iterate bit b from 61 down to 0: if bit b is set in X and u + (1 << b) <= A_1, set u += (1 << b).
5. 5. Check u >= 1 (since d < A_1 requires u >= 1). If u == 0, output -1; otherwise output A_1 - u.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + log(max A))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<unsigned long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    unsigned long long x = 0;
    for (int i = 2; i < n; i++) x ^= a[i];

    unsigned long long s = a[0] + a[1];

    if (s < x || ((s - x) & 1)) {
        cout << -1 << "\n";
        return 0;
    }

    unsigned long long d = (s - x) / 2;

    if ((d & x) != 0) {
        cout << -1 << "\n";
        return 0;
    }

    if (d > a[0]) {
        cout << -1 << "\n";
        return 0;
    }

    unsigned long long u = d;
    for (int b = 61; b >= 0; b--) {
        if ((x >> b) & 1ULL) {
            if (u + (1ULL << b) <= a[0]) {
                u += (1ULL << b);
            }
        }
    }

    if (u == 0) {
        cout << -1 << "\n";
        return 0;
    }

    unsigned long long ans = a[0] - u;
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
