# Problem Analysis: AtCoder-abc099_d — Good Grid

**Problem ID**: `AtCoder-abc099_d`  
**Contest**: `abc099`  
**Rating / Difficulty**: 1345  
**URL**: https://atcoder.jp/contests/abc099/tasks/abc099_d  
**VJudge Tag**: `[problem:AtCoder-abc099_d]`  
**Category File**: [`../categories/basics/grid_mod3_coloring_permutations.md`](../categories/basics/grid_mod3_coloring_permutations.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Complete Search`  
- **Topic (Skill)**: `Grid (i + j) % 3 Coloring with Color Permutations`  

---

## 1. Problem Statement & Key Idea
An N x N grid with C colors. A grid is 'good' if all cells with the same (r + c) % 3 have the same color, and different remainder classes have different colors. Cost to change color x to y is D_{x, y}. Minimize total cost (C <= 30).

**Key Idea**: The grid is partitioned into exactly 3 equivalence classes by (r + c) % 3.

## 2. Core Observation & Invariant
Precompute cost[rem][col]: the total cost to repaint all cells with (r + c) % 3 == rem to color col. Then iterate over all P(C, 3) = C * (C - 1) * (C - 2) distinct triplets of colors (c0, c1, c2) assigned to remainders 0, 1, 2. For C = 30, 30 * 29 * 28 = 24,360 operations.

## 3. Step-by-Step Algorithm
1. Initialize cost[3][C + 1] to 0.
2. For each cell (r, c) with current color cur: let rem = (r + c) % 3; for each target color col in 1..C: cost[rem][col] += D[cur][col].
3. Initialize min_cost = INF.
4. Iterate distinct colors c0, c1, c2 in 1..C: min_cost = min(min_cost, cost[0][c0] + cost[1][c1] + cost[2][c2]).
5. Print min_cost.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * C + C^3)`
- **Space Complexity**: `O(C^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, C;
    if (!(cin >> n >> C)) return 0;

    vector<vector<int>> d(C + 1, vector<int>(C + 1));
    for (int i = 1; i <= C; ++i) {
        for (int j = 1; j <= C; ++j) {
            cin >> d[i][j];
        }
    }

    vector<vector<long long>> cost(3, vector<long long>(C + 1, 0));

    for (int r = 1; r <= n; ++r) {
        for (int c = 1; c <= n; ++c) {
            int cur_col;
            cin >> cur_col;
            int rem = (r + c) % 3;
            for (int target = 1; target <= C; ++target) {
                cost[rem][target] += d[cur_col][target];
            }
        }
    }

    long long ans = INF;

    for (int c0 = 1; c0 <= C; ++c0) {
        for (int c1 = 1; c1 <= C; ++c1) {
            if (c1 == c0) continue;
            for (int c2 = 1; c2 <= C; ++c2) {
                if (c2 == c0 || c2 == c1) continue;
                long long cur = cost[0][c0] + cost[1][c1] + cost[2][c2];
                ans = min(ans, cur);
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Partitioning 2D grid constraints into remainder classes and assigning distinct colors via permutation search.
- **Reusable Pattern**: `Grid mod 3 coloring: precalculate cost[rem][col], brute force 3 distinct colors.`
