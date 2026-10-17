# Problem Analysis: AtCoder-agc021_b — Holes

**Problem ID**: `AtCoder-agc021_b`  
**Contest**: `agc021`  
**Rating / Difficulty**: 2130  
**URL**: https://atcoder.jp/contests/agc021/tasks/agc021_b  
**VJudge Tag**: `[problem:AtCoder-agc021_b]`  
**Category File**: [`../categories/geometry/convex_hull_normal_angular_span.md`](../categories/geometry/convex_hull_normal_angular_span.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Convex Hull(2D)`  

---

## 1. Problem Statement & Key Idea
N holes are given on a 2D plane. A ball is placed uniformly at random on a circle of radius R -> infinity and falls into the closest hole. Find the probability that each hole receives the ball.

**Key Insight**: As R -> infinity, only vertices on the strictly exterior Convex Hull have unbounded Voronoi cells that reach infinity; all interior points receive the ball with probability 0. For a convex hull vertex P, the set of directions from which P is the unique closest point is the angular span between the outward normal of the incident incoming edge and the outward normal of the incident outgoing edge. The probability is exactly (exterior angle span) / (2 * pi).

## 2. Core Observation & Invariant
Voronoi cell area at infinity is proportional to the exterior normal angular span of the convex hull vertices.

## 3. Step-by-Step Algorithm
1. If N == 2: both points have probability 0.5.
2. Construct Convex Hull using Monotone Chain.
3. For each vertex on the convex hull:
4.   Compute outward normal angle of incoming edge.
5.   Compute outward normal angle of outgoing edge.
6.   Calculate angular difference in [0, 2pi].
7.   Probability = angle_span / (2 * pi).
8. Output probability for each original point.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Convex hull construction and outward normal angular span computation for infinite Voronoi measures.
- **Reusable Pattern**: Asymptotic nearest-neighbor probabilities on 2D point sets determined by convex hull exterior normal angles.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

const double PI = acos(-1.0);

struct Point {
    long long x, y;
    int id;
};

long long cross(Point a, Point b, Point c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].x >> pts[i].y;
        pts[i].id = i;
    }

    if (n == 2) {
        cout << fixed << setprecision(10);
        cout << 0.5 << "\n" << 0.5 << "\n";
        return 0;
    }

    vector<Point> p = pts;
    sort(p.begin(), p.end(), [](const Point& a, const Point& b) {
        if (a.x != b.x) return a.x < b.x;
        return a.y < b.y;
    });

    vector<Point> hull;
    for (int i = 0; i < n; ++i) {
        while (hull.size() >= 2 && cross(hull[hull.size() - 2], hull.back(), p[i]) <= 0) {
            hull.pop_back();
        }
        hull.push_back(p[i]);
    }
    int t = hull.size() + 1;
    for (int i = n - 2; i >= 0; --i) {
        while ((int)hull.size() >= t && cross(hull[hull.size() - 2], hull.back(), p[i]) <= 0) {
            hull.pop_back();
        }
        hull.push_back(p[i]);
    }
    hull.pop_back();

    vector<double> ans(n, 0.0);
    int h = hull.size();

    for (int i = 0; i < h; ++i) {
        Point prev_p = hull[(i - 1 + h) % h];
        Point cur_p = hull[i];
        Point next_p = hull[(i + 1) % h];

        double a1 = atan2(cur_p.y - prev_p.y, cur_p.x - prev_p.x) - PI / 2.0;
        double a2 = atan2(next_p.y - cur_p.y, next_p.x - cur_p.x) - PI / 2.0;

        while (a2 < a1) a2 += 2 * PI;
        double angle_span = a2 - a1;
        ans[cur_p.id] = angle_span / (2 * PI);
    }

    cout << fixed << setprecision(10);
    for (int i = 0; i < n; ++i) {
        cout << ans[i] << "\n";
    }

    return 0;
}
```
