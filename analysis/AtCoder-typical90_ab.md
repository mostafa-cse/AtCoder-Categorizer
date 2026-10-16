# Problem Analysis: AtCoder-typical90_ab — Cluttered Paper

**Problem ID**: `AtCoder-typical90_ab`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 028)  
**Rating / Difficulty**: 1300 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ab  
**VJudge Tag**: `[problem:AtCoder-typical90_ab]`  
**Category File**: [`../categories/data_structures/difference_arrays_imos.md`](../categories/data_structures/difference_arrays_imos.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Prefix Sums & Difference Arrays`  
- **Topic (Skill)**: `2D Imos Method / 2D Difference Array`  

---

## 1. Problem Statement & Key Idea
N axis-aligned sheets of paper are placed on a 1000 x 1000 grid. Each rectangle covers [lx, rx) x [ly, ry). For each k from 1 to N, calculate the total area covered by exactly k sheets.

**Core Idea**: Use 2D difference arrays (2D Imos method) to perform O(1) rectangle range additions.

## 2. Core Observation & Invariant
For each rectangle [lx, rx) x [ly, ry), add +1 at (lx, ly) and (rx, ry), and -1 at (lx, ry) and (rx, ly). A 2D prefix sum over rows and columns reconstructs all cell coverage counts in O(W^2).

## 3. Step-by-Step Algorithm
1. Initialize D[1005][1005] = 0.
2. For each rectangle: D[lx][ly]++; D[rx][ry]++; D[lx][ry]--; D[rx][ly]--;
3. Prefix sum rows: D[x][y] += D[x-1][y].
4. Prefix sum cols: D[x][y] += D[x][y-1].
5. Count frequency of each k in 1..N and output.

## 4. Complexity Analysis
Time: O(N + W^2), Space: O(W^2) where W = 1000.

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 1001;
int diff[MAX + 1][MAX + 1];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    for (int i = 0; i < n; ++i) {
        int lx, ly, rx, ry;
        cin >> lx >> ly >> rx >> ry;
        diff[lx][ly]++;
        diff[rx][ry]++;
        diff[lx][ry]--;
        diff[rx][ly]--;
    }

    // 2D Prefix Sums
    for (int x = 0; x <= MAX; ++x) {
        for (int y = 1; y <= MAX; ++y) {
            diff[x][y] += diff[x][y - 1];
        }
    }
    for (int y = 0; y <= MAX; ++y) {
        for (int x = 1; x <= MAX; ++x) {
            diff[x][y] += diff[x - 1][y];
        }
    }

    vector<int> ans(n + 1, 0);
    for (int x = 0; x < MAX; ++x) {
        for (int y = 0; y < MAX; ++y) {
            int k = diff[x][y];
            if (k >= 1 && k <= n) {
                ans[k]++;
            }
        }
    }

    for (int k = 1; k <= n; ++k) {
        cout << ans[k] << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
2D Imos method for cumulative 2D rectangle additions.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 2D Difference arrays (Imos method), 2D prefix accumulation, and O(1) rectangle range updates.
- **Reusable Pattern**: `2D Imos Difference Array.`

---
Back to [2D Imos Method / 2D Difference Array](../categories/data_structures/difference_arrays_imos.md) | [Categories Directory](../categories/README.md)