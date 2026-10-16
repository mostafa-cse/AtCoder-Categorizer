# Problem Analysis: AtCoder-abc182_e — Akari

**Problem ID**: `AtCoder-abc182_e`  
**Contest**: `abc182`  
**Rating / Difficulty**: 1098  
**URL**: https://atcoder.jp/contests/abc182/tasks/abc182_e  
**VJudge Tag**: `[problem:AtCoder-abc182_e]`  
**Category File**: [`../categories/basics/grid_linear_beam_propagation.md`](../categories/basics/grid_linear_beam_propagation.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Grid Ray Casting`  
- **Topic (Skill)**: `4-Way Linear Beam Propagation on Grids`  

---

## 1. Problem Statement & Key Idea
An H x W grid has N light bulbs and M blocks. Light travels from bulbs in 4 cardinal directions until blocked by a block or boundary. Count the number of illuminated cells.

**Key Idea**: Ray-casting from each bulb independently takes O(N * (H + W)), which is too slow. Instead, sweep each row and column in both directions.

## 2. Core Observation & Invariant
Sweep each row left-to-right: maintain whether a light beam is currently active. A bulb activates the beam; a block stops the beam; empty cells become illuminated. Repeat for right-to-left, top-to-bottom, and bottom-to-top. This visits every cell a constant number of times.

## 3. Step-by-Step Algorithm
1. Mark bulbs as 1 and blocks as -1 in grid.
2. Allocate lit[H][W] boolean array.
3. For each row: sweep left-to-right (activate on bulb, stop on block); sweep right-to-left.
4. For each col: sweep top-to-bottom; sweep bottom-to-top.
5. Count cells with lit[r][c] == true.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n, m;
    if (!(cin >> h >> w >> n >> m)) return 0;

    vector<vector<int>> grid(h, vector<int>(w, 0));
    for (int i = 0; i < n; ++i) {
        int r, c;
        cin >> r >> c;
        grid[r - 1][c - 1] = 1; // bulb
    }
    for (int i = 0; i < m; ++i) {
        int r, c;
        cin >> r >> c;
        grid[r - 1][c - 1] = -1; // block
    }

    vector<vector<bool>> lit(h, vector<bool>(w, false));

    // Horizontal sweeps
    for (int r = 0; r < h; ++r) {
        bool beam = false;
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == 1) beam = true;
            else if (grid[r][c] == -1) beam = false;
            if (beam) lit[r][c] = true;
        }
        beam = false;
        for (int c = w - 1; c >= 0; --c) {
            if (grid[r][c] == 1) beam = true;
            else if (grid[r][c] == -1) beam = false;
            if (beam) lit[r][c] = true;
        }
    }

    // Vertical sweeps
    for (int c = 0; c < w; ++c) {
        bool beam = false;
        for (int r = 0; r < h; ++r) {
            if (grid[r][c] == 1) beam = true;
            else if (grid[r][c] == -1) beam = false;
            if (beam) lit[r][c] = true;
        }
        beam = false;
        for (int r = h - 1; r >= 0; --r) {
            if (grid[r][c] == 1) beam = true;
            else if (grid[r][c] == -1) beam = false;
            if (beam) lit[r][c] = true;
        }
    }

    int count = 0;
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (lit[r][c]) count++;
        }
    }

    cout << count << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Full-grid ray propagation via 4-pass directional sweeping.
- **Reusable Pattern**: `4-pass grid beam: sweep rows L->R and R->L, sweep cols T->B and B->T.`
