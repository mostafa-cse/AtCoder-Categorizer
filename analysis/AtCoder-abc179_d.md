# Problem Analysis: AtCoder-abc179_d — Leaping Tak

**Problem ID**: `AtCoder-abc179_d`  
**Contest**: `abc179`  
**Rating / Difficulty**: 1251  
**URL**: https://atcoder.jp/contests/abc179/tasks/abc179_d  
**VJudge Tag**: `[problem:AtCoder-abc179_d]`  
**Category File**: [`../categories/dp/dp_range_transitions_prefix_sums.md`](../categories/dp/dp_range_transitions_prefix_sums.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `DP Optimization`  
- **Topic (Skill)**: `DP with Range Transitions Accelerated by Prefix Sums`  

---

## 1. Problem Statement & Key Idea
Start at cell 1, reach cell N. You can jump by any distance in K given intervals [L_i, R_i]. Find the number of paths from 1 to N modulo 998244353.

**Key Idea**: Let dp[i] be the number of paths to cell i. Base case: dp[1] = 1. Transition: dp[i] = sum_{j=1}^K sum_{d = L_j}^{R_j} dp[i - d].

## 2. Core Observation & Invariant
The transition sum_{d = L}^{R} dp[i - d] is a contiguous range sum on previous DP values: sum_{x = max(1, i - R)}^{i - L} dp[x]. Maintaining prefix sums pref[x] = sum_{y=1}^x dp[y] allows each interval range sum to be computed in O(1)!

## 3. Step-by-Step Algorithm
1. Initialize dp array and prefix sum array pref of size N + 1 to 0; dp[1] = 1, pref[1] = 1.
2. For i from 2 to N:
3.   For each interval [L, R]: l_bound = max(1, i - R), r_bound = i - L; if l_bound <= r_bound: dp[i] = (dp[i] + pref[r_bound] - pref[l_bound - 1]) % MOD.
4.   pref[i] = (pref[i - 1] + dp[i]) % MOD.
5. Output dp[N] (adjusted for positive modulo).

## 4. Complexity Analysis
- **Time Complexity**: `O(N * K)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

struct Interval {
    int l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<Interval> intervals(k);
    for (int i = 0; i < k; ++i) {
        cin >> intervals[i].l >> intervals[i].r;
    }

    vector<long long> dp(n + 1, 0);
    vector<long long> pref(n + 1, 0);

    dp[1] = 1;
    pref[1] = 1;

    for (int i = 2; i <= n; ++i) {
        for (const auto& iv : intervals) {
            int r_idx = i - iv.l;
            int l_idx = max(1, i - iv.r);
            if (l_idx <= r_idx && r_idx >= 1) {
                long long term = (pref[r_idx] - pref[l_idx - 1] + MOD) % MOD;
                dp[i] = (dp[i] + term) % MOD;
            }
        }
        pref[i] = (pref[i - 1] + dp[i]) % MOD;
    }

    cout << dp[n] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Accelerating interval-based DP transitions using running prefix sums.
- **Reusable Pattern**: `Range transition DP: sum_{d in [L, R]} dp[i - d] = pref[i - L] - pref[i - R - 1].`
