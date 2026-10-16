# Problem Analysis: AtCoder-abc151_f — Enclose All

**Problem ID**: `AtCoder-abc151_f`  
**Contest**: `abc151`  
**Rating / Difficulty**: 1671  
**URL**: https://atcoder.jp/contests/abc151/tasks/abc151_f  
**VJudge Tag**: `[problem:AtCoder-abc151_f]`  
**Category File**: [`../categories/geometry/minimum_enclosing_circle_search.md`](../categories/geometry/minimum_enclosing_circle_search.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Minimum Enclosing Circle`  
- **Topic (Skill)**: `Minimum Enclosing Circle: Pair and Triple Circumcircle Search`  

---

## 1. Problem Statement & Key Idea
Given N points in the 2D plane (N <= 50). Find the minimum radius of a closed circle that contains all N points on or inside its boundary.

**Key Insight**: The minimum enclosing circle of a set of points is uniquely defined either by two points (as diameter) or by three points on its boundary (as circumcircle).

## 2. Core Observation & Invariant
Because N <= 50, test all pairs of points (C(50, 2) = 1225 circles) and all triples of non-collinear points (C(50, 3) = 19,600 circles). For each candidate circle, check if all N points lie inside in O(N). Total operations <= 20,000 * 50 ~ 10^6.

## 3. Step-by-Step Algorithm
1. Candidate circles from 2 points (p1, p2): center = (p1 + p2)/2, radius = dist(p1, p2)/2.
2. Candidate circles from 3 points (p1, p2, p3): circumcenter and circumradius.
3. For each candidate circle (center, r):
4.   If all N points have dist(center, pt) <= r + 1e-9:
5.     min_radius = min(min_radius, r).
6. Print min_radius with 12 decimals.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^4)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

struct Point {
    double x, y;
};

double dist(Point a, Point b) {
    return hypot(a.x - b.x, a.y - b.y);
}

// Circumcircle of 3 points
bool get_circle_3(Point p1, Point p2, Point p3, Point& center, double& r) {
    double d = 2 * (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y));
    if (abs(d) < 1e-9) return false;

    double p1_sq = p1.x * p1.x + p1.y * p1.y;
    double p2_sq = p2.x * p2.x + p2.y * p2.y;
    double p3_sq = p3.x * p3.x + p3.y * p3.y;

    center.x = (p1_sq * (p2.y - p3.y) + p2_sq * (p3.y - p1.y) + p3_sq * (p1.y - p2.y)) / d;
    center.y = (p1_sq * (p3.x - p2.x) + p2_sq * (p1.x - p3.x) + p3_sq * (p2.x - p1.x)) / d;
    r = dist(center, p1);
    return true;
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

    double min_r = 1e9;

    auto test_circle = [&](Point center, double r) {
        for (int i = 0; i < n; ++i) {
            if (dist(center, pts[i]) > r + 1e-9) return;
        }
        min_r = min(min_r, r);
    };

    // 2-point candidates
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            Point center = {(pts[i].x + pts[j].x) / 2.0, (pts[i].y + pts[j].y) / 2.0};
            double r = dist(pts[i], pts[j]) / 2.0;
            test_circle(center, r);
        }
    }

    // 3-point candidates
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            for (int k = j + 1; k < n; ++k) {
                Point center;
                double r;
                if (get_circle_3(pts[i], pts[j], pts[k], center, r)) {
                    test_circle(center, r);
                }
            }
        }
    }

    cout << fixed << setprecision(12) << min_r << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Geometric minimum enclosing circle candidate generation via 2-point and 3-point boundary sets.
- **Reusable Pattern**: `Minimum Enclosing Circle: test 2-point diameters and 3-point circumcenters.`
