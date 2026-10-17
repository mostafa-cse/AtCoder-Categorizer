# Problem Analysis: AtCoder-arc092_b — Two Sequences

**Problem ID**: `AtCoder-arc092_b`  
**Contest**: `arc092`  
**Rating / Difficulty**: 2207  
**URL**: https://atcoder.jp/contests/arc092/tasks/arc092_b  
**VJudge Tag**: `[problem:AtCoder-arc092_b]`  
**Category File**: [`../categories/basics/two_sequences_bit_by_bit_modular_binary_search.md`](../categories/basics/two_sequences_bit_by_bit_modular_binary_search.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Leveraging Monotonicity`  
- **Topic (Skill)**: `Binary Search`  

---

## 1. Problem Statement & Key Idea
Bit-by-bit contribution method with modular reduction mod 2^(k+1) and range counting via binary search.

## 2. Core Observation & Invariant
Bit k of a_i + b_j is completely determined by (a_i mod 2^(k+1)) + (b_j mod 2^(k+1)). Setting T = 2^k, bit k is 1 iff the sum lies in [T, 2T - 1] or [3T, 4T - 2].

## 3. Step-by-Step Algorithm
1. 1. For each bit k from 0 to 28:
2.    - Reduce all b_j modulo 2^(k+1) and sort array y.
3.    - For each a_i, x = a_i mod 2^(k+1). Use binary search (lower_bound/upper_bound) on y to count j such that y_j in [T - x, 2T - 1 - x] and [3T - x, 4T - 2 - x].
4.    - If the total count across all i is odd, set bit k in answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(B * N log N) where B = 29`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<int> a(N), b(N);
    for (int i = 0; i < N; ++i) cin >> a[i];
    for (int i = 0; i < N; ++i) cin >> b[i];

    int ans = 0;

    for (int k = 0; k < 29; ++k) {
        int T = 1 << k;
        int mod = 1 << (k + 1);

        vector<int> y(N);
        for (int i = 0; i < N; ++i) {
            y[i] = b[i] % mod;
        }
        sort(y.begin(), y.end());

        ll count = 0;

        for (int i = 0; i < N; ++i) {
            int x = a[i] % mod;

            // Range 1: [T - x, 2T - 1 - x]
            int l1 = T - x;
            int r1 = 2 * T - 1 - x;
            auto it1_l = lower_bound(y.begin(), y.end(), l1);
            auto it1_r = upper_bound(y.begin(), y.end(), r1);
            count += (it1_r - it1_l);

            // Range 2: [3T - x, 4T - 2 - x]
            int l2 = 3 * T - x;
            int r2 = 4 * T - 2 - x;
            auto it2_l = lower_bound(y.begin(), y.end(), l2);
            auto it2_r = upper_bound(y.begin(), y.end(), r2);
            count += (it2_r - it2_l);
        }

        if (count % 2 != 0) {
            ans |= (1 << k);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
