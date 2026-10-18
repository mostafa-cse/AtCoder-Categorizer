# Problem Analysis: AtCoder-arc081_d — F. Flip and Rectangles

**Problem ID**: `AtCoder-arc081_d`  
**Contest**: `arc081`  
**Rating / Difficulty**: 2608  
**URL**: https://atcoder.jp/contests/arc081/tasks/arc081_d  
**VJudge Tag**: `[problem:AtCoder-arc081_d]`  
**Category File**: [`../categories/data_structures_ds/flip_and_rectangles_monotonic_stack.md`](../categories/data_structures_ds/flip_and_rectangles_monotonic_stack.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Monotonic Data Structures`  
- **Topic (Skill)**: `Monotonic Stack: All Nearest Smaller Values and All Subarray Maximum/Minimum`  

---

## 1. Problem Statement & Key Idea
Given an H x W grid of black and white squares, you can invert any row or column. Find the maximum area of a subgrid that can be made entirely black.

## 2. Core Observation & Invariant
Inverting a row or column preserves the XOR parity of '#' squares in every 2x2 subgrid. A subgrid can be made all black iff every 2x2 block in it has even parity. A rectangle of a x b valid 2x2 blocks corresponds to an original subgrid of area (a + 1)(b + 1).

## 3. Step-by-Step Algorithm
1. Create an (H-1) x (W-1) binary matrix B where B[i][j] = 1 iff the 2x2 block at (i, j) has even parity.
2. Compute the largest rectangle of 1s in B using a monotonic stack on histogram heights, maximizing (h + 1)(w + 1). Base answer is max(H, W).

## 4. Complexity Analysis
- **Time Complexity**: `O(HW)`
- **Space Complexity**: `O(HW)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<string> grid(H);
    for (int i = 0; i < H; ++i) {
        cin >> grid[i];
    }

    int ans = max(H, W);
    if (H < 2 || W < 2) {
        cout << ans << "\n";
        return 0;
    }

    vector<vector<int>> B(H - 1, vector<int>(W - 1, 0));
    for (int i = 0; i < H - 1; ++i) {
        for (int j = 0; j < W - 1; ++j) {
            int cnt = (grid[i][j] == '#' ? 1 : 0) +
                      (grid[i][j + 1] == '#' ? 1 : 0) +
                      (grid[i + 1][j] == '#' ? 1 : 0) +
                      (grid[i + 1][j + 1] == '#' ? 1 : 0);
            B[i][j] = (cnt % 2 == 0) ? 1 : 0;
        }
    }

    vector<int> h(W - 1, 0);
    for (int i = 0; i < H - 1; ++i) {
        for (int j = 0; j < W - 1; ++j) {
            if (B[i][j] == 1) h[j]++;
            else h[j] = 0;
        }

        vector<pair<int, int>> stack; // (start_idx, height)
        for (int j = 0; j <= W - 1; ++j) {
            int cur_h = (j < W - 1) ? h[j] : 0;
            int start = j;
            while (!stack.empty() && stack.back().second >= cur_h) {
                int idx = stack.back().first;
                int val = stack.back().second;
                stack.pop_back();
                int width = j - idx;
                if (val > 0) {
                    ans = max(ans, (val + 1) * (width + 1));
                }
                start = idx;
            }
            stack.push_back({start, cur_h});
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
