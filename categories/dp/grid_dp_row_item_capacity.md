# 2D Grid DP with Per-Row Item Capacity Constraint (At Most 3 Items)

**Domain**: `Dynamic Programming`  
**Subtopic**: `2D Grid DP`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Grid DP with Per-Row Item Capacity Constraint (At Most 3 Items)**.

---

## Curated Problems

### `[problem:AtCoder-abc175_e]` — Picking Goods
- **Rating / Difficulty**: 1554
- **Contest**: `abc175`
- **Analysis**: [`analysis/AtCoder-abc175_e.md`](../../analysis/AtCoder-abc175_e.md)
- **Key Idea**: 3D DP state: `dp[r][c][k]` representing the maximum value at cell (r, c) having picked k items in row r (k in 0..3).
- **Time Complexity**: `O(R * C)`
- **Space Complexity**: `O(R * C)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, K;
    if (!(cin >> R >> C >> K)) return 0;

    vector<vector<long long>> val(R + 1, vector<long long>(C + 1, 0));
    for (int i = 0; i < K; ++i) {
        int r, c;
        long long v;
        cin >> r >> c >> v;
        val[r][c] = v;
    }

    // dp[r][c][k]: max value at (r, c) with k items picked on row r
    vector<vector<vector<long long>>> dp(R + 1, vector<vector<long long>>(C + 1, vector<long long>(4, 0)));

    for (int r = 1; r <= R; ++r) {
        for (int c = 1; c <= C; ++c) {
            long long item = val[r][c];

            // Transition from above (r - 1, c): row resets
            long long max_above = 0;
            for (int k = 0; k < 4; ++k) max_above = max(max_above, dp[r - 1][c][k]);

            dp[r][c][0] = max(dp[r][c][0], max_above);
            if (item > 0) {
                dp[r][c][1] = max(dp[r][c][1], max_above + item);
            }

            // Transition from left (r, c - 1): same row
            for (int k = 0; k < 4; ++k) {
                dp[r][c][k] = max(dp[r][c][k], dp[r][c - 1][k]);
            }
            if (item > 0) {
                for (int k = 0; k < 3; ++k) {
                    dp[r][c][k + 1] = max(dp[r][c][k + 1], dp[r][c - 1][k] + item);
                }
            }
        }
    }

    long long ans = 0;
    for (int k = 0; k < 4; ++k) ans = max(ans, dp[R][C][k]);

    cout << ans << "\n";
    return 0;
}
```
