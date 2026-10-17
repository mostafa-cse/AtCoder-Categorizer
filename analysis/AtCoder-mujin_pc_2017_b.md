# Problem Analysis: AtCoder-mujin_pc_2017_b — B. Row to Column

**Problem ID**: `AtCoder-mujin_pc_2017_b`  
**Contest**: `mujin_pc_2017`  
**Rating / Difficulty**: 2177  
**URL**: https://atcoder.jp/contests/mujin_pc_2017/tasks/mujin_pc_2017_b  
**VJudge Tag**: `[problem:AtCoder-mujin_pc_2017_b]`  
**Category File**: [`../categories/basics/row_to_column_grid_operations_state_reduction.md`](../categories/basics/row_to_column_grid_operations_state_reduction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
On an N x N grid of white/black cells, an operation copies row i into column j. Minimize operations to make all cells black. The strategy is to construct a single completely black row r, and then copy row r into every column that is not already fully black. Solved by iterating over all possible target rows r.

## 2. Core Observation & Invariant
If no cell is black initially, it is impossible (output -1). If all cells are black, 0 operations. Every column not initially full black must eventually be painted by an all-black row. To make row r all black, for each white cell (r, c) we copy a row whose r-th cell is black into column c (Z_r operations). If column r has no black cell initially, 1 extra operation seeds column r with a black cell.

## 3. Step-by-Step Algorithm
1. If no '#' exists in the grid, output -1. If every cell is '#', output 0.
2. Count the number of columns not completely black: c_nonfull.
3. For each row r from 0 to N-1, count white cells Z_r in row r.
4. Check if column r contains at least one '#'. If not, add 1 extra operation.
5. Minimum operations is c_nonfull + min_r (Z_r + (1 if column r has no black cell else 0)).

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<string> grid(N);
    bool has_any_black = false;
    bool all_black = true;
    for (int i = 0; i < N; ++i) {
        cin >> grid[i];
        for (char c : grid[i]) {
            if (c == '#') has_any_black = true;
            else all_black = false;
        }
    }

    if (!has_any_black) {
        cout << -1 << "\n";
        return 0;
    }
    if (all_black) {
        cout << 0 << "\n";
        return 0;
    }

    vector<bool> col_full(N, true);
    vector<bool> col_has_black(N, false);
    int c_nonfull = 0;

    for (int c = 0; c < N; ++c) {
        for (int r = 0; r < N; ++r) {
            if (grid[r][c] == '#') {
                col_has_black[c] = true;
            } else {
                col_full[c] = false;
            }
        }
        if (!col_full[c]) c_nonfull++;
    }

    int ans = 1e9;
    for (int r = 0; r < N; ++r) {
        int z_r = 0;
        for (int c = 0; c < N; ++c) {
            if (grid[r][c] == '.') z_r++;
        }
        int add = (!col_has_black[r] ? 1 : 0);
        ans = min(ans, c_nonfull + z_r + add);
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
