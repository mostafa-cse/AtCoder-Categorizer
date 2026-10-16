# Problem Analysis: AtCoder-typical90_bk — Monochromatic Subgrid

**Problem ID**: `AtCoder-typical90_bk`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 063)  
**Rating / Difficulty**: 1250 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_bk  
**VJudge Tag**: `[problem:AtCoder-typical90_bk]`  
**Category File**: [`../categories/basics/subgrid_bitmask.md`](../categories/basics/subgrid_bitmask.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitmask Enumeration & Pruning`  
- **Topic (Skill)**: `Subgrid Dimension Reduction / Row Bitmask with Column Frequency Counting`  

---

## 1. Problem Statement & Key Idea
H x W grid (H <= 8, W <= 10^4). Select a subset of rows and columns such that all cells in the subgrid have the same integer. Maximize the number of cells in the subgrid.

**Core Idea**: H <= 8 is tiny! Enumerate all 2^H - 1 non-empty subsets of rows using bitmasks, then greedily aggregate columns in O(W).

## 2. Core Observation & Invariant
For a fixed subset of rows, column c is valid iff all chosen rows have identical value V = grid[r_first][c]. Count frequencies of valid values across all W columns; the max frequency gives the optimal column subset for this row mask.

## 3. Step-by-Step Algorithm
1. Loop mask from 1 to 2^H - 1.
2. For each column c: check if all rows in mask have same value V. If so, freq[V]++.
3. Max cells = popcount(mask) * max(freq.values()).
4. Return maximum over all 2^H - 1 masks.

## 4. Complexity Analysis
Time: O(2^H * H * W), Space: O(H * W).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<vector<int>> p(h, vector<int>(w));
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) cin >> p[i][j];
    }

    int max_cells = 0;
    int total_masks = 1 << h;

    for (int mask = 1; mask < total_masks; ++mask) {
        int row_count = __builtin_popcount(mask);
        map<int, int> freq;

        for (int c = 0; c < w; ++c) {
            int val = -1;
            bool ok = true;
            for (int r = 0; r < h; ++r) {
                if (mask & (1 << r)) {
                    if (val == -1) val = p[r][c];
                    else if (val != p[r][c]) {
                        ok = false;
                        break;
                    }
                }
            }
            if (ok && val != -1) {
                freq[val]++;
            }
        }

        for (auto [val, cnt] : freq) {
            max_cells = max(max_cells, row_count * cnt);
        }
    }

    cout << max_cells << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Row bitmask brute force with linear column frequency counting.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Exploiting asymmetric dimensions (H <= 8 vs W <= 10^4) via bitmask state reduction.
- **Reusable Pattern**: `Asymmetric Dimension Reduction via Bitmask.`

---
Back to [Subgrid Dimension Reduction / Row Bitmask with Column Frequency Counting](../categories/basics/subgrid_bitmask.md) | [Categories Directory](../categories/README.md)