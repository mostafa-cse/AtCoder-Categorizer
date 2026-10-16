# 2D Grid DP with 3-Way Running Prefix Sums

**Domain**: `Dynamic Programming`  
**Subtopic**: `Grid DP`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Grid DP with 3-Way Running Prefix Sums**.

---

## Curated Problems

### [problem:AtCoder-abc183_e] — Queen on Grid
- **Contest**: `abc183`
- **Rating / Difficulty**: 1288
- **Specific Skill**: 2D Grid DP with 3-Way Running Prefix Sums
- **Individual Analysis**: [`../../analysis/AtCoder-abc183_e.md`](../../analysis/AtCoder-abc183_e.md)
- **Problem Statement Summary**: An H x W grid of '.' and '#'. Start at (1, 1), reach (H, W). A piece can move any number of steps right, down, or down-right without passing obstacles '#'. Find the number of paths modulo 10^9 + 7.
- **Core Insight**: Naive summation takes O(H * W * max(H, W)). Maintain 3 running prefix sums at each cell: X[r][c] (horizontal prefix), Y[r][c] (vertical prefix), and Z[r][c] (diagonal prefix). If cell is '#', all prefixes reset to 0. Else dp[r][c] = X + Y + Z in O(1)!
- **Complexity**: Time: `O(H * W)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    vector<vector<long long>> dp(h, vector<long long>(w, 0));
    vector<vector<long long>> X(h, vector<long long>(w, 0));
    vector<vector<long long>> Y(h, vector<long long>(w, 0));
    vector<vector<long long>> Z(h, vector<long long>(w, 0));

    dp[0][0] = 1;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '#') continue;

            if (r > 0 || c > 0) {
                dp[r][c] = (X[r][c] + Y[r][c] + Z[r][c]) % MOD;
            }

            // Propagate to right
            if (c + 1 < w) X[r][c + 1] = (X[r][c] + dp[r][c]) % MOD;
            // Propagate down
            if (r + 1 < h) Y[r + 1][c] = (Y[r][c] + dp[r][c]) % MOD;
            // Propagate diagonal
            if (r + 1 < h && c + 1 < w) Z[r + 1][c + 1] = (Z[r][c] + dp[r][c]) % MOD;
        }
    }

    cout << dp[h - 1][w - 1] << "\n";
    return 0;
}
```
