# Grid (i + j) % 3 Coloring with Color Permutations

**Domain**: `Basics`  
**Subtopic**: `Complete Search`  

This workbook contains curated, high-quality competitive programming problems teaching **Grid (i + j) % 3 Coloring with Color Permutations**.

---

## Curated Problems

### [problem:AtCoder-abc099_d] — Good Grid
- **Contest**: `abc099`
- **Rating / Difficulty**: 1345
- **Specific Skill**: Grid (i + j) % 3 Coloring with Color Permutations
- **Individual Analysis**: [`../../analysis/AtCoder-abc099_d.md`](../../analysis/AtCoder-abc099_d.md)
- **Problem Statement Summary**: An N x N grid with C colors. A grid is 'good' if all cells with the same (r + c) % 3 have the same color, and different remainder classes have different colors. Cost to change color x to y is D_{x, y}. Minimize total cost (C <= 30).
- **Core Insight**: Precompute cost[rem][col]: the total cost to repaint all cells with (r + c) % 3 == rem to color col. Then iterate over all P(C, 3) = C * (C - 1) * (C - 2) distinct triplets of colors (c0, c1, c2) assigned to remainders 0, 1, 2. For C = 30, 30 * 29 * 28 = 24,360 operations.
- **Complexity**: Time: `O(N^2 * C + C^3)` | Space: `O(C^2)`
- **Verified C++ Implementation**:
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
