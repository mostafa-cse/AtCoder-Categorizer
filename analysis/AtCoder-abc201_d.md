# Problem Analysis: AtCoder-abc201_d — Game in Momotetsu World

**Problem ID**: `AtCoder-abc201_d`  
**Contest**: `abc201`  
**Rating / Difficulty**: 1317  
**URL**: https://atcoder.jp/contests/abc201/tasks/abc201_d  
**VJudge Tag**: `[problem:AtCoder-abc201_d]`  
**Category File**: [`../categories/game_theory/minimax_game_grid_dp.md`](../categories/game_theory/minimax_game_grid_dp.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Minimax DP`  
- **Topic (Skill)**: `Minimax Game DP on 2D Grid`  

---

## 1. Problem Statement & Key Idea
An H x W grid with '+' (1 pt) and '-' (-1 pt). Players Takahashi (moves first) and Aoki start at (1, 1) and take turns moving right or down to (H, W). A player gains/loses points based on the cell entered. Predict winner assuming optimal play.

**Key Idea**: Define dp[r][c] as the maximum value of (current player's score - opponent's score) from cell (r, c) to (H, W).

## 2. Core Observation & Invariant
Base case: at (H-1, W-1), no moves can be made, so dp = 0. From cell (r, c), moving to (nr, nc) gives value val(nr, nc) to the current player, and the opponent will achieve dp[nr][nc] in the remainder of the game. Thus, moving to (nr, nc) yields: val(nr, nc) - dp[nr][nc]. Optimal play chooses max over valid moves: dp[r][c] = max_{(nr, nc)} (val(nr, nc) - dp[nr][nc]).

## 3. Step-by-Step Algorithm
1. Initialize dp[H][W] to 0.
2. Iterate r from H - 1 down to 0, c from W - 1 down to 0:
3.   If r == H - 1 && c == W - 1: dp[r][c] = 0, continue.
4.   dp[r][c] = -INF.
5.   If c + 1 < W: dp[r][c] = max(dp[r][c], val[r][c+1] - dp[r][c+1]).
6.   If r + 1 < H: dp[r][c] = max(dp[r][c], val[r+1][c] - dp[r+1][c]).
7. If dp[0][0] > 0 print 'Takahashi'; if dp[0][0] < 0 print 'Aoki'; else print 'Draw'.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    vector<vector<int>> val(h, vector<int>(w));
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            val[r][c] = (grid[r][c] == '+' ? 1 : -1);
        }
    }

    vector<vector<int>> dp(h, vector<int>(w, 0));

    for (int r = h - 1; r >= 0; --r) {
        for (int c = w - 1; c >= 0; --c) {
            if (r == h - 1 && c == w - 1) continue;

            int best = -INF;
            if (c + 1 < w) {
                best = max(best, val[r][c + 1] - dp[r][c + 1]);
            }
            if (r + 1 < h) {
                best = max(best, val[r + 1][c] - dp[r + 1][c]);
            }
            dp[r][c] = best;
        }
    }

    if (dp[0][0] > 0) cout << "Takahashi\n";
    else if (dp[0][0] < 0) cout << "Aoki\n";
    else cout << "Draw\n";

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Negamax / Minimax formulation for two-player zero-sum sequential games on DAGs.
- **Reusable Pattern**: `Minimax score difference: dp[u] = max_{(u, v)} (gain(v) - dp[v]).`
