# Convex Hull(2D)

**Domain**: `Geometry`  
**Subtopic**: `Geometry 2D`  

This workbook contains curated, high-quality competitive programming problems teaching **Convex Hull(2D)**.

---

## Curated Problems

### `[problem:AtCoder-agc021_b]` — Holes
- **Rating / Difficulty**: 2130
- **Contest**: `agc021`
- **Analysis**: [`analysis/AtCoder-agc021_b.md`](../../analysis/AtCoder-agc021_b.md)
- **Key Idea**: As R -> infinity, only vertices on the strictly exterior Convex Hull have unbounded Voronoi cells that reach infinity; all interior points receive the ball with probability 0. For a convex hull vertex P, the set of directions from which P is the unique closest point is the angular span between the outward normal of the incident incoming edge and the outward normal of the incident outgoing edge. The probability is exactly (exterior angle span) / (2 * pi).
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
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
