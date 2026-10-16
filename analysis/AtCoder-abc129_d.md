# Problem Analysis: AtCoder-abc129_d — Lamp

**Problem ID**: `AtCoder-abc129_d`  
**Contest**: `abc129`  
**Rating / Difficulty**: 1103  
**URL**: https://atcoder.jp/contests/abc129/tasks/abc129_d  
**VJudge Tag**: `[problem:AtCoder-abc129_d]`  
**Category File**: [`../categories/dp/four_way_ray_dp_precomputation.md`](../categories/dp/four_way_ray_dp_precomputation.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Grid DP`  
- **Topic (Skill)**: `4-Directional Prefix Ray DP Precomputation`  

---

## 1. Problem Statement & Key Idea
An H x W grid has '.' and '#'. Place a lamp at a '.' cell to illuminate cells in 4 directions until reaching an obstacle. Maximize illuminated cells (H, W <= 2000).

**Key Idea**: For each cell (r, c), the illuminated cells along its row and column can be decomposed into consecutive '.' cells in 4 directions: Left, Right, Up, Down.

## 2. Core Observation & Invariant
Precompute 4 DP tables: L[r][c] = (grid[r][c] == '#' ? 0 : L[r][c-1] + 1), R[r][c] from right, U[r][c] from top, D[r][c] from bottom. Then total illuminated cells from (r, c) is L[r][c] + R[r][c] + U[r][c] + D[r][c] - 3.

## 3. Step-by-Step Algorithm
1. Compute L[r][c] scanning each row left-to-right.
2. Compute R[r][c] scanning each row right-to-left.
3. Compute U[r][c] scanning each col top-to-bottom.
4. Compute D[r][c] scanning each col bottom-to-top.
5. For each '.' cell, compute L + R + U + D - 3 and take the maximum.

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    vector<vector<int>> L(h, vector<int>(w, 0));
    vector<vector<int>> R(h, vector<int>(w, 0));
    vector<vector<int>> U(h, vector<int>(w, 0));
    vector<vector<int>> D(h, vector<int>(w, 0));

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '.') L[r][c] = (c == 0 ? 1 : L[r][c - 1] + 1);
        }
        for (int c = w - 1; c >= 0; --c) {
            if (grid[r][c] == '.') R[r][c] = (c == w - 1 ? 1 : R[r][c + 1] + 1);
        }
    }

    for (int c = 0; c < w; ++c) {
        for (int r = 0; r < h; ++r) {
            if (grid[r][c] == '.') U[r][c] = (r == 0 ? 1 : U[r - 1][c] + 1);
        }
        for (int r = h - 1; r >= 0; --r) {
            if (grid[r][c] == '.') D[r][c] = (r == h - 1 ? 1 : D[r + 1][c] + 1);
        }
    }

    int max_lit = 0;
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '.') {
                max_lit = max(max_lit, L[r][c] + R[r][c] + U[r][c] + D[r][c] - 3);
            }
        }
    }

    cout << max_lit << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 4-way contiguous segment length precomputation via dynamic programming.
- **Reusable Pattern**: `Grid ray length: L[r][c] + R[r][c] + U[r][c] + D[r][c] - 3.`
