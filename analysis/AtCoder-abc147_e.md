# Problem Analysis: AtCoder-abc147_e — Balanced Path

**Problem ID**: `AtCoder-abc147_e`  
**Contest**: `abc147`  
**Rating / Difficulty**: 1713  
**URL**: https://atcoder.jp/contests/abc147/tasks/abc147_e  
**VJudge Tag**: `[problem:AtCoder-abc147_e]`  
**Category File**: [`../categories/dp/grid_path_subset_sum_bitset.md`](../categories/dp/grid_path_subset_sum_bitset.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Grid DP`  
- **Topic (Skill)**: `Grid Path Subset Sum with Bitset Acceleration`  

---

## 1. Problem Statement & Key Idea
Given an H x W grid where each cell (i, j) has values A_{i, j} and B_{i, j}. Move from (1, 1) to (H, W) taking steps down or right. At each cell, choose either +|A - B| or -|A - B|. Minimize the absolute value of the final sum. (H, W <= 80, A, B <= 80).

**Key Insight**: The maximum possible sum is (H + W - 1) * 80 <= 159 * 80 = 12720. Using a bitset of size 25441 (with offset 12720), maintain all reachable difference sums at cell (i, j) by shifting left and right by D_{i, j}.

## 2. Core Observation & Invariant
Bitset operations process 64 states simultaneously per CPU cycle, completing in under 20 ms for 80 x 80 cells.

## 3. Step-by-Step Algorithm
1. Let D_{i, j} = |A_{i, j} - B_{i, j}| and OFFSET = 12720.
2. Initialize bitset dp[H][W].
3. dp[0][0][OFFSET + D_{0,0}] = 1; dp[0][0][OFFSET - D_{0,0}] = 1.
4. For each cell (i, j):
5.   accumulate previous states: from (i - 1, j) and (i, j - 1).
6.   dp[i][j] = (prev << D_{i, j}) | (prev >> D_{i, j}).
7. Find min |k - OFFSET| such that dp[H-1][W-1][k] == 1.
8. Print result.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W * MAX_SUM / 64)`
- **Space Complexity**: `O(H * W * MAX_SUM / 64)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;

const int MAX_VAL = 12800;
const int OFFSET = MAX_VAL;
const int SIZE = 2 * MAX_VAL + 5;

bitset<SIZE> dp[85][85];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<vector<int>> a(h, vector<int>(w));
    vector<vector<int>> b(h, vector<int>(w));
    vector<vector<int>> d(h, vector<int>(w));

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) cin >> a[i][j];
    }
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            cin >> b[i][j];
            d[i][j] = abs(a[i][j] - b[i][j]);
        }
    }

    dp[0][0][OFFSET + d[0][0]] = 1;
    dp[0][0][OFFSET - d[0][0]] = 1;

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (i == 0 && j == 0) continue;
            bitset<SIZE> prev;
            if (i > 0) prev |= dp[i - 1][j];
            if (j > 0) prev |= dp[i][j - 1];

            int diff = d[i][j];
            dp[i][j] = (prev << diff) | (prev >> diff);
        }
    }

    int min_diff = 1e9;
    for (int k = 0; k < SIZE; ++k) {
        if (dp[h - 1][w - 1][k]) {
            min_diff = min(min_diff, abs(k - OFFSET));
        }
    }

    cout << min_diff << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitset acceleration for reachable sum state propagation on grids.
- **Reusable Pattern**: `Grid Subset Sum: dp[i][j] = (prev << D) | (prev >> D) using bitset.`
