# Problem Analysis: AtCoder-abc191_c — Digital Graffiti

**Problem ID**: `AtCoder-abc191_c`  
**Contest**: `abc191`  
**Rating / Difficulty**: 1063  
**URL**: https://atcoder.jp/contests/abc191/tasks/abc191_c  
**VJudge Tag**: `[problem:AtCoder-abc191_c]`  
**Category File**: [`../categories/geometry/corner_vertices_topological_counting.md`](../categories/geometry/corner_vertices_topological_counting.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Topological Grids`  
- **Topic (Skill)**: `Corner Vertices 2x2 Topological Counting on Grids`  

---

## 1. Problem Statement & Key Idea
An H x W grid has '#' forming a single non-self-intersecting polygon. Find the number of sides (or vertices) of this polygon.

**Key Idea**: In any polygon, the number of sides equals the number of vertices. On a grid of unit squares, polygon vertices occur only at the grid intersection points (corners).

## 2. Core Observation & Invariant
Every 2x2 square of cells shares exactly one central grid corner. Inspect each 2x2 window: if it contains exactly 1 black cell, it is a 90-degree corner. If it contains exactly 3 black cells, it is a 270-degree inner corner. If it contains 0, 2, or 4 black cells, the boundary passes straight through or doesn't touch the corner. Therefore, the corner count equals the number of 2x2 blocks with 1 or 3 black cells!

## 3. Step-by-Step Algorithm
1. Iterate r from 0 to H - 2 and c from 0 to W - 2.
2. Count black cells in the 2x2 window (r, c), (r+1, c), (r, c+1), (r+1, c+1).
3. If the count is 1 or 3, increment vertex_count.
4. Output vertex_count.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

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

    int corners = 0;
    for (int r = 0; r < h - 1; ++r) {
        for (int c = 0; c < w - 1; ++c) {
            int black_count = 0;
            if (grid[r][c] == '#') black_count++;
            if (grid[r + 1][c] == '#') black_count++;
            if (grid[r][c + 1] == '#') black_count++;
            if (grid[r + 1][c + 1] == '#') black_count++;

            if (black_count == 1 || black_count == 3) {
                corners++;
            }
        }
    }

    cout << corners << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Topological corner counting on rasterized digital polygons.
- **Reusable Pattern**: `Polygon vertices in grid = count of 2x2 windows with odd number of '#' cells (1 or 3).`
