# Problem Analysis: AtCoder-abc162_f — Select Half

**Problem ID**: `AtCoder-abc162_f`  
**Contest**: `abc162`  
**Rating / Difficulty**: 1764  
**URL**: https://atcoder.jp/contests/abc162/tasks/abc162_f  
**VJudge Tag**: `[problem:AtCoder-abc162_f]`  
**Category File**: [`../categories/dp/skip_budget_dp_select_half.md`](../categories/dp/skip_budget_dp_select_half.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Non-Adjacent Selection via Skip-Budget DP`  

---

## 1. Problem Statement & Key Idea
Given an array A of N integers. Choose floor(N / 2) elements such that no two chosen elements are adjacent. Maximize the sum of chosen elements.

**Key Insight**: To choose floor(N/2) non-adjacent elements out of N, the total number of 'extra skips' allowed is at most 1 (for even N) or at most 2 (for odd N). Maintain DP state dp[i][skip] tracking the maximum sum using skip extra skips.

## 2. Core Observation & Invariant
Transitions: at index i, you either choose A[i] (skipping the immediate next index) or take an extra skip to move to i + 1. Total states O(N * 3), taking O(N) time.

## 3. Step-by-Step Algorithm
1. Let max_skips = N % 2 == 0 ? 1 : 2.
2. Initialize dp[N + 1][3] with -INF.
3. dp[0][0] = 0.
4. For i = 0 to N - 1:
5.   For skip = 0 to max_skips:
6.     if dp[i][skip] == -INF: continue.
7.     // Choice 1: Take A[i+1], advance to i + 2
8.     if (i + 1 <= N) dp[min(N, i + 2)][skip] = max(dp[min(N, i + 2)][skip], dp[i][skip] + A[i + 1]).
9.     // Choice 2: Extra skip, advance to i + 1
10.     if (skip + 1 <= max_skips) dp[i + 1][skip + 1] = max(dp[i + 1][skip + 1], dp[i][skip]).
11. Answer is max over valid final states.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

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
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int max_skips = (n % 2 == 0) ? 1 : 2;
    // dp[i][skip]: after considering elements up to index i-1, with 'skip' extra skips used
    vector<vector<long long>> dp(n + 2, vector<long long>(max_skips + 1, -INF));
    dp[0][0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int s = 0; s <= max_skips; ++s) {
            if (dp[i][s] == -INF) continue;

            // Option 1: Pick a[i], must skip i+1, so jump to i+2
            int next_i = min(n, i + 2);
            dp[next_i][s] = max(dp[next_i][s], dp[i][s] + a[i]);

            // Option 2: Do not pick a[i], spend 1 extra skip, jump to i+1
            if (s + 1 <= max_skips) {
                dp[i + 1][s + 1] = max(dp[i + 1][s + 1], dp[i][s]);
            }
        }
    }

    long long ans = -INF;
    for (int s = 0; s <= max_skips; ++s) {
        ans = max(ans, dp[n][s]);
        ans = max(ans, dp[n + 1][s]);
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Dynamic programming with bounded slack/skip budget for non-adjacent element selection.
- **Reusable Pattern**: `Skip-Budget DP: dp[i][slack] tracking exact count of omitted positions.`
