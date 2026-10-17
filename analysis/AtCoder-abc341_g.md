# Problem Analysis: AtCoder-abc341_g — Highest Ratio

**Problem ID**: `AtCoder-abc341_g`  
**Contest**: `abc341`  
**Rating / Difficulty**: 2208  
**URL**: https://atcoder.jp/contests/abc341/tasks/abc341_g  
**VJudge Tag**: `[problem:AtCoder-abc341_g]`  
**Category File**: [`../categories/geometry/highest_ratio_geometric_slope_lower_hull_monotonic_stack.md`](../categories/geometry/highest_ratio_geometric_slope_lower_hull_monotonic_stack.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Convex Hull(2D)`  

---

## 1. Problem Statement & Key Idea
Geometric slope interpretation of subsegment average as tangent to lower convex hull maintained via right-to-left monotonic stack.

## 2. Core Observation & Invariant
The average of A[k..r] is (S_r - S_{k-1}) / (r - (k - 1)), which is the slope between points (k - 1, S_{k-1}) and (r, S_r). Maximizing slope from (k - 1, S_{k-1}) to points to its right is equivalent to finding the tangent to the lower convex hull of { (j, S_j) : j >= k }.

## 3. Step-by-Step Algorithm
1. 1. Compute prefix sums S_0, S_1, ..., S_N.
2. 2. Process k from N down to 1, maintaining the lower convex hull in a monotonic stack.
3. 3. While the top two points of the hull form a non-convex turn with (k - 1, S_{k-1}), pop the top.
4. 4. The maximum slope is the slope from (k - 1, S_{k-1}) to the top point of the hull.
5. 5. Push (k - 1, S_{k-1}) onto the stack.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Point {
    ll x, y;
};

// Check if slope(p1 -> p2) <= slope(p2 -> p3)
// (y2 - y1) / (x2 - x1) <= (y3 - y2) / (x3 - x2)
// (y2 - y1) * (x3 - x2) <= (y3 - y2) * (x2 - x1)
bool bad_turn(const Point& p1, const Point& p2, const Point& p3) {
    return (p2.y - p1.y) * (p3.x - p2.x) <= (p3.y - p2.y) * (p2.x - p1.x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;

    vector<ll> A(N + 1);
    vector<ll> S(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
        S[i] = S[i - 1] + A[i];
    }

    vector<Point> hull;
    hull.push_back({N, S[N]});

    vector<double> ans(N + 1);

    for (int k = N; k >= 1; --k) {
        Point p0 = {k - 1, S[k - 1]};
        while (hull.size() >= 2) {
            Point p1 = hull.back();
            Point p2 = hull[hull.size() - 2];
            if (bad_turn(p0, p1, p2)) {
                hull.pop_back();
            } else {
                break;
            }
        }

        Point best = hull.back();
        ans[k] = (double)(best.y - p0.y) / (double)(best.x - p0.x);
        hull.push_back(p0);
    }

    cout << fixed << setprecision(8);
    for (int k = 1; k <= N; ++k) {
        cout << ans[k] << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
