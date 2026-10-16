# 4-Way Linear Beam Propagation on Grids

**Domain**: `Basics`  
**Subtopic**: `Grid Ray Casting`  

This workbook contains curated, high-quality competitive programming problems teaching **4-Way Linear Beam Propagation on Grids**.

---

## Curated Problems

### [problem:AtCoder-abc182_e] — Akari
- **Contest**: `abc182`
- **Rating / Difficulty**: 1098
- **Specific Skill**: 4-Way Linear Beam Propagation on Grids
- **Individual Analysis**: [`../../analysis/AtCoder-abc182_e.md`](../../analysis/AtCoder-abc182_e.md)
- **Problem Statement Summary**: An H x W grid has N light bulbs and M blocks. Light travels from bulbs in 4 cardinal directions until blocked by a block or boundary. Count the number of illuminated cells.
- **Core Insight**: Sweep each row left-to-right: maintain whether a light beam is currently active. A bulb activates the beam; a block stops the beam; empty cells become illuminated. Repeat for right-to-left, top-to-bottom, and bottom-to-top. This visits every cell a constant number of times.
- **Complexity**: Time: `O(H * W)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n, m;
    if (!(cin >> h >> w >> n >> m)) return 0;

    vector<vector<int>> grid(h, vector<int>(w, 0));
    for (int i = 0; i < n; ++i) {
        int r, c;
        cin >> r >> c;
        grid[r - 1][c - 1] = 1; // bulb
    }
    for (int i = 0; i < m; ++i) {
        int r, c;
        cin >> r >> c;
        grid[r - 1][c - 1] = -1; // block
    }

    vector<vector<bool>> lit(h, vector<bool>(w, false));

    // Horizontal sweeps
    for (int r = 0; r < h; ++r) {
        bool beam = false;
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == 1) beam = true;
            else if (grid[r][c] == -1) beam = false;
            if (beam) lit[r][c] = true;
        }
        beam = false;
        for (int c = w - 1; c >= 0; --c) {
            if (grid[r][c] == 1) beam = true;
            else if (grid[r][c] == -1) beam = false;
            if (beam) lit[r][c] = true;
        }
    }

    // Vertical sweeps
    for (int c = 0; c < w; ++c) {
        bool beam = false;
        for (int r = 0; r < h; ++r) {
            if (grid[r][c] == 1) beam = true;
            else if (grid[r][c] == -1) beam = false;
            if (beam) lit[r][c] = true;
        }
        beam = false;
        for (int r = h - 1; r >= 0; --r) {
            if (grid[r][c] == 1) beam = true;
            else if (grid[r][c] == -1) beam = false;
            if (beam) lit[r][c] = true;
        }
    }

    int count = 0;
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (lit[r][c]) count++;
        }
    }

    cout << count << "\n";
    return 0;
}
```
