# Moment-Tracking Grid Path DP (E[X^2] Expansion)

**Domain**: `Dynamic Programming`  
**Subtopic**: `Grid DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Moment-Tracking Grid Path DP (E[X^2] Expansion)**.

---

## Curated Problems

### `[problem:AtCoder-arc157_c]` — YY Square
- **Rating / Difficulty**: 1802
- **Contest**: `arc157`
- **Analysis**: [`analysis/AtCoder-arc157_c.md`](../../analysis/AtCoder-arc157_c.md)
- **Key Idea**: To compute sum of squared scores, track the 0th, 1st, and 2nd algebraic moments along paths: dp0 = number of paths, dp1 = sum of scores, dp2 = sum of squared scores. When taking a step that adds 1: (x + 1)^2 = x^2 + 2x + 1.
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) cin >> grid[i];

    vector<vector<long long>> dp0(h, vector<long long>(w, 0));
    vector<vector<long long>> dp1(h, vector<long long>(w, 0));
    vector<vector<long long>> dp2(h, vector<long long>(w, 0));

    dp0[0][0] = 1;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            long long p0 = dp0[r][c], p1 = dp1[r][c], p2 = dp2[r][c];
            if (p0 == 0) continue;

            // Step down
            if (r + 1 < h) {
                int delta = (grid[r][c] == 'Y' && grid[r + 1][c] == 'Y') ? 1 : 0;
                dp0[r + 1][c] = (dp0[r + 1][c] + p0) % MOD;
                dp1[r + 1][c] = (dp1[r + 1][c] + p1 + delta * p0) % MOD;
                dp2[r + 1][c] = (dp2[r + 1][c] + p2 + 2LL * delta * p1 + delta * p0) % MOD;
            }

            // Step right
            if (c + 1 < w) {
                int delta = (grid[r][c] == 'Y' && grid[r][c + 1] == 'Y') ? 1 : 0;
                dp0[r][c + 1] = (dp0[r][c + 1] + p0) % MOD;
                dp1[r][c + 1] = (dp1[r][c + 1] + p1 + delta * p0) % MOD;
                dp2[r][c + 1] = (dp2[r][c + 1] + p2 + 2LL * delta * p1 + delta * p0) % MOD;
            }
        }
    }

    cout << dp2[h - 1][w - 1] << "\n";
    return 0;
}
```
