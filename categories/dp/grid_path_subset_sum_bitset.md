# Grid Path Subset Sum with Bitset Acceleration

**Domain**: `Dynamic Programming`  
**Subtopic**: `Grid DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Grid Path Subset Sum with Bitset Acceleration**.

---

## Curated Problems

### `[problem:AtCoder-abc147_e]` — Balanced Path
- **Rating / Difficulty**: 1713
- **Contest**: `abc147`
- **Analysis**: [`analysis/AtCoder-abc147_e.md`](../../analysis/AtCoder-abc147_e.md)
- **Key Idea**: The maximum possible sum is (H + W - 1) * 80 <= 159 * 80 = 12720. Using a bitset of size 25441 (with offset 12720), maintain all reachable difference sums at cell (i, j) by shifting left and right by D_{i, j}.
- **Time Complexity**: `O(H * W * MAX_SUM / 64)`
- **Space Complexity**: `O(H * W * MAX_SUM / 64)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <bitset>
#include <cmath>

using namespace std;

const int MAX_VAL = 12800;
const int OFFSET = MAX_VAL;
const int SIZE = 2 * MAX_VAL + 5;

bitset<SIZE> dp[85][85];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<vector<int>> a(h, vector<int>(w));
    vector<vector<int>> b(h, vector<int>(w));
    vector<vector<int>> d(h, vector<int>(w));

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) cin >> a[i][j];
    }
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            cin >> b[i][j];
            d[i][j] = abs(a[i][j] - b[i][j]);
        }
    }

    dp[0][0][OFFSET + d[0][0]] = 1;
    dp[0][0][OFFSET - d[0][0]] = 1;

    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (i == 0 && j == 0) continue;
            bitset<SIZE> prev;
            if (i > 0) prev |= dp[i - 1][j];
            if (j > 0) prev |= dp[i][j - 1];

            int diff = d[i][j];
            dp[i][j] = (prev << diff) | (prev >> diff);
        }
    }

    int min_diff = 1e9;
    for (int k = 0; k < SIZE; ++k) {
        if (dp[h - 1][w - 1][k]) {
            min_diff = min(min_diff, abs(k - OFFSET));
        }
    }

    cout << min_diff << "\n";
    return 0;
}
```
