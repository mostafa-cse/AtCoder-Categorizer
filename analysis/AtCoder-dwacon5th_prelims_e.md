# Problem Analysis: AtCoder-dwacon5th_prelims_e — E - Cyclic GCDs

**Problem ID**: `AtCoder-dwacon5th_prelims_e`  
**Contest**: `dwacon5th-prelims`  
**Rating / Difficulty**: 2978  
**URL**: https://atcoder.jp/contests/dwacon5th-prelims/tasks/dwacon5th_prelims_e  
**VJudge Tag**: `[problem:AtCoder-dwacon5th_prelims_e]`  
**Category File**: [`../categories/miscellaneous/permutation_cycle_generating_function_gauss_lemma_content.md`](../categories/miscellaneous/permutation_cycle_generating_function_gauss_lemma_content.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Permutations`  
- **Topic (Skill)**: `Permutations and Permutation Cycles`  

---

## 1. Problem Statement & Key Idea
Find the greatest common divisor of b_1, ..., b_N modulo 998244353, where b_k is the sum of cycle products of the minimum chicken size over all permutations with exactly k disjoint cycles.

## 2. Core Observation & Invariant
Sorting a so that a_1 <= ... <= a_N, inserting element i+1 into an existing cycle has i choices and does not change the cycle minimum, while forming a new cycle has 1 choice and multiplies beauty by a_{i+1}. The generating function for the cycle partition polynomial is P_N(t) = \prod_{i=0}^{N-1} (a_{i+1} t + i). By Gauss's Lemma on polynomial content, the GCD of all coefficients of a product of integer polynomials equals the product of their contents: c(P_N(t)) = \prod_{i=0}^{N-1} \gcd(a_{i+1}, i).

## 3. Step-by-Step Algorithm
1. 1. Sort chicken sizes a in non-decreasing order: a_1 <= a_2 <= ... <= a_N.
2. 2. Initialize ans = 1.
3. 3. For each i from 0 to N-1, compute g = gcd(a_{i+1}, i) (where gcd(a_1, 0) = a_1).
4. 4. Update ans = (ans * (g % 998244353)) % 998244353.
5. 5. Output ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log (\max A))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

long long gcd_ll(long long a, long long b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<long long> a(N);
    for (int i = 0; i < N; ++i) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    long long MOD = 998244353;
    long long ans = 1;

    for (int i = 0; i < N; ++i) {
        long long g = gcd_ll(a[i], i);
        ans = (ans * (g % MOD)) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
