# Problem Analysis: AtCoder-arc157_c — YY Square

**Problem ID**: `AtCoder-arc157_c`  
**Contest**: `arc157`  
**Rating / Difficulty**: 1802  
**URL**: https://atcoder.jp/contests/arc157/tasks/arc157_c  
**VJudge Tag**: `[problem:AtCoder-arc157_c]`  
**Category File**: [`../categories/dp/moment_tracking_grid_path_dp.md`](../categories/dp/moment_tracking_grid_path_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Grid DP`  
- **Topic (Skill)**: `Moment-Tracking Grid Path DP (E[X^2] Expansion)`  

---

## 1. Problem Statement & Key Idea
An H x W grid has cells labeled 'X' or 'Y'. Move from (1, 1) to (H, W) taking steps right or down. For each step between two cells that are both 'Y', add 1 to the path score. Find the sum of (score)^2 over all paths, modulo 998244353.

**Key Insight**: To compute sum of squared scores, track the 0th, 1st, and 2nd algebraic moments along paths: dp0 = number of paths, dp1 = sum of scores, dp2 = sum of squared scores. When taking a step that adds 1: (x + 1)^2 = x^2 + 2x + 1.

## 2. Core Observation & Invariant
Transitions at cell (r, c) incoming from (pr, pc): if step is 'Y'->'Y' (delta = 1), new_dp2 = dp2 + 2 * dp1 + dp0, new_dp1 = dp1 + dp0, new_dp0 = dp0. If delta = 0, new_dp2 = dp2, new_dp1 = dp1, new_dp0 = dp0.

## 3. Step-by-Step Algorithm
1. Initialize dp0[H][W], dp1[H][W], dp2[H][W] = 0.
2. dp0[0][0] = 1.
3. For r = 0 to H - 1, c = 0 to W - 1:
4.   For each neighbor (nr, nc) in {(r+1, c), (r, c+1)} within grid:
5.     delta = (grid[r][c] == 'Y' && grid[nr][nc] == 'Y') ? 1 : 0;
6.     dp0[nr][nc] = (dp0[nr][nc] + dp0[r][c]) % MOD;
7.     dp1[nr][nc] = (dp1[nr][nc] + dp1[r][c] + delta * dp0[r][c]) % MOD;
8.     dp2[nr][nc] = (dp2[nr][nc] + dp2[r][c] + 2 * delta * dp1[r][c] + delta * dp0[r][c]) % MOD;
9. Print dp2[H - 1][W - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) cin >> grid[i];

    vector<vector<long long>> dp0(h, vector<long long>(w, 0));
    vector<vector<long long>> dp1(h, vector<long long>(w, 0));
    vector<vector<long long>> dp2(h, vector<long long>(w, 0));

    dp0[0][0] = 1;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            long long p0 = dp0[r][c], p1 = dp1[r][c], p2 = dp2[r][c];
            if (p0 == 0) continue;

            // Step down
            if (r + 1 < h) {
                int delta = (grid[r][c] == 'Y' && grid[r + 1][c] == 'Y') ? 1 : 0;
                dp0[r + 1][c] = (dp0[r + 1][c] + p0) % MOD;
                dp1[r + 1][c] = (dp1[r + 1][c] + p1 + delta * p0) % MOD;
                dp2[r + 1][c] = (dp2[r + 1][c] + p2 + 2LL * delta * p1 + delta * p0) % MOD;
            }

            // Step right
            if (c + 1 < w) {
                int delta = (grid[r][c] == 'Y' && grid[r][c + 1] == 'Y') ? 1 : 0;
                dp0[r][c + 1] = (dp0[r][c + 1] + p0) % MOD;
                dp1[r][c + 1] = (dp1[r][c + 1] + p1 + delta * p0) % MOD;
                dp2[r][c + 1] = (dp2[r][c + 1] + p2 + 2LL * delta * p1 + delta * p0) % MOD;
            }
        }
    }

    cout << dp2[h - 1][w - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Expanding quadratic quantities into linear DP moment states (count, sum, square sum).
- **Reusable Pattern**: `Quadratic Moment DP: Track (dp0, dp1, dp2) with (x + 1)^2 = x^2 + 2x + 1.`
