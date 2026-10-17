# Problem Analysis: AtCoder-agc015_c — Nuske vs Phantom Thnook

**Problem ID**: `AtCoder-agc015_c`  
**Contest**: `agc015`  
**Rating / Difficulty**: 2241  
**URL**: https://atcoder.jp/contests/agc015/tasks/agc015_c  
**VJudge Tag**: `[problem:AtCoder-agc015_c]`  
**Category File**: [`../categories/basics/2d_prefix_sum_grid_forest_connected_components.md`](../categories/basics/2d_prefix_sum_grid_forest_connected_components.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `2D Prefix Sum`  
- **Topic (Skill)**: `2D Prefix Sum`  

---

## 1. Problem Statement & Key Idea
Answer Q queries counting connected components of blue cells in arbitrary subgrids of an N x M grid where blue cells form an induced forest.

## 2. Core Observation & Invariant
The problem states that between any two blue cells there is at most one simple path, meaning the blue cells form an induced forest. In any forest graph, the number of connected components equals V - E, where V is the number of vertices and E is the number of edges. Any induced subgraph of a forest is also a forest. Thus, in any query rectangle [x1, x2] x [y1, y2], Components = V - (E_horizontal + E_vertical). All three quantities are rectangle sum queries on static binary grids, computable in O(1) using 2D prefix sums.

## 3. Step-by-Step Algorithm
1. 1. Precompute 2D prefix sums for blue cell counts: prefV[i][j].
2. 2. Precompute 2D prefix sums for horizontal blue edges: prefH[i][j] where grid[i][j] == grid[i][j+1] == 1.
3. 3. Precompute 2D prefix sums for vertical blue edges: prefD[i][j] where grid[i][j] == grid[i+1][j] == 1.
4. 4. For each query (r1, c1, r2, c2):
5.    - V = query(prefV, r1, c1, r2, c2)
6.    - Eh = query(prefH, r1, c1, r2, c2 - 1)
7.    - Ev = query(prefD, r1, c1, r2 - 1, c2)
8.    - Output V - Eh - Ev.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M + Q)`
- **Space Complexity**: `O(N * M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<string> s(n);
    for (int i = 0; i < n; ++i) {
        cin >> s[i];
    }

    // 2D prefix sums for:
    // prefV: count of blue cells (1s)
    // prefH: count of horizontal edges (s[i][j]=='1' && s[i][j+1]=='1')
    // prefD: count of vertical edges (s[i][j]=='1' && s[i+1][j]=='1')
    vector<vector<int>> prefV(n + 1, vector<int>(m + 1, 0));
    vector<vector<int>> prefH(n + 1, vector<int>(m + 1, 0));
    vector<vector<int>> prefD(n + 1, vector<int>(m + 1, 0));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int is_blue = (s[i][j] == '1');
            prefV[i + 1][j + 1] = is_blue + prefV[i][j + 1] + prefV[i + 1][j] - prefV[i][j];

            int has_h = (j + 1 < m && s[i][j] == '1' && s[i][j + 1] == '1');
            prefH[i + 1][j + 1] = has_h + prefH[i][j + 1] + prefH[i + 1][j] - prefH[i][j];

            int has_d = (i + 1 < n && s[i][j] == '1' && s[i + 1][j] == '1');
            prefD[i + 1][j + 1] = has_d + prefD[i][j + 1] + prefD[i + 1][j] - prefD[i][j];
        }
    }

    auto query_2d = [](const vector<vector<int>>& pref, int r1, int c1, int r2, int c2) -> int {
        if (r1 > r2 || c1 > c2) return 0;
        return pref[r2][c2] - pref[r1 - 1][c2] - pref[r2][c1 - 1] + pref[r1 - 1][c1 - 1];
    };

    while (q--) {
        int r1, c1, r2, c2;
        cin >> r1 >> c1 >> r2 >> c2;

        int V = query_2d(prefV, r1, c1, r2, c2);
        int Eh = query_2d(prefH, r1, c1, r2, c2 - 1);
        int Ev = query_2d(prefD, r1, c1, r2 - 1, c2);

        int ans = V - (Eh + Ev);
        cout << ans << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
