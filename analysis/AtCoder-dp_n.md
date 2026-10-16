# Problem Analysis: AtCoder-dp_n — Slimes

**Problem ID**: `AtCoder-dp_n`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1600  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_n  
**VJudge Tag**: `[problem:AtCoder-dp_n]`  
**Category File**: [`../categories/dp/interval_dp.md`](../categories/dp/interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Merge adjacent slimes pairwise into one slime with minimum total combination cost.

**Core Idea**: The final combine step joins two sub-blocks [l, k] and [k+1, r] with cost sum(a[l..r]).

## 2. Core Observation & Invariant
dp[l][r] = sum(a[l..r]) + min_{l <= k < r} (dp[l][k] + dp[k+1][r]). Prefix sums yield sum(a[l..r]) in O(1).

## 3. Step-by-Step Algorithm
1. Precompute prefix sums.
2. For len = 2..N: for l = 1..N-len+1: r = l+len-1: dp[l][r] = min_{k=l}^{r-1}(dp[l][k] + dp[k+1][r]) + (pref[r] - pref[l-1]).
3. Return dp[1][N].

## 4. Complexity Analysis
Time: O(N^3) standard, O(N^2) via Knuth optimization.

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    vector<long long> pref(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        pref[i + 1] = pref[i] + a[i];
    }

    vector<vector<long long>> dp(n, vector<long long>(n, 0));

    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l <= n - len; ++l) {
            int r = l + len - 1;
            dp[l][r] = INF;
            long long cost = pref[r + 1] - pref[l];
            for (int k = l; k < r; ++k) {
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + cost);
            }
        }
    }

    cout << dp[0][n - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Optimal binary search tree / matrix chain multiplication DP.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Interval DP with split-point minimization and cost of merging subproblems.
- **Reusable Pattern**: `Split-point interval DP.`

---
Back to [Interval DP / Range DP / Matrix Chain Multiplication (MCM)](../categories/dp/interval_dp.md) | [Categories Directory](../categories/README.md)