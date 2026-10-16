# 4-Directional Prefix Ray DP Precomputation

**Domain**: `Dynamic Programming`  
**Subtopic**: `Grid DP`  

This workbook contains curated, high-quality competitive programming problems teaching **4-Directional Prefix Ray DP Precomputation**.

---

## Curated Problems

### [problem:AtCoder-abc129_d] — Lamp
- **Contest**: `abc129`
- **Rating / Difficulty**: 1103
- **Specific Skill**: 4-Directional Prefix Ray DP Precomputation
- **Individual Analysis**: [`../../analysis/AtCoder-abc129_d.md`](../../analysis/AtCoder-abc129_d.md)
- **Problem Statement Summary**: An H x W grid has '.' and '#'. Place a lamp at a '.' cell to illuminate cells in 4 directions until reaching an obstacle. Maximize illuminated cells (H, W <= 2000).
- **Core Insight**: Precompute 4 DP tables: L[r][c] = (grid[r][c] == '#' ? 0 : L[r][c-1] + 1), R[r][c] from right, U[r][c] from top, D[r][c] from bottom. Then total illuminated cells from (r, c) is L[r][c] + R[r][c] + U[r][c] + D[r][c] - 3.
- **Complexity**: Time: `O(H * W)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

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

    vector<vector<int>> L(h, vector<int>(w, 0));
    vector<vector<int>> R(h, vector<int>(w, 0));
    vector<vector<int>> U(h, vector<int>(w, 0));
    vector<vector<int>> D(h, vector<int>(w, 0));

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '.') L[r][c] = (c == 0 ? 1 : L[r][c - 1] + 1);
        }
        for (int c = w - 1; c >= 0; --c) {
            if (grid[r][c] == '.') R[r][c] = (c == w - 1 ? 1 : R[r][c + 1] + 1);
        }
    }

    for (int c = 0; c < w; ++c) {
        for (int r = 0; r < h; ++r) {
            if (grid[r][c] == '.') U[r][c] = (r == 0 ? 1 : U[r - 1][c] + 1);
        }
        for (int r = h - 1; r >= 0; --r) {
            if (grid[r][c] == '.') D[r][c] = (r == h - 1 ? 1 : D[r + 1][c] + 1);
        }
    }

    int max_lit = 0;
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '.') {
                max_lit = max(max_lit, L[r][c] + R[r][c] + U[r][c] + D[r][c] - 3);
            }
        }
    }

    cout << max_lit << "\n";
    return 0;
}
```
