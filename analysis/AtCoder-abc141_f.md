# Problem Analysis: AtCoder-abc141_f — F. Xor Sum 3

**Problem ID**: `AtCoder-abc141_f`  
**Contest**: `abc141`  
**Rating / Difficulty**: 2342  
**URL**: https://atcoder.jp/contests/abc141/tasks/abc141_f  
**VJudge Tag**: `[problem:AtCoder-abc141_f]`  
**Category File**: [`../categories/math/xor_basis_two_partition_maximization.md`](../categories/math/xor_basis_two_partition_maximization.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `Vector Space and XOR Basis`  

---

## 1. Problem Statement & Key Idea
Maximize the sum of two disjoint subset XOR sums. Bits with odd total counts contribute $2^b$ regardless; bits with even total counts can both be made 1 by finding the maximum subset XOR sum on masked elements via Gaussian elimination in $O(N \log (\max A))$.

## 2. Core Observation & Invariant
Let $S = \bigoplus A_i$ be the total XOR sum. In any partition $(X, Y)$, $X \oplus Y = S$. For bits where $S$ has 1, exactly one of $X$ and $Y$ has 1, contributing $2^b$ to $X + Y$ regardless of partition. For bits where $S$ has 0, $X$ and $Y$ have the same bit value; if that bit is 1 in $X$, both contribute $2^b$, adding $2^{b+1}$ to $X + Y$. Thus, maximizing $X + Y$ is equivalent to maximizing the subset XOR sum on masked elements $A_i \ \& \ (\sim S)$.

## 3. Step-by-Step Algorithm
1. Compute total XOR sum $S = \bigoplus A_i$.
2. Mask every element: $A'_i = A_i \ \& \ (\sim S)$.
3. Construct an XOR Basis (Gaussian elimination over $\text{GF}(2)$) on $\{A'_i\}$ from MSB (bit 59 down to 0).
4. Find the maximum possible XOR sum $X_{masked}$ obtainable from the basis.
5. The answer is $2 \cdot X_{masked} + S$, solved in $O(N \log(\max A))$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log (\max A))`
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
    unsigned long long total_xor = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        total_xor ^= a[i];
    }

    unsigned long long mask = ~total_xor;
    vector<unsigned long long> basis(62, 0);

    for (int i = 0; i < n; ++i) {
        unsigned long long val = a[i] & mask;
        for (int b = 60; b >= 0; --b) {
            if ((val >> b) & 1) {
                if (!basis[b]) {
                    basis[b] = val;
                    break;
                }
                val ^= basis[b];
            }
        }
    }

    unsigned long long max_val = 0;
    for (int b = 60; b >= 0; --b) {
        if (!((max_val >> b) & 1) && basis[b]) {
            max_val ^= basis[b];
        }
    }

    unsigned long long ans = total_xor + 2 * max_val;
    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
