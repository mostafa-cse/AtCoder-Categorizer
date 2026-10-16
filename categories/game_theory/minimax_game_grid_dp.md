# Minimax Game DP on 2D Grid

**Domain**: `Game Theory`  
**Subtopic**: `Minimax DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Minimax Game DP on 2D Grid**.

---

## Curated Problems

### [problem:AtCoder-abc201_d] — Game in Momotetsu World
- **Contest**: `abc201`
- **Rating / Difficulty**: 1317
- **Specific Skill**: Minimax Game DP on 2D Grid
- **Individual Analysis**: [`../../analysis/AtCoder-abc201_d.md`](../../analysis/AtCoder-abc201_d.md)
- **Problem Statement Summary**: An H x W grid with '+' (1 pt) and '-' (-1 pt). Players Takahashi (moves first) and Aoki start at (1, 1) and take turns moving right or down to (H, W). A player gains/loses points based on the cell entered. Predict winner assuming optimal play.
- **Core Insight**: Base case: at (H-1, W-1), no moves can be made, so dp = 0. From cell (r, c), moving to (nr, nc) gives value val(nr, nc) to the current player, and the opponent will achieve dp[nr][nc] in the remainder of the game. Thus, moving to (nr, nc) yields: val(nr, nc) - dp[nr][nc]. Optimal play chooses max over valid moves: dp[r][c] = max_{(nr, nc)} (val(nr, nc) - dp[nr][nc]).
- **Complexity**: Time: `O(H * W)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
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
