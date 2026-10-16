# Problem Analysis: AtCoder-arc043_b — Difficulty

**Problem ID**: `AtCoder-arc043_b`  
**Contest**: `arc043`  
**Rating / Difficulty**: 1606  
**URL**: https://atcoder.jp/contests/arc043/tasks/arc043_b  
**VJudge Tag**: `[problem:AtCoder-arc043_b]`  
**Category File**: [`../categories/dp/multistep_increasing_ratio_dp.md`](../categories/dp/multistep_increasing_ratio_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `4-Step Increasing Sequence with 2x Ratio via Coordinate Prefix Sums`  

---

## 1. Problem Statement & Key Idea
Given N problems with difficulties D_1, ..., D_N. Select 4 problems with difficulties (A, B, C, D) such that 2A <= B, 2B <= C, and 2C <= D. Find the number of valid 4-problem selections, modulo 10^9 + 7.

**Key Insight**: Multi-stage DP. Sort difficulties D. Let dp[k][i] be the number of valid k-problem sequences ending with D[i]. Transitions sum over all j where 2 * D[j] <= D[i], accelerated using prefix sums.

## 2. Core Observation & Invariant
Since 2 * D[j] <= D[i] is monotonic, for each i we can use std::upper_bound to find the largest index j with D[j] <= D[i] / 2. Then transition in O(1) using prefix sums of the previous DP stage.

## 3. Step-by-Step Algorithm
1. Sort D in ascending order.
2. Initialize dp[1][i] = 1 for all i = 0..N-1.
3. For stage k = 1 to 3:
4.   Compute prefix sums pref[i] = sum_{j=0}^{i-1} dp[k][j] % MOD.
5.   For i = 0 to N - 1:
6.     Find count of elements j with D[j] <= D[i] / 2 using upper_bound on D.
7.     dp[k + 1][i] = pref[count].
8. Sum dp[4][i] over all i and print modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(4 * N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> d(n);
    for (int i = 0; i < n; ++i) {
        cin >> d[i];
    }

    sort(d.begin(), d.end());

    vector<long long> dp(n, 1);

    for (int stage = 1; stage <= 3; ++stage) {
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = (pref[i] + dp[i]) % MOD;
        }

        vector<long long> next_dp(n, 0);
        for (int i = 0; i < n; ++i) {
            int target = d[i] / 2;
            int count = upper_bound(d.begin(), d.end(), target) - d.begin();
            next_dp[i] = pref[count];
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        ans = (ans + dp[i]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multi-stage chain selection DP with prefix-sum binary search acceleration.
- **Reusable Pattern**: `Ratio-Constrained Chain DP: dp[k+1][i] = pref_dp[k][upper_bound(D[i]/2)].`
