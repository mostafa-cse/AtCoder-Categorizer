# Problem Analysis: AtCoder-agc061_c — First Come First Served

**Problem ID**: `AtCoder-agc061_c`  
**Contest**: `agc061`  
**Rating / Difficulty**: 2697  
**URL**: https://atcoder.jp/contests/agc061/tasks/agc061_c  
**VJudge Tag**: `[problem:AtCoder-agc061_c]`  
**Category File**: [`../categories/dynamic_programming_dp/first_come_first_serve_interval_dp.md`](../categories/dynamic_programming_dp/first_come_first_serve_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `More Tricks`  
- **Topic (Skill)**: `Open and Close Interval Trick`  

---

## 1. Problem Statement & Key Idea
Customers choose arrival A_i (C_i = 0) or departure B_i (C_i = 1). Two choices yield the same permutation iff one can flip C_i from 1 to 0 without changing relative order, which occurs iff interval (A_i, B_i) contains no other entries ('a problem at i'). Using Principle of Inclusion-Exclusion (PIE) over sets of simultaneous problems, each problem at i forces C_j = 0 for j in [L_i, i-1] and C_j = 1 for j in [i, R_i]. Simultaneous problems must be disjoint intervals, leading to an O(N) DP.

## 2. Core Observation & Invariant
For two problem intervals [L_i, R_i] and [L_j, R_j] with i < j, if R_i >= L_j, they impose contradictory requirements on overlapping elements, so valid PIE configurations consist strictly of disjoint intervals [L_i, R_i]. Uncovered indices have 2 choices, each interval contributes factor (-1).

## 3. Step-by-Step Algorithm
1. 1. Find L_i = smallest j with B_j > A_i and R_i = largest j with A_j < B_i using two pointers in O(N).
2. 2. Group L_i by R_i.
3. 3. Compute dp[k] = 2 * dp[k-1] - sum_{L: R=k} dp[L-1] for k = 1..N with dp[0] = 1.
4. 4. Output dp[N] mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> A(n), B(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i] >> B[i];
    }

    // Two pointers or binary search to find L_i and R_i for each i
    // L_i: smallest j (0-indexed) such that B[j] > A[i]
    // R_i: largest j (0-indexed) such that A[j] < B[i]
    vector<vector<int>> by_R(n + 1);

    int ptr_B = 0;
    int ptr_A = 0;
    for (int i = 0; i < n; ++i) {
        while (ptr_B < n && B[ptr_B] <= A[i]) {
            ptr_B++;
        }
        int L_i = ptr_B; // 0-indexed

        while (ptr_A < n && A[ptr_A] < B[i]) {
            ptr_A++;
        }
        int R_i = ptr_A - 1; // 0-indexed

        // Convert to 1-indexed customer numbers
        int L = L_i + 1;
        int R = R_i + 1;
        if (R <= n) {
            by_R[R].push_back(L);
        }
    }

    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    for (int k = 1; k <= n; ++k) {
        dp[k] = (2 * dp[k - 1]) % MOD;
        for (int L : by_R[k]) {
            dp[k] = (dp[k] - dp[L - 1] + MOD) % MOD;
        }
    }

    cout << dp[n] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
