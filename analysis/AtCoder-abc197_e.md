# Problem Analysis: AtCoder-abc197_e — Traveler

**Problem ID**: `AtCoder-abc197_e`  
**Contest**: `abc197`  
**Rating / Difficulty**: 1379  
**URL**: https://atcoder.jp/contests/abc197/tasks/abc197_e  
**VJudge Tag**: `[problem:AtCoder-abc197_e]`  
**Category File**: [`../categories/dp/color_segments_left_right_dp.md`](../categories/dp/color_segments_left_right_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Linear DP`  
- **Topic (Skill)**: `Coordinate Compression Color Segments Left/Right DP`  

---

## 1. Problem Statement & Key Idea
N balls on a line with coordinates X_i and colors C_i. You must pick all balls of color 1, then all of color 2, ..., then color K, and return to coordinate 0. Minimize total distance traveled.

**Key Idea**: For each color c, to collect all balls of color c, we must cover the bounding interval [min_X[c], max_X[c]].

## 2. Core Observation & Invariant
When collecting balls of color c, we will inevitably end either at its leftmost ball min_X[c] or its rightmost ball max_X[c]! Define DP state: dp[c][0] = min distance ending at min_X[c]; dp[c][1] = min distance ending at max_X[c]. Transitions consider moving from previous endpoints to the new segment and sweeping to the other end.

## 3. Step-by-Step Algorithm
1. For each present color c, record min_x[c] and max_x[c].
2. Initialize dp_l = 0, dp_r = 0 at pos_l = 0, pos_r = 0 (origin).
3. For each color segment [L, R]:
4.   Cost to finish at L: sweep to R then L: min(dp_l + |pos_l - R|, dp_r + |pos_r - R|) + (R - L).
5.   Cost to finish at R: sweep to L then R: min(dp_l + |pos_l - L|, dp_r + |pos_r - L|) + (R - L).
6.   Update dp values and positions.
7. Finally, return to 0: min(dp_l + |pos_l|, dp_r + |pos_r|).

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Segment endpoint DP transitions on sequential 1D bounding intervals.
- **Reusable Pattern**: `Interval sweep DP: finish at Left or Right endpoint of current bounding box.`
