# Coordinate Compression Color Segments Left/Right DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `Linear DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Coordinate Compression Color Segments Left/Right DP**.

---

## Curated Problems

### [problem:AtCoder-abc197_e] — Traveler
- **Contest**: `abc197`
- **Rating / Difficulty**: 1379
- **Specific Skill**: Coordinate Compression Color Segments Left/Right DP
- **Individual Analysis**: [`../../analysis/AtCoder-abc197_e.md`](../../analysis/AtCoder-abc197_e.md)
- **Problem Statement Summary**: N balls on a line with coordinates X_i and colors C_i. You must pick all balls of color 1, then all of color 2, ..., then color K, and return to coordinate 0. Minimize total distance traveled.
- **Core Insight**: When collecting balls of color c, we will inevitably end either at its leftmost ball min_X[c] or its rightmost ball max_X[c]! Define DP state: dp[c][0] = min distance ending at min_X[c]; dp[c][1] = min distance ending at max_X[c]. Transitions consider moving from previous endpoints to the new segment and sweeping to the other end.
- **Complexity**: Time: `O(N log N)` | Space: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

const long long INF = 4e18;

struct Segment {
    long long l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    map<int, pair<long long, long long>> color_bounds;
    for (int i = 0; i < n; ++i) {
        long long x;
        int c;
        cin >> x >> c;
        if (!color_bounds.count(c)) {
            color_bounds[c] = {x, x};
        } else {
            color_bounds[c].first = min(color_bounds[c].first, x);
            color_bounds[c].second = max(color_bounds[c].second, x);
        }
    }

    long long dp_l = 0, dp_r = 0;
    long long cur_l = 0, cur_r = 0;

    for (const auto& [color, bounds] : color_bounds) {
        long long L = bounds.first;
        long long R = bounds.second;
        long long span = R - L;

        // Finish at L (must visit R first)
        long long next_dp_l = min(dp_l + abs(cur_l - R), dp_r + abs(cur_r - R)) + span;

        // Finish at R (must visit L first)
        long long next_dp_r = min(dp_l + abs(cur_l - L), dp_r + abs(cur_r - L)) + span;

        dp_l = next_dp_l;
        dp_r = next_dp_r;
        cur_l = L;
        cur_r = R;
    }

    long long ans = min(dp_l + abs(cur_l), dp_r + abs(cur_r));
    cout << ans << "\n";
    return 0;
}
```
