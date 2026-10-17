# Problem Analysis: AtCoder-abc227_f — I. Treasure Hunting

**Problem ID**: `AtCoder-abc227_f`  
**Contest**: `abc227`  
**Rating / Difficulty**: 2323  
**URL**: https://atcoder.jp/contests/abc227/tasks/abc227_f  
**VJudge Tag**: `[problem:AtCoder-abc227_f]`  
**Category File**: [`../categories/dynamic_programming/grid_path_k_largest_sum_threshold_dp.md`](../categories/dynamic_programming/grid_path_k_largest_sum_threshold_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
In an $H \times W$ grid with values $A_{i, j}$, find the minimum sum of the $K$ largest elements along any shortest path from $(1, 1)$ to $(H, W)$.

## 2. Core Observation & Invariant
If the $K$-th largest cell value on the optimal path is $X = A_{r, c}$, then every cell with $A_{i, j} > X$ must be counted, cells with $A_{i, j} < X$ cannot be counted, and cells with $A_{i, j} = X$ can optionally be counted to reach exactly $K$ selections.

## 3. Step-by-Step Algorithm
1. Iterate over all $O(HW)$ unique values $X = A_{r, c}$ present in the grid.
2. For each fixed $X$, define $dp[i][j][c]$ as the minimum sum of $c$ selected cells $\ge X$ along a path from $(1, 1)$ to $(i, j)$.
3. Transition in $O(1)$ based on whether $A_{i, j} > X$, $A_{i, j} = X$, or $A_{i, j} < X$, taking the minimum of $dp[H-1][W-1][K]$ over all $X$ in $O(H^2 W^2 K)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(H^2 W^2 K)`
- **Space Complexity**: `O(H W K)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, k;
    if (!(cin >> h >> w >> k)) return 0;

    vector<vector<long long>> a(h, vector<long long>(w));
    vector<long long> all_vals;
    all_vals.reserve(h * w);

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            cin >> a[i][j];
            all_vals.push_back(a[i][j]);
        }
    }

    sort(all_vals.begin(), all_vals.end());
    all_vals.erase(unique(all_vals.begin(), all_vals.end()), all_vals.end());

    long long ans = INF;

    vector<vector<vector<long long>>> dp(h, vector<vector<long long>>(w, vector<long long>(k + 1, INF)));

    for (long long x : all_vals) {
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                fill(dp[i][j].begin(), dp[i][j].end(), INF);
            }
        }

        long long v0 = a[0][0];
        if (v0 > x) {
            if (k >= 1) dp[0][0][1] = v0;
        } else if (v0 == x) {
            dp[0][0][0] = 0;
            if (k >= 1) dp[0][0][1] = v0;
        } else {
            dp[0][0][0] = 0;
        }

        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                if (i == 0 && j == 0) continue;
                long long val = a[i][j];
                for (int c = 0; c <= k; ++c) {
                    if (val > x) {
                        if (c > 0) {
                            long long prev = INF;
                            if (i > 0) prev = min(prev, dp[i - 1][j][c - 1]);
                            if (j > 0) prev = min(prev, dp[i][j - 1][c - 1]);
                            if (prev < INF) dp[i][j][c] = prev + val;
                        }
                    } else if (val == x) {
                        long long prev0 = INF;
                        if (i > 0) prev0 = min(prev0, dp[i - 1][j][c]);
                        if (j > 0) prev0 = min(prev0, dp[i][j - 1][c]);
                        dp[i][j][c] = min(dp[i][j][c], prev0);

                        if (c > 0) {
                            long long prev1 = INF;
                            if (i > 0) prev1 = min(prev1, dp[i - 1][j][c - 1]);
                            if (j > 0) prev1 = min(prev1, dp[i][j - 1][c - 1]);
                            if (prev1 < INF) dp[i][j][c] = prev1 + val;
                        }
                    } else {
                        long long prev = INF;
                        if (i > 0) prev = min(prev, dp[i - 1][j][c]);
                        if (j > 0) prev = min(prev, dp[i][j - 1][c]);
                        dp[i][j][c] = prev;
                    }
                }
            }
        }

        ans = min(ans, dp[h - 1][w - 1][k]);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
