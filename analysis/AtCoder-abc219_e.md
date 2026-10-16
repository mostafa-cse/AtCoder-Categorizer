# Problem Analysis: AtCoder-abc219_e — Moat

**Problem ID**: `AtCoder-abc219_e`  
**Contest**: `abc219`  
**Rating / Difficulty**: 1690  
**URL**: https://atcoder.jp/contests/abc219/tasks/abc219_e  
**VJudge Tag**: `[problem:AtCoder-abc219_e]`  
**Category File**: [`../categories/basics/bitmask_grid_shape_topology.md`](../categories/basics/bitmask_grid_shape_topology.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Bitmask Search`  
- **Topic (Skill)**: `Bitmask Grid Shapes with Connectivity (DSU) and Hole-Free (Outer BFS) Checking`  

---

## 1. Problem Statement & Key Idea
A 4x4 grid. Some cells contain houses (A[i][j] == 1). Build a moat around a set of cells S such that: 1) S contains all houses; 2) S forms a single 4-connected component; 3) The boundary of S is a simple polygon (S has no internal holes / lakes). Count valid sets S.

**Key Insight**: The grid has only 16 cells, meaning 2^16 = 65,536 subsets! Enumerate all subsets mask and check: 1) mask has all houses; 2) moat cells form 1 connected component; 3) outer white cells (padded to 6x6) form 1 connected component (guaranteeing no holes).

## 2. Core Observation & Invariant
A shape has no internal holes iff its complement is connected to the outer boundary! Pad the 4x4 grid with an outer ring to 6x6. Flood-fill from (0, 0) through all non-moat cells: if the count of reachable non-moat cells equals 36 - popcount(mask), there are no interior holes.

## 3. Step-by-Step Algorithm
1. Check that mask covers all cells with A[i][j] == 1.
2. Moat connectivity: count connected components among 1s in mask using BFS/DSU; must equal 1.
3. Hole-free test: create 6x6 grid, place moat in rows 1..4, cols 1..4.
4. Flood fill (BFS) from (0, 0) over all cells not in moat.
5. If flooded cell count == 36 - popcount(mask), increment valid_count.
6. Print valid_count.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^16 * 36)`
- **Space Complexity**: `O(36)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int dr[4] = {-1, 1, 0, 0};
const int dc[4] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int house_mask = 0;
    for (int r = 0; r < 4; ++r) {
        for (int c = 0; c < 4; ++c) {
            int val;
            if (cin >> val && val == 1) {
                house_mask |= (1 << (r * 4 + c));
            }
        }
    }

    int total_masks = 1 << 16;
    int ans = 0;

    for (int mask = 1; mask < total_masks; ++mask) {
        // Condition 1: Contains all houses
        if ((mask & house_mask) != house_mask) continue;

        // Condition 2: Moat is connected
        int start_cell = __builtin_ctz(mask);
        int visited_moat = 0;
        queue<int> q;
        q.push(start_cell);
        visited_moat |= (1 << start_cell);

        while (!q.empty()) {
            int cell = q.front();
            q.pop();
            int r = cell / 4, c = cell % 4;
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < 4 && nc >= 0 && nc < 4) {
                    int ncell = nr * 4 + nc;
                    if ((mask & (1 << ncell)) && !(visited_moat & (1 << ncell))) {
                        visited_moat |= (1 << ncell);
                        q.push(ncell);
                    }
                }
            }
        }

        if (visited_moat != mask) continue;

        // Condition 3: No holes (outer complement is connected on 6x6 grid)
        vector<vector<bool>> is_moat(6, vector<bool>(6, false));
        for (int r = 0; r < 4; ++r) {
            for (int c = 0; c < 4; ++c) {
                if (mask & (1 << (r * 4 + c))) {
                    is_moat[r + 1][c + 1] = true;
                }
            }
        }

        vector<vector<bool>> vis_outer(6, vector<bool>(6, false));
        queue<pair<int, int>> q_out;
        q_out.push({0, 0});
        vis_outer[0][0] = true;
        int outer_reach = 0;

        while (!q_out.empty()) {
            auto [r, c] = q_out.front();
            q_out.pop();
            outer_reach++;

            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < 6 && nc >= 0 && nc < 6) {
                    if (!is_moat[nr][nc] && !vis_outer[nr][nc]) {
                        vis_outer[nr][nc] = true;
                        q_out.push({nr, nc});
                    }
                }
            }
        }

        if (outer_reach == 36 - __builtin_popcount(mask)) {
            ans++;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Topological shape validation (connectivity + hole-free simple boundary) via bitmask enumeration and flood-fill.
- **Reusable Pattern**: `Simple Polygon Grid Moat: check mask connectivity + complement flood fill from outer border.`
