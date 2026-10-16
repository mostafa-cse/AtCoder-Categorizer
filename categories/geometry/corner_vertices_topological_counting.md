# Corner Vertices 2x2 Topological Counting on Grids

**Domain**: `Geometry`  
**Subtopic**: `Topological Grids`  

This workbook contains curated, high-quality competitive programming problems teaching **Corner Vertices 2x2 Topological Counting on Grids**.

---

## Curated Problems

### [problem:AtCoder-abc191_c] — Digital Graffiti
- **Contest**: `abc191`
- **Rating / Difficulty**: 1063
- **Specific Skill**: Corner Vertices 2x2 Topological Counting on Grids
- **Individual Analysis**: [`../../analysis/AtCoder-abc191_c.md`](../../analysis/AtCoder-abc191_c.md)
- **Problem Statement Summary**: An H x W grid has '#' forming a single non-self-intersecting polygon. Find the number of sides (or vertices) of this polygon.
- **Core Insight**: Every 2x2 square of cells shares exactly one central grid corner. Inspect each 2x2 window: if it contains exactly 1 black cell, it is a 90-degree corner. If it contains exactly 3 black cells, it is a 270-degree inner corner. If it contains 0, 2, or 4 black cells, the boundary passes straight through or doesn't touch the corner. Therefore, the corner count equals the number of 2x2 blocks with 1 or 3 black cells!
- **Complexity**: Time: `O(H * W)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

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

    int corners = 0;
    for (int r = 0; r < h - 1; ++r) {
        for (int c = 0; c < w - 1; ++c) {
            int black_count = 0;
            if (grid[r][c] == '#') black_count++;
            if (grid[r + 1][c] == '#') black_count++;
            if (grid[r][c + 1] == '#') black_count++;
            if (grid[r + 1][c + 1] == '#') black_count++;

            if (black_count == 1 || black_count == 3) {
                corners++;
            }
        }
    }

    cout << corners << "\n";
    return 0;
}
```
