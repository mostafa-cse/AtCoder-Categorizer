# Problem Analysis: AtCoder-abc296_g — Polygon and Points

**Problem ID**: `AtCoder-abc296_g`  
**Contest**: `abc296`  
**Rating / Difficulty**: 2241  
**URL**: https://atcoder.jp/contests/abc296/tasks/abc296_g  
**VJudge Tag**: `[problem:AtCoder-abc296_g]`  
**Category File**: [`../categories/geometry/point_in_convex_polygon_log_n_queries.md`](../categories/geometry/point_in_convex_polygon_log_n_queries.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Point in Convex Polygon in log(N)(2D)`  

---

## 1. Problem Statement & Key Idea
Determine whether each of Q query points lies strictly inside (IN), on the boundary (ON), or strictly outside (OUT) a strictly convex N-gon.

## 2. Core Observation & Invariant
A strictly convex N-gon with CCW vertices P_0, ..., P_{N-1} can be decomposed into N-2 triangular sectors originating from P_0. For any query point Q, check if it falls within the wedge between rays P_0->P_1 and P_0->P_{N-1}. If so, binary search in O(log N) on the sector index i in [1, N-2] where Q lies between ray P_0->P_i and P_0->P_{i+1}. Then test orientation of Q relative to the outer edge P_i->P_{i+1} using 2D cross products to classify as IN, ON, or OUT.

## 3. Step-by-Step Algorithm
1. 1. For each query point pt, first check if it lies on segment P_0->P_1 or P_0->P_{N-1} (ON).
2. 2. Test if pt is strictly outside the wedge from P_0: cross(P_1 - P_0, pt - P_0) < 0 or cross(P_{N-1} - P_0, pt - P_0) > 0 (OUT).
3. 3. Binary search on index mid in [1, N-1] with cross(P_mid - P_0, pt - P_0) >= 0 to isolate the triangular sector P_0, P_low, P_{low+1}.
4. 4. Evaluate cross product cp = cross(P_{low+1} - P_low, pt - P_low):
5.    - If cp < 0: OUT.
6.    - If cp == 0: ON if pt lies on segment P_low->P_{low+1}, else OUT.
7.    - If cp > 0: IN.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
    Point(long long x = 0, long long y = 0) : x(x), y(y) {}
};

Point operator-(const Point& a, const Point& b) {
    return Point(a.x - b.x, a.y - b.y);
}

long long cross(const Point& a, const Point& b) {
    // __int128 to prevent overflow since coords are up to 10^9
    __int128 res = (__int128)a.x * b.y - (__int128)a.y * b.x;
    if (res > 0) return 1;
    if (res < 0) return -1;
    return 0;
}

long long dot(const Point& a, const Point& b) {
    __int128 res = (__int128)a.x * b.x + (__int128)a.y * b.y;
    if (res > 0) return 1;
    if (res < 0) return -1;
    return 0;
}

bool on_segment(const Point& p, const Point& a, const Point& b) {
    if (cross(b - a, p - a) != 0) return false;
    return p.x >= min(a.x, b.x) && p.x <= max(a.x, b.x) &&
           p.y >= min(a.y, b.y) && p.y <= max(a.y, b.y);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> P(n);
    for (int i = 0; i < n; ++i) {
        cin >> P[i].x >> P[i].y;
    }

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        Point pt;
        cin >> pt.x >> pt.y;

        // Check boundary on the two wedge edges
        if (on_segment(pt, P[0], P[1])) {
            cout << "ON\n";
            continue;
        }
        if (on_segment(pt, P[0], P[n - 1])) {
            cout << "ON\n";
            continue;
        }

        // Check if outside the wedge from P[0]
        // Wedge is from ray P[0]->P[1] to ray P[0]->P[n-1] CCW
        if (cross(P[1] - P[0], pt - P[0]) < 0 || cross(P[n - 1] - P[0], pt - P[0]) > 0) {
            cout << "OUT\n";
            continue;
        }

        // Binary search for ray sector
        // Sector i is between ray P[0]->P[i] and ray P[0]->P[i+1]
        // cross(P[i] - P[0], pt - P[0]) >= 0 for all i in sector
        int low = 1, high = n - 1;
        while (high - low > 1) {
            int mid = low + (high - low) / 2;
            if (cross(P[mid] - P[0], pt - P[0]) >= 0) {
                low = mid;
            } else {
                high = mid;
            }
        }

        // The point is in triangle P[0], P[low], P[low + 1]
        // Check relative to segment P[low] -> P[low + 1]
        long long cp = cross(P[low + 1] - P[low], pt - P[low]);
        if (cp < 0) {
            cout << "OUT\n";
        } else if (cp == 0) {
            // on boundary segment P[low]->P[low+1]
            if (on_segment(pt, P[low], P[low + 1])) {
                cout << "ON\n";
            } else {
                cout << "OUT\n";
            }
        } else {
            // strictly to the left of segment P[low]->P[low+1]
            cout << "IN\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
