# Problem Analysis: AtCoder-abc358_g — AtCoder Tour

**Problem ID**: `AtCoder-abc358_g`  
**Contest**: `abc358`  
**Rating / Difficulty**: 1737  
**URL**: https://atcoder.jp/contests/abc358/tasks/abc358_g  
**VJudge Tag**: `[problem:AtCoder-abc358_g]`  
**Category File**: [`../categories/dp/bounded_step_grid_dp_infinite_stay.md`](../categories/dp/bounded_step_grid_dp_infinite_stay.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Grid DP`  
- **Topic (Skill)**: `Grid Graph Bounded Step DP with Infinite Stay Greedy Extension`  

---

## 1. Problem Statement & Key Idea
Given an H x W grid (H, W <= 50) and K <= 10^9 steps. You start at (S_r, S_c). At each step, you can move to an adjacent cell or stay in place, gaining cell (i, j)'s points A_{i, j}. Maximize points after K steps.

**Key Insight**: The maximum number of steps taken before settling to stay indefinitely at the highest-scoring cell is bounded by H * W <= 2500. Compute dp[t][r][c] = max score reaching (r, c) in t moves without staying, then add (K - t) * A_{r, c}.

## 2. Core Observation & Invariant
Iterating t from 1 to min(K, H * W) takes at most 2500 * 2500 * 4 ~ 2.5 * 10^7 transitions, easily fitting within the 2-second time limit.

## 3. Step-by-Step Algorithm
1. Initialize dp[r][c] = -INF, dp[S_r][S_c] = 0.
2. ans = K * A[S_r][S_c].
3. For t = 1 to min(K, H * W):
4.   next_dp[r][c] = max over neighbors of dp[nr][nc] + A[r][c].
5.   dp = next_dp.
6.   ans = max(ans, dp[r][c] + (K - t) * A[r][c]).
7. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W * min(K, H * W))`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;
const int dr[] = {0, 0, 1, -1};
const int dc[] = {1, -1, 0, 0};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    long long k;
    if (!(cin >> h >> w >> k)) return 0;

    int sr, sc;
    cin >> sr >> sc;
    --sr; --sc;

    vector<vector<long long>> a(h, vector<long long>(w));
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) cin >> a[i][j];
    }

    vector<vector<long long>> dp(h, vector<long long>(w, -INF));
    dp[sr][sc] = 0;

    long long ans = k * a[sr][sc];
    int max_steps = min((long long)h * w, k);

    for (int step = 1; step <= max_steps; ++step) {
        vector<vector<long long>> next_dp(h, vector<long long>(w, -INF));

        for (int r = 0; r < h; ++r) {
            for (int c = 0; c < w; ++c) {
                if (dp[r][c] == -INF) continue;
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < h && nc >= 0 && nc < w) {
                        next_dp[nr][nc] = max(next_dp[nr][nc], dp[r][c] + a[nr][nc]);
                    }
                }
            }
        }

        dp = move(next_dp);

        for (int r = 0; r < h; ++r) {
            for (int c = 0; c < w; ++c) {
                if (dp[r][c] != -INF) {
                    long long total = dp[r][c] + (k - step) * a[r][c];
                    ans = max(ans, total);
                }
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bounding finite wander phases before an infinite stay greedy choice.
- **Reusable Pattern**: `Bounded Roam + Stay DP: Limit dynamic path length to |V| and extrapolate stay duration.`
