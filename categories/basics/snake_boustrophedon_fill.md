# Snake / Boustrophedon Connected Fill

**Domain**: `Basics`  
**Subtopic**: `Grid Traversal`  

This workbook contains curated, high-quality competitive programming problems teaching **Snake / Boustrophedon Connected Fill**.

---

## Curated Problems

### [problem:AtCoder-arc080_b] — Grid Coloring
- **Contest**: `abc069`
- **Rating / Difficulty**: 852
- **Specific Skill**: Snake / Boustrophedon Connected Fill
- **Individual Analysis**: [`../../analysis/AtCoder-arc080_b.md`](../../analysis/AtCoder-arc080_b.md)
- **Problem Statement Summary**: Given an H x W grid and N colors, where color i must be used exactly a_i times (sum a_i = H * W). Paint each cell such that the cells of each color form a single 4-directionally connected component.
- **Core Insight**: Boustrophedon (snake-like) traversal: visit even rows left-to-right (0 to W-1) and odd rows right-to-left (W-1 down to 0). This creates a simple continuous path through all H * W cells.
- **Complexity**: Time: `O(H * W)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n;
    if (!(cin >> h >> w >> n)) return 0;

    vector<int> a(n);
    vector<int> stream;
    stream.reserve(h * w);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        for (int k = 0; k < a[i]; ++k) {
            stream.push_back(i + 1);
        }
    }

    vector<vector<int>> grid(h, vector<int>(w));
    int idx = 0;

    for (int r = 0; r < h; ++r) {
        if (r % 2 == 0) {
            for (int c = 0; c < w; ++c) {
                grid[r][c] = stream[idx++];
            }
        } else {
            for (int c = w - 1; c >= 0; --c) {
                grid[r][c] = stream[idx++];
            }
        }
    }

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            cout << grid[r][c] << (c + 1 == w ? '\n' : ' ');
        }
    }

    return 0;
}
```
