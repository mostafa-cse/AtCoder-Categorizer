# Problem Analysis: AtCoder-abc147_d — Xor Sum 4

**Problem ID**: `AtCoder-abc147_d`  
**Contest**: `abc147`  
**Rating / Difficulty**: 1205  
**URL**: https://atcoder.jp/contests/abc147/tasks/abc147_d  
**VJudge Tag**: `[problem:AtCoder-abc147_d]`  
**Category File**: [`../categories/math/bitwise_independent_contribution.md`](../categories/math/bitwise_independent_contribution.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Bitwise Arithmetic`  
- **Topic (Skill)**: `Bitwise Independent Contribution Summation modulo 10^9+7`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers (A_i < 2^60). Compute sum_{i=1}^{N-1} sum_{j=i+1}^N (A_i XOR A_j) modulo 10^9 + 7.

**Key Idea**: Bitwise XOR operates independently on each bit position b from 0 to 59.

## 2. Core Observation & Invariant
For each bit b: count how many elements have bit b equal to 1 (let this be c_1) and how many have bit b equal to 0 (c_0 = N - c_1). A pair (A_i, A_j) has bit b set in (A_i XOR A_j) if and only if one element has bit b = 1 and the other has bit b = 0. Thus, bit b is set in exactly c_1 * c_0 pairs! Contribution to the total sum is 2^b * c_1 * c_0.

## 3. Step-by-Step Algorithm
1. For bit b from 0 to 59: count c1 = count of elements with (A[i] >> b) & 1.
2. Pairs with bit b set: pairs = c1 * (N - c1).
3. Add (pairs % MOD) * (2^b % MOD) to total sum.
4. Output total sum modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(60 * N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long total_ans = 0;

    for (int b = 0; b < 60; ++b) {
        long long c1 = 0;
        for (int i = 0; i < n; ++i) {
            if ((a[i] >> b) & 1) {
                c1++;
            }
        }
        long long c0 = n - c1;
        long long pairs = (c1 * c0) % MOD;
        long long weight = (1ULL << b) % MOD;
        long long term = (pairs * weight) % MOD;
        total_ans = (total_ans + term) % MOD;
    }

    cout << total_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitwise linearity and contribution counting across all pairs.
- **Reusable Pattern**: `Sum of pairwise XOR: sum_{b=0}^{59} 2^b * count_1(b) * count_0(b).`
