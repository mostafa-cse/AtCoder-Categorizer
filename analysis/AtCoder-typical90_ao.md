# Problem Analysis: AtCoder-typical90_ao — Piles in AtCoder Farm

**Problem ID**: `AtCoder-typical90_ao`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 041)  
**Rating / Difficulty**: 2600 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ao  
**VJudge Tag**: `[problem:AtCoder-typical90_ao]`  
**Category File**: [`../categories/geometry/convex_hull_picks_theorem.md`](../categories/geometry/convex_hull_picks_theorem.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Convex Hull & Pick's Theorem`  
- **Topic (Skill)**: `Convex Hull + Pick's Theorem + Shoelace Formula for Lattice Points`  

---

## 1. Problem Statement & Key Idea
Given N points in 2D plane, find the number of integer lattice points contained inside or on the boundary of their convex hull.

**Core Idea**: Compute Convex Hull using Monotone Chain, then apply Pick's Theorem: Area = I + B/2 - 1.

## 2. Core Observation & Invariant
Total lattice points = I + B = Area + B/2 + 1. Area is computed using Shoelace formula (2 * Area = cross products). Boundary points B on segment (P1, P2) is gcd(|x1 - x2|, |y1 - y2|).

## 3. Step-by-Step Algorithm
1. Compute convex hull using Monotone Chain algorithm.
2. Compute 2 * Area using Shoelace formula.
3. Compute boundary points B = sum gcd(|dx|, |dy|) for all hull edges.
4. Output (2 * Area + B) / 2 + 1 - N (or total lattice points - N if asking for new points).

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;

struct Point {
    long long x, y;
};

long long cross(const Point& O, const Point& A, const Point& B) {
    return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x);
}

vector<Point> convex_hull(vector<Point>& pts) {
    int n = pts.size(), k = 0;
    if (n <= 2) return pts;
    vector<Point> h(2 * n);
    sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
        if (a.x != b.x) return a.x < b.x;
        return a.y < b.y;
    });

    for (int i = 0; i < n; ++i) {
        while (k >= 2 && cross(h[k - 2], h[k - 1], pts[i]) <= 0) k--;
        h[k++] = pts[i];
    }
    for (int i = n - 2, t = k + 1; i >= 0; --i) {
        while (k >= t && cross(h[k - 2], h[k - 1], pts[i]) <= 0) k--;
        h[k++] = pts[i];
    }
    h.resize(k - 1);
    return h;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].x >> pts[i].y;
    }

    vector<Point> hull = convex_hull(pts);
    int m = hull.size();

    long long area2 = 0;
    long long b = 0;

    for (int i = 0; i < m; ++i) {
        Point p1 = hull[i];
        Point p2 = hull[(i + 1) % m];
        area2 += (p1.x * p2.y - p2.x * p1.y);
        b += gcd(abs(p1.x - p2.x), abs(p1.y - p2.y));
    }
    area2 = abs(area2);

    long long total_lattice = (area2 + b) / 2 + 1;
    cout << total_lattice - n << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Convex hull with Shoelace formula and Pick's Theorem.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Pick's Theorem, Monotone Chain convex hull, and counting integer lattice points in polygons.
- **Reusable Pattern**: `Convex Hull + Pick's Theorem + Shoelace Formula.`

---
Back to [Convex Hull + Pick's Theorem + Shoelace Formula for Lattice Points](../categories/geometry/convex_hull_picks_theorem.md) | [Categories Directory](../categories/README.md)