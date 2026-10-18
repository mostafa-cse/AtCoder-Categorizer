# Problem Analysis: AtCoder-agc004_c — C. AND Grid

**Problem ID**: `AtCoder-agc004_c`  
**Contest**: `agc004`  
**Rating / Difficulty**: 2367  
**URL**: https://atcoder.jp/contests/agc004/tasks/agc004_c  
**VJudge Tag**: `[problem:AtCoder-agc004_c]`  
**Category File**: [`../categories/basics/dual_comb_grid_construction.md`](../categories/basics/dual_comb_grid_construction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Paint Red and Blue connected grids whose intersection is strictly the given purple cells. Dual interlocking comb construction: Red spans column 1 and all odd rows; Blue spans column $W$ and all even rows. Their base combs are disjoint, solved in $O(HW)$.

## 2. Core Observation & Invariant
Since purple cells are strictly internal (not on the boundary $i=1,H$ or $j=1,W$), Red and Blue can be given disjoint interlocking spanning combs: Red spans column 1 and all odd rows (excluding column $W$); Blue spans column $W$ and all even rows (excluding column 1). Red base and Blue base are completely disjoint; adding all purple cells to both ensures Red and Blue remain connected while their intersection is strictly the purple cells.

## 3. Step-by-Step Algorithm
1. Initialize Red grid: color all cells in column 1 (0-indexed 0) and all cells in odd rows (0-indexed even) except the last column.
2. Initialize Blue grid: color all cells in column $W$ (0-indexed $W-1$) and all cells in even rows (0-indexed odd) except the first column.
3. Color every purple cell `#` in both Red and Blue grids.
4. Output both grids in $O(HW)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(HW)`
- **Space Complexity**: `O(HW)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;
    vector<string> grid(h);
    for (int i = 0; i < h; i++) cin >> grid[i];

    vector<string> red(h, string(w, '.'));
    vector<string> blue(h, string(w, '.'));

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            // Red base: column 0 and odd rows (0-indexed: i % 2 == 0) except last column
            if (j == 0 || (i % 2 == 0 && j < w - 1) || grid[i][j] == '#') {
                red[i][j] = '#';
            }
            // Blue base: column w-1 and even rows (0-indexed: i % 2 == 1) except first column
            if (j == w - 1 || (i % 2 == 1 && j > 0) || grid[i][j] == '#') {
                blue[i][j] = '#';
            }
        }
    }

    for (int i = 0; i < h; i++) cout << red[i] << "\n";
    cout << "\n";
    for (int i = 0; i < h; i++) cout << blue[i] << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
