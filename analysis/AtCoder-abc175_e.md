# Problem Analysis: AtCoder-abc175_e — Picking Goods

**Problem ID**: `AtCoder-abc175_e`  
**Contest**: `abc175`  
**Rating / Difficulty**: 1554  
**URL**: https://atcoder.jp/contests/abc175/tasks/abc175_e  
**VJudge Tag**: `[problem:AtCoder-abc175_e]`  
**Category File**: [`../categories/dp/grid_dp_row_item_capacity.md`](../categories/dp/grid_dp_row_item_capacity.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `2D Grid DP`  
- **Topic (Skill)**: `2D Grid DP with Per-Row Item Capacity Constraint (At Most 3 Items)`  

---

## 1. Problem Statement & Key Idea
An R x C grid with K items. Move from (1, 1) to (R, C) using right and down moves. In each row, you may pick at most 3 items. Maximize the total value of items collected.

**Key Insight**: 3D DP state: `dp[r][c][k]` representing the maximum value at cell (r, c) having picked k items in row r (k in 0..3).

## 2. Core Observation & Invariant
When moving right: k can increase by 1 if an item is picked at (r, c). When moving down: the row resets, so k resets to 0, taking the maximum over all 0..3 items picked from the previous row.

## 3. Step-by-Step Algorithm
1. Initialize dp[R+1][C+1][4] with 0.
2. For r from 1 to R:
3.   For c from 1 to C:
4.     val = item_value[r][c].
5.     Transitions from (r-1, c) moving down:
6.       max_prev_row = max_{k=0..3} dp[r-1][c][k].
7.       dp[r][c][0] = max(dp[r][c][0], max_prev_row).
8.       If val > 0: dp[r][c][1] = max(dp[r][c][1], max_prev_row + val).
9.     Transitions from (r, c-1) moving right:
10.       For k from 0 to 3:
11.         dp[r][c][k] = max(dp[r][c][k], dp[r][c-1][k]).
12.         If val > 0 and k < 3:
13.           dp[r][c][k+1] = max(dp[r][c][k+1], dp[r][c-1][k] + val).
14. Print max_{k=0..3} dp[R][C][k].

## 4. Complexity Analysis
- **Time Complexity**: `O(R * C)`
- **Space Complexity**: `O(R * C)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, K;
    if (!(cin >> R >> C >> K)) return 0;

    vector<vector<long long>> val(R + 1, vector<long long>(C + 1, 0));
    for (int i = 0; i < K; ++i) {
        int r, c;
        long long v;
        cin >> r >> c >> v;
        val[r][c] = v;
    }

    // dp[r][c][k]: max value at (r, c) with k items picked on row r
    vector<vector<vector<long long>>> dp(R + 1, vector<vector<long long>>(C + 1, vector<long long>(4, 0)));

    for (int r = 1; r <= R; ++r) {
        for (int c = 1; c <= C; ++c) {
            long long item = val[r][c];

            // Transition from above (r - 1, c): row resets
            long long max_above = 0;
            for (int k = 0; k < 4; ++k) max_above = max(max_above, dp[r - 1][c][k]);

            dp[r][c][0] = max(dp[r][c][0], max_above);
            if (item > 0) {
                dp[r][c][1] = max(dp[r][c][1], max_above + item);
            }

            // Transition from left (r, c - 1): same row
            for (int k = 0; k < 4; ++k) {
                dp[r][c][k] = max(dp[r][c][k], dp[r][c - 1][k]);
            }
            if (item > 0) {
                for (int k = 0; k < 3; ++k) {
                    dp[r][c][k + 1] = max(dp[r][c][k + 1], dp[r][c - 1][k] + item);
                }
            }
        }
    }

    long long ans = 0;
    for (int k = 0; k < 4; ++k) ans = max(ans, dp[R][C][k]);

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multi-dimensional grid DP tracking localized row-reset resource constraints.
- **Reusable Pattern**: `Row-Constrained Grid DP: dp[r][c][k] where moving down transitions from max_k dp[r-1][c][k].`
