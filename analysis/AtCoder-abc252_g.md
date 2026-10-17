# Problem Analysis: AtCoder-abc252_g — Pre-Order

**Problem ID**: `AtCoder-abc252_g`  
**Contest**: `abc252`  
**Rating / Difficulty**: 2153  
**URL**: https://atcoder.jp/contests/abc252/tasks/abc252_g  
**VJudge Tag**: `[problem:AtCoder-abc252_g]`  
**Category File**: [`../categories/dynamic_programming/interval_dp_preorder_tree_reconstruction.md`](../categories/dynamic_programming/interval_dp_preorder_tree_reconstruction.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Given the DFS preorder sequence of a rooted tree where children of any vertex are visited in strictly increasing numerical order, count the number of valid rooted tree topologies modulo 998244353. Solved via interval DP tracking valid forests under root order constraints.

## 2. Core Observation & Invariant
Let dp[l][r] count valid trees rooted at a virtual node 0 covering the subsequence A[l..r-1]. The first child of 0 is A[l]. Either A[l] is the sole child of 0 (all remaining elements are in A[l]'s subtree, counted by dp[l+1][r]), or 0 has subsequent children. If the next child of 0 is A[k] (l+1 <= k < r), the condition that siblings are visited in increasing order demands A[l] < A[k]. Subtree of A[l] covers [l+1, k) and the remaining forest covers [k, r).

## 3. Step-by-Step Algorithm
1. Define DP state dp[l][r] for 2 <= l <= r <= N + 1 where base cases are dp[i][i] = 1.
2. Iterate over interval length len from 2 to N, and left endpoint l from 2 to N + 1 - len + 1.
3. Transition: dp[l][r] = dp[l+1][r] + sum_{l+1 <= k < r, A[l] < A[k]} (dp[l+1][k] * dp[k][r]) % MOD.
4. The total number of valid trees is given by dp[2][N+1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n + 2);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<vector<long long>> dp(n + 2, vector<long long>(n + 2, 0));

    for (int i = 1; i <= n + 1; ++i) {
        dp[i][i] = 1;
    }

    for (int len = 2; len <= n; ++len) {
        for (int l = 2; l + len - 1 <= n + 1; ++l) {
            int r = l + len - 1;
            long long res = dp[l + 1][r];
            for (int k = l + 1; k < r; ++k) {
                if (a[l] < a[k]) {
                    res = (res + dp[l + 1][k] * dp[k][r]) % MOD;
                }
            }
            dp[l][r] = res;
        }
    }

    cout << dp[2][n + 1] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
