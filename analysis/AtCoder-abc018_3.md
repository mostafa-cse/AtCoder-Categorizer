# Problem Analysis: AtCoder-abc018_3 — Diamond Count

**Problem ID**: `AtCoder-abc018_3`  
**Contest**: `abc018`  
**Rating / Difficulty**: 1553  
**URL**: https://atcoder.jp/contests/abc018/tasks/abc018_3  
**VJudge Tag**: `[problem:AtCoder-abc018_3]`  
**Category File**: [`../categories/dp/diamond_pattern_vertical_runs.md`](../categories/dp/diamond_pattern_vertical_runs.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `2D Grid DP`  
- **Topic (Skill)**: `2D Vertical Consecutive Run Prefix Sums for Diamond Pattern Matching`  

---

## 1. Problem Statement & Key Idea
An R x C grid of 'o' and 'x'. Count center cells (r, c) such that a diamond (Manhattan circle) of radius K centered at (r, c) consists entirely of 'o'.

**Key Insight**: For cell (r, c) to be a diamond center, for each column offset dx in [-(K-1), K-1], the vertical continuous span of 'o's above and below (r, c+dx) must be at least K - 1 - |dx|.

## 2. Core Observation & Invariant
Precompute up[r][c] (number of consecutive 'o's above (r, c)) and down[r][c] (consecutive 'o's below (r, c)) in O(R * C). Then test each potential center (r, c) by checking the 2K - 1 columns in O(K).

## 3. Step-by-Step Algorithm
1. Compute up[r][c] = (grid[r][c] == 'o' ? up[r-1][c] + 1 : 0).
2. Compute down[r][c] = (grid[r][c] == 'o' ? down[r+1][c] + 1 : 0).
3. valid_centers = 0.
4. For r from K to R - K + 1:
5.   For c from K to C - K + 1:
6.     valid = true.
7.     For dx from -(K - 1) to K - 1:
8.       req = K - 1 - abs(dx);
9.       if (up[r][c + dx] <= req || down[r][c + dx] <= req) { valid = false; break; }
10.     If valid: valid_centers++.
11. Print valid_centers.

## 4. Complexity Analysis
- **Time Complexity**: `O(R * C * K)`
- **Space Complexity**: `O(R * C)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, K;
    if (!(cin >> R >> C >> K)) return 0;

    vector<string> grid(R + 1);
    for (int r = 1; r <= R; ++r) {
        cin >> grid[r];
        grid[r] = " " + grid[r];
    }

    vector<vector<int>> up(R + 2, vector<int>(C + 2, 0));
    vector<vector<int>> down(R + 2, vector<int>(C + 2, 0));

    for (int c = 1; c <= C; ++c) {
        for (int r = 1; r <= R; ++r) {
            up[r][c] = (grid[r][c] == 'o' ? up[r - 1][c] + 1 : 0);
        }
        for (int r = R; r >= 1; --r) {
            down[r][c] = (grid[r][c] == 'o' ? down[r + 1][c] + 1 : 0);
        }
    }

    int count = 0;
    for (int r = K; r <= R - K + 1; ++r) {
        for (int c = K; c <= C - K + 1; ++c) {
            bool ok = true;
            for (int dx = -(K - 1); dx <= K - 1; ++dx) {
                int req = K - 1 - abs(dx);
                if (up[r][c + dx] <= req || down[r][c + dx] <= req) {
                    ok = false;
                    break;
                }
            }
            if (ok) count++;
        }
    }

    cout << count << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Vertical consecutive span precomputation for fast geometric shape validation on grids.
- **Reusable Pattern**: `Manhattan Diamond Validation: up/down runs >= K - 1 - |dx| across horizontal window.`
