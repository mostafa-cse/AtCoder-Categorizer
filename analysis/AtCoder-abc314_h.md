# Problem Analysis: AtCoder-abc314_h — H. Disk and Segments

**Problem ID**: `AtCoder-abc314_h`  
**Contest**: `abc314`  
**Rating / Difficulty**: 2938  
**URL**: https://atcoder.jp/contests/abc314/tasks/abc314_h  
**VJudge Tag**: `[problem:AtCoder-abc314_h]`  
**Category File**: [`../categories/miscellaneous/segment_covering_disk_nested_ternary_search.md`](../categories/miscellaneous/segment_covering_disk_nested_ternary_search.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Search Techniques`  
- **Topic (Skill)**: `Ternary Search`  

---

## 1. Problem Statement & Key Idea
Given N segments in the 2D plane, find the center (X, Y) of a disk of minimum radius R that intersects all N segments.

## 2. Core Observation & Invariant
For any fixed center (X, Y), the minimum radius required to touch all segments is R(X, Y) = max_i dist((X, Y), seg_i). The distance from a point to a line segment is a convex function of (X, Y). The upper envelope (maximum) of convex functions is strictly convex! Thus R(X, Y) is a convex function in both X and Y, permitting nested ternary search: outer ternary search on X in [-10^5, 10^5], inner ternary search on Y in [-10^5, 10^5].

## 3. Step-by-Step Algorithm
1. 1. Implement point-to-segment Euclidean distance function.
2. 2. Implement f(X, Y) = max_i dist((X, Y), seg_i).
3. 3. Inner ternary search over Y in [-10^5, 10^5] (85 iterations) to find min_Y f(X, Y).
4. 4. Outer ternary search over X in [-10^5, 10^5] (85 iterations) to minimize the inner function.
5. 5. Output optimal radius R with 10^-6 precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * K^2) where K approx 85`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Segment {
    double x1, y1, x2, y2;
};

inline double dist_point_segment(double px, double py, const Segment& seg) {
    double dx = seg.x2 - seg.x1;
    double dy = seg.y2 - seg.y1;
    if (dx == 0.0 && dy == 0.0) {
        return hypot(px - seg.x1, py - seg.y1);
    }
    double t = ((px - seg.x1) * dx + (py - seg.y1) * dy) / (dx * dx + dy * dy);
    t = max(0.0, min(1.0, t));
    double proj_x = seg.x1 + t * dx;
    double proj_y = seg.y1 + t * dy;
    return hypot(px - proj_x, py - proj_y);
}

inline double eval_R(double X, double Y, const vector<Segment>& segs) {
    double max_d = 0.0;
    for (const auto& seg : segs) {
        double d = dist_point_segment(X, Y, seg);
        if (d > max_d) max_d = d;
    }
    return max_d;
}

double min_Y(double X, const vector<Segment>& segs) {
    double low = -100.0, high = 1100.0;
    for (int iter = 0; iter < 85; ++iter) {
        double m1 = low + (high - low) / 3.0;
        double m2 = high - (high - low) / 3.0;
        if (eval_R(X, m1, segs) < eval_R(X, m2, segs)) {
            high = m2;
        } else {
            low = m1;
        }
    }
    return eval_R(X, (low + high) / 2.0, segs);
}

double solve_nested_ternary(const vector<Segment>& segs) {
    double low = -100.0, high = 1100.0;
    for (int iter = 0; iter < 85; ++iter) {
        double m1 = low + (high - low) / 3.0;
        double m2 = high - (high - low) / 3.0;
        if (min_Y(m1, segs) < min_Y(m2, segs)) {
            high = m2;
        } else {
            low = m1;
        }
    }
    return min_Y((low + high) / 2.0, segs);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<Segment> segs(N);
    for (int i = 0; i < N; ++i) {
        cin >> segs[i].x1 >> segs[i].y1 >> segs[i].x2 >> segs[i].y2;
    }

    double ans = solve_nested_ternary(segs);
    cout << fixed << setprecision(16) << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
