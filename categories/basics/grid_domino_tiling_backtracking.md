# Grid Domino Tiling Backtracking DFS

**Domain**: `Basics`  
**Subtopic**: `Backtracking`  

This workbook contains curated, high-quality competitive programming problems teaching **Grid Domino Tiling Backtracking DFS**.

---

## Curated Problems

### [problem:AtCoder-abc196_d] — Hanjo
- **Contest**: `abc196`
- **Rating / Difficulty**: 1277
- **Specific Skill**: Grid Domino Tiling Backtracking DFS
- **Individual Analysis**: [`../../analysis/AtCoder-abc196_d.md`](../../analysis/AtCoder-abc196_d.md)
- **Problem Statement Summary**: An H x W room. Tile with A tatami mats of size 2x1 and B mats of size 1x1 such that 2A + B = H * W (H * W <= 16). Find the number of valid tilings.
- **Core Insight**: Visit cells in row-major order: index k from 0 to H*W - 1 (r = k / W, c = k % W). If cell (r, c) is already covered, advance to k + 1. Otherwise, we can: (1) place a 1x1 mat if B > 0; (2) place a 2x1 horizontal mat if c + 1 < W and cell (r, c+1) is empty and A > 0; (3) place a 1x2 vertical mat if r + 1 < H and cell (r+1, c) is empty and A > 0.
- **Complexity**: Time: `O(3^(HW/2))` | Space: `O(HW)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>

using namespace std;

int h, w, a_mats, b_mats;

long long dfs(int k, int a, int b, int mask) {
    if (k == h * w) {
        return (a == 0 && b == 0 ? 1 : 0);
    }
    if ((mask >> k) & 1) {
        return dfs(k + 1, a, b, mask);
    }

    int r = k / w;
    int c = k % w;
    long long ways = 0;

    // Place 1x1 mat
    if (b > 0) {
        ways += dfs(k + 1, a, b - 1, mask | (1 << k));
    }

    // Place 1x2 horizontal mat
    if (a > 0 && c + 1 < w && !((mask >> (k + 1)) & 1)) {
        ways += dfs(k + 1, a - 1, b, mask | (1 << k) | (1 << (k + 1)));
    }

    // Place 2x1 vertical mat
    if (a > 0 && r + 1 < h && !((mask >> (k + w)) & 1)) {
        ways += dfs(k + 1, a - 1, b, mask | (1 << k) | (1 << (k + w)));
    }

    return ways;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> h >> w >> a_mats >> b_mats)) return 0;

    cout << dfs(0, a_mats, b_mats, 0) << "\n";
    return 0;
}
```
