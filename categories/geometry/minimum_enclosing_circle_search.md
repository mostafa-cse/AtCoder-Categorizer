# Minimum Enclosing Circle: Pair and Triple Circumcircle Search

**Domain**: `Geometry`  
**Subtopic**: `Minimum Enclosing Circle`  

This workbook contains curated, high-quality competitive programming problems teaching **Minimum Enclosing Circle: Pair and Triple Circumcircle Search**.

---

## Curated Problems

### `[problem:AtCoder-abc151_f]` — Enclose All
- **Rating / Difficulty**: 1671
- **Contest**: `abc151`
- **Analysis**: [`analysis/AtCoder-abc151_f.md`](../../analysis/AtCoder-abc151_f.md)
- **Key Idea**: The minimum enclosing circle of a set of points is uniquely defined either by two points (as diameter) or by three points on its boundary (as circumcircle).
- **Time Complexity**: `O(N^4)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
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
