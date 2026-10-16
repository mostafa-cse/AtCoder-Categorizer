# 2D Prefix Sums on Interval Endpoints [L, R]

**Domain**: `Data Structures`  
**Subtopic**: `2D Prefix Sums`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Prefix Sums on Interval Endpoints [L, R]**.

---

## Curated Problems

### [problem:AtCoder-abc106_d] — AtCoder Express 2
- **Contest**: `abc106`
- **Rating / Difficulty**: 1319
- **Specific Skill**: 2D Prefix Sums on Interval Endpoints [L, R]
- **Individual Analysis**: [`../../analysis/AtCoder-abc106_d.md`](../../analysis/AtCoder-abc106_d.md)
- **Problem Statement Summary**: M train lines, where train i runs between cities L_i and R_i (1 <= L_i <= R_i <= N <= 500). Q queries: count train lines running strictly inside interval [p, q] (i.e. p <= L_i and R_i <= q).
- **Core Insight**: A train line lies entirely within [p, q] if and only if its left endpoint satisfies p <= L and its right endpoint satisfies R <= q. In the 2D plane, this corresponds to querying the number of points in the bounding box [p, N] x [1, q], solved in O(1) using standard 2D prefix sums!
- **Complexity**: Time: `O(N^2 + Q)` | Space: `O(N^2)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    vector<vector<int>> grid(n + 1, vector<int>(n + 1, 0));
    for (int i = 0; i < m; ++i) {
        int l, r;
        cin >> l >> r;
        grid[l][r]++;
    }

    vector<vector<int>> pref(n + 1, vector<int>(n + 1, 0));
    for (int r = 1; r <= n; ++r) {
        for (int c = 1; c <= n; ++c) {
            pref[r][c] = grid[r][c] + pref[r - 1][c] + pref[r][c - 1] - pref[r - 1][c - 1];
        }
    }

    while (q--) {
        int p, q_end;
        cin >> p >> q_end;
        int ans = pref[q_end][q_end] - pref[p - 1][q_end] - pref[q_end][p - 1] + pref[p - 1][p - 1];
        cout << ans << "\n";
    }

    return 0;
}
```
