# Group-by-Value DP on Grids with Row/Column Maximum Buffering

**Domain**: `Dynamic Programming`  
**Subtopic**: `2D Grid DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Group-by-Value DP on Grids with Row/Column Maximum Buffering**.

---

## Curated Problems

### `[problem:AtCoder-abc224_e]` — Integers on Grid
- **Rating / Difficulty**: 1657
- **Contest**: `abc224`
- **Analysis**: [`analysis/AtCoder-abc224_e.md`](../../analysis/AtCoder-abc224_e.md)
- **Key Idea**: A point with value a_i transitions to any point in row r or column c with value > a_i. Process all points grouped by value in DESCENDING order.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N + H + W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

struct Point {
    int id, r, c, a;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n;
    if (!(cin >> h >> w >> n)) return 0;

    map<int, vector<Point>> groups;
    for (int i = 0; i < n; ++i) {
        int r, c, a;
        cin >> r >> c >> a;
        groups[a].push_back({i, r, c, a});
    }

    vector<int> ans(n, 0);
    vector<int> row_max(h + 1, 0);
    vector<int> col_max(w + 1, 0);

    // Process from largest value down to smallest
    for (auto it = groups.rbegin(); it != groups.rend(); ++it) {
        const auto& pts = it->second;

        // Step 1: Query max moves
        vector<int> cur_dp(pts.size());
        for (size_t i = 0; i < pts.size(); ++i) {
            cur_dp[i] = max(row_max[pts[i].r], col_max[pts[i].c]);
            ans[pts[i].id] = cur_dp[i];
        }

        // Step 2: Commit updates
        for (size_t i = 0; i < pts.size(); ++i) {
            row_max[pts[i].r] = max(row_max[pts[i].r], cur_dp[i] + 1);
            col_max[pts[i].c] = max(col_max[pts[i].c], cur_dp[i] + 1);
        }
    }

    for (int i = 0; i < n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
