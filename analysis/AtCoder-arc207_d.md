# Problem Analysis: AtCoder-arc207_d — D - Devourers and Cake

**Problem ID**: `AtCoder-arc207_d`  
**Contest**: `arc207`  
**Rating / Difficulty**: 2957  
**URL**: https://atcoder.jp/contests/arc207/tasks/arc207_d  
**VJudge Tag**: `[problem:AtCoder-arc207_d]`  
**Category File**: [`../categories/game_theory/grid_row_col_deletion_center_inversion_game.md`](../categories/game_theory/grid_row_col_deletion_center_inversion_game.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
Two players play an impartial game on an H x W binary grid. A player can remove an entire boundary row/column if its sum is non-zero. Determine who wins under optimal play across T testcases.

## 2. Core Observation & Invariant
Analyze the geometry of shrinking the rectangle around the grid center. If one dimension is odd and the other is even, the game directly reduces to whether the central column/row has a '1' or whether the center forms a specific alternating cross structure. When both dimensions have the same parity, the first move transitions into an odd-even subgrid with inverted polarity. Thus, the winning condition decomposes into checking the central cross cells and testing the 4 single-boundary reductions in O(1) per state.

## 3. Step-by-Step Algorithm
1. 1. For an odd-even grid, inspect the central 2 columns (or rows) and their immediate vertical neighbours.
2. 2. For even-even or odd-odd grids, analyze the 4 candidate eaten subgrids (top, bottom, left, right).
3. 3. Evaluate whether any transition leaves the second player with a losing state (backward induction).
4. 4. Output 'First' or 'Second' for each test case.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool solve_case2(const vector<string>& grid) {
    int H = grid.size();
    int W = grid[0].size();
    vector<string> g;
    if (H % 2 == 0) {
        g.assign(W, string(H, ' '));
        for (int r = 0; r < H; ++r) {
            for (int c = 0; c < W; ++c) {
                g[c][r] = grid[r][c];
            }
        }
        H = g.size();
        W = g[0].size();
    } else {
        g = grid;
    }

    int r = H / 2;
    int c1 = W / 2 - 1;
    int c2 = W / 2;

    if (g[r][c1] == '1' || g[r][c2] == '1') return true;

    if (H >= 3) {
        if (g[r - 1][c1] == '1' && g[r][c1] == '0' && g[r + 1][c1] == '1') return true;
        if (g[r - 1][c2] == '1' && g[r][c2] == '0' && g[r + 1][c2] == '1') return true;
    }

    return false;
}

vector<string> invert_grid(const vector<string>& grid) {
    int H = grid.size();
    int W = grid[0].size();
    vector<string> res = grid;
    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            res[r][c] = (grid[r][c] == '0' ? '1' : '0');
        }
    }
    return res;
}

vector<vector<string>> get_subgrids(const vector<string>& grid) {
    int H = grid.size();
    int W = grid[0].size();
    vector<vector<string>> res;

    if (H > 1) {
        // Eat top
        vector<string> top(grid.begin() + 1, grid.end());
        res.push_back(top);
        // Eat bottom
        vector<string> bot(grid.begin(), grid.end() - 1);
        res.push_back(bot);
    }
    if (W > 1) {
        // Eat left
        vector<string> left(H);
        for (int r = 0; r < H; ++r) left[r] = grid[r].substr(1);
        res.push_back(left);
        // Eat right
        vector<string> right(H);
        for (int r = 0; r < H; ++r) right[r] = grid[r].substr(0, W - 1);
        res.push_back(right);
    }
    return res;
}

string solve_game(const vector<string>& grid) {
    int H = grid.size();
    int W = grid[0].size();

    if (H % 2 == 0 && W % 2 == 0) {
        auto subs = get_subgrids(grid);
        for (const auto& g : subs) {
            if (!solve_case2(invert_grid(g))) {
                return "First";
            }
        }
        return "Second";
    }

    if ((H % 2) != (W % 2)) {
        return solve_case2(grid) ? "First" : "Second";
    }

    int r = H / 2;
    int c = W / 2;

    if (grid[r][c] == '0') return "Second";
    if (H >= 3 && grid[r - 1][c] == '0' && grid[r][c] == '1' && grid[r + 1][c] == '0') return "Second";
    if (W >= 3 && grid[r][c - 1] == '0' && grid[r][c] == '1' && grid[r][c + 1] == '0') return "Second";

    auto subs = get_subgrids(grid);
    for (const auto& g : subs) {
        if (!solve_case2(invert_grid(g))) {
            return "First";
        }
    }
    return "Second";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (!(cin >> T)) return 0;

    while (T--) {
        int N, M;
        cin >> N >> M;
        vector<string> grid(N);
        for (int i = 0; i < N; ++i) cin >> grid[i];

        cout << solve_game(grid) << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
