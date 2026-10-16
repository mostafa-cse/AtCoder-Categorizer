# Problem Analysis: AtCoder-dp_h — Grid 1

**Problem ID**: `AtCoder-dp_h`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1050  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_h  
**VJudge Tag**: `[problem:AtCoder-dp_h]`  
**Category File**: [`../categories/dp/grid_dp.md`](../categories/dp/grid_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Grid DP / Path Counting with Obstacles`  

---

## 1. Problem Statement & Key Idea
Count paths from top-left (1,1) to bottom-right (H,W) moving only right and down, avoiding obstacle walls '#'. Output modulo 10^9+7.

**Core Idea**: Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.

## 2. Core Observation & Invariant
Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.

## 3. Step-by-Step Algorithm
1. dp[1][1] = 1.
2. For r in 1..H, c in 1..W: if grid[r][c] == '#': dp[r][c] = 0; else dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % MOD.
3. Return dp[H][W].

## 4. Complexity Analysis
Time: O(H * W), Space: O(W).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) cin >> grid[i];

    vector<vector<int>> dp(h, vector<int>(w, 0));
    dp[0][0] = 1;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '#') {
                dp[r][c] = 0;
                continue;
            }
            if (r > 0) dp[r][c] = (dp[r][c] + dp[r - 1][c]) % MOD;
            if (c > 0) dp[r][c] = (dp[r][c] + dp[r][c - 1]) % MOD;
        }
    }

    cout << dp[h - 1][w - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Grid combinatorial dynamic programming.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Grid boundary enforcement, obstacle nullification, and modulo arithmetic accumulation.
- **Reusable Pattern**: `2D additive grid DP.`

---
Back to [Grid DP / Path Counting with Obstacles](../categories/dp/grid_dp.md) | [Categories Directory](../categories/README.md)