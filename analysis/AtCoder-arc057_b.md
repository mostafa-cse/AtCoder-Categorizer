# Problem Analysis: AtCoder-arc057_b — 高橋君ゲーム

**Problem ID**: `AtCoder-arc057_b`  
**Contest**: `arc057`  
**Rating / Difficulty**: 2220  
**URL**: https://atcoder.jp/contests/arc057/tasks/arc057_b  
**VJudge Tag**: `[problem:AtCoder-arc057_b]`  
**Category File**: [`../categories/dynamic_programming/takahashi_game_state_inversion_win_rate_dp.md`](../categories/dynamic_programming/takahashi_game_state_inversion_win_rate_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Across N days with a_i games on day i, Takahashi wins exactly K total games. Mood strictly increases on days where the cumulative win rate strictly exceeds the previous day. Maximize the number of good days.

## 2. Core Observation & Invariant
Since total wins K <= 10^9 is large while days N <= 2000 is small, invert the DP state: dp[j] is the minimum cumulative wins required to achieve exactly j good days by the current day. Strict inequality w / S_i > dp[j-1] / S_{i-1} requires minimum wins w = floor(dp[j-1] * S_i / S_{i-1}) + 1. If K == sum(a_i), win rate is permanently 1.0, yielding answer 1.

## 3. Step-by-Step Algorithm
1. 1. If K == 0, return 0. If K == sum(a_i), return 1.
2. 2. Initialize dp array of size N + 1 with INF, dp[0] = 0, dp[1] = 1.
3. 3. For each day i from 2 to N: iterate j from i down to 1. If previous state dp[j-1] != INF, calculate minimum required cumulative wins need_w = (dp[j-1] * S_i) / S_{i-1} + 1.
4. 4. If need_w - dp[j-1] <= a_i and need_w <= K, update dp[j] = min(dp[j], need_w).
5. 5. Return the maximum j such that dp[j] <= K.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    long long total_games = 0;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        total_games += a[i];
    }

    if (k == 0) {
        cout << 0 << "\n";
        return 0;
    }
    if (k == total_games) {
        cout << 1 << "\n";
        return 0;
    }

    const long long INF = 2e18;
    vector<long long> dp(n + 1, INF);
    dp[0] = 0;
    dp[1] = 1;

    long long s = a[0];
    for (int i = 1; i < n; i++) {
        long long cur_a = a[i];
        long long new_s = s + cur_a;
        vector<long long> new_dp = dp;

        for (int j = 1; j <= i + 1; j++) {
            if (dp[j - 1] != INF) {
                // need_w > dp[j-1] * new_s / s
                long long need_w = (dp[j - 1] * new_s) / s + 1;
                long long diff = need_w - dp[j - 1];
                if (diff <= cur_a && need_w <= k) {
                    if (need_w < new_dp[j]) {
                        new_dp[j] = need_w;
                    }
                }
            }
        }
        dp = move(new_dp);
        s = new_s;
    }

    int ans = 0;
    for (int j = 0; j <= n; j++) {
        if (dp[j] <= k) ans = j;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
