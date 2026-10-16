# Problem Analysis: AtCoder-typical90_bt — Loop Railway Plan

**Problem ID**: `AtCoder-typical90_bt`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 072)  
**Rating / Difficulty**: 1350 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bt  
**VJudge Tag**: `[problem:AtCoder-typical90_bt]`  
**Category File**: [`../categories/basics/grid_cycle_backtracking.md`](../categories/basics/grid_cycle_backtracking.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Backtracking & Recursion`  
- **Topic (Skill)**: `Grid Simple Cycle Search via DFS Backtracking (Small N <= 16)`  

---

## 1. Problem Statement & Key Idea
H x W grid with empty cells '.' and walls '#' (H, W <= 16, H*W <= 16). Find a simple cycle of length >= 3 traversing only empty cells that maximizes cycle length, or -1 if no cycle exists.

**Core Idea**: H*W <= 16 is small enough for exhaustive simple cycle search with DFS backtracking.

## 2. Core Observation & Invariant
Iterate each non-wall cell as the cycle start (r0, c0). Run DFS marking visited cells. When reaching an adjacent neighbor that equals (r0, c0) with step >= 3, update max cycle length.

## 3. Step-by-Step Algorithm
1. For each cell (r, c): DFS(r, c, r0, c0, step).
2. If neighbor == (r0, c0) and step >= 3: max_cycle = max(max_cycle, step).
3. If neighbor unvisited and not wall: mark visited, DFS(nr, nc, r0, c0, step + 1), unmark visited.
4. Output max_cycle or -1.

## 4. Complexity Analysis
Time: O(4^(HW)), extremely fast for HW <= 16 (< 0.02s), Space: O(HW).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int h, w;
vector<string> grid;
bool vis[20][20];
int max_len = -1;

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

void dfs(int r, int c, int start_r, int start_c, int step) {
    for (int k = 0; k < 4; ++k) {
        int nr = r + dr[k], nc = c + dc[k];
        if (nr < 0 || nr >= h || nc < 0 || nc >= w || grid[nr][nc] == '#') continue;

        if (nr == start_r && nc == start_c && step >= 3) {
            max_len = max(max_len, step);
            continue;
        }

        if (!vis[nr][nc]) {
            vis[nr][nc] = true;
            dfs(nr, nc, start_r, start_c, step + 1);
            vis[nr][nc] = false;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> h >> w)) return 0;
    grid.resize(h);
    for (int i = 0; i < h; ++i) cin >> grid[i];

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '.') {
                vis[r][c] = true;
                dfs(r, c, r, c, 1);
                vis[r][c] = false;
            }
        }
    }

    cout << max_len << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
DFS backtracking cycle search on small bounded grid.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Grid cycle finding, backtracking state restoration, and constraint-based pruning.
- **Reusable Pattern**: `Grid Cycle Backtracking DFS.`

---
Back to [Grid Simple Cycle Search via DFS Backtracking (Small N <= 16)](../categories/basics/grid_cycle_backtracking.md) | [Categories Directory](../categories/README.md)