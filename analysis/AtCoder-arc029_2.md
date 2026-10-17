# Problem Analysis: AtCoder-arc029_2 — 高橋君と禁断の書

**Problem ID**: `AtCoder-arc029_2`  
**Contest**: `arc029`  
**Rating / Difficulty**: 2032  
**URL**: https://atcoder.jp/contests/arc029/tasks/arc029_2  
**VJudge Tag**: `[problem:AtCoder-arc029_2]`  
**Category File**: [`../categories/geometry/rotated_rectangle_bounding_box_binary_search.md`](../categories/geometry/rotated_rectangle_bounding_box_binary_search.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Rotational Sweep & Convex Polygons`  
- **Topic (Skill)**: `Rotated Rectangle Bounding Box Containment via Binary Search on Angle`  

---

## 1. Problem Statement & Key Idea
A book is a rectangle of dimensions A x B. Process N queries: can it fit inside a rectangular hole of dimensions C_i x D_i after rotating by some angle theta in [0, pi/2]?

**Key Idea**: Assume A >= B without loss of generality. When rotated by angle theta in [0, pi/2], the bounding box dimensions of the rectangle are W(theta) = A cos(theta) + B sin(theta) and H(theta) = A sin(theta) + B cos(theta). W(theta) is strictly decreasing on [0, pi/2] while H(theta) is strictly increasing. To test if W(theta) <= C and H(theta) <= D, we binary search on the minimum angle theta in [0, pi/2] such that W(theta) <= C, and check if H(theta) <= D. We test both orientations (C, D) and (D, C).

## 2. Core Observation & Invariant
Monotonicity of rotated bounding box width and height enables binary searching the exact transition angle.

## 3. Step-by-Step Algorithm
1. Ensure A >= B.
2. Define test(C, D):
3.   If A <= C && B <= D: return true (no rotation needed).
4.   If B > C || B > D: return false.
5.   Binary search theta in [0, pi / 2] with 60 iterations:
6.     mid = (low + high) / 2.
7.     w = A * cos(mid) + B * sin(mid).
8.     if w <= C: high = mid (can rotate less/more).
9.     else: low = mid.
10.   Evaluate H(high) = A * sin(high) + B * cos(high).
11.   If H(high) <= D: return true.
12. For each query (C, D):
13.   If test(C, D) or test(D, C): print YES; else NO.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * log(precision))`
- **Space Complexity**: `O(1)`

## 5. Core Algorithmic Skill & Learning Takeaway
Continuous bounding box trigonometric monotonicity and binary search.

**Reusable Pattern**: Rotated Bounding Box Check: W(theta) = A cos theta + B sin theta; binary search theta to satisfy width bound, then verify height.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

const double PI = acos(-1.0);

bool can_fit(double A, double B, double C, double D) {
    if (A <= C && B <= D) return true;
    if (B > C || B > D) return false;

    // Binary search angle theta in [0, PI / 2] where W(theta) <= C
    // W(theta) = A * cos(theta) + B * sin(theta) is decreasing from A down to B
    double low = 0.0, high = PI / 2.0;
    for (int iter = 0; iter < 70; ++iter) {
        double mid = (low + high) / 2.0;
        double w = A * cos(mid) + B * sin(mid);
        if (w <= C) {
            high = mid;
        } else {
            low = mid;
        }
    }

    double h = A * sin(high) + B * cos(high);
    return h <= D;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double a, b;
    if (!(cin >> a >> b)) return 0;
    if (a < b) swap(a, b);

    int n;
    if (!(cin >> n)) return 0;

    while (n--) {
        double c, d;
        cin >> c >> d;
        if (can_fit(a, b, c, d) || can_fit(a, b, d, c)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
```
