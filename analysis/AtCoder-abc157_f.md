# Problem Analysis: AtCoder-abc157_f — F. Yakiniku Optimization Problem

**Problem ID**: `AtCoder-abc157_f`  
**Contest**: `abc157`  
**Rating / Difficulty**: 2525  
**URL**: https://atcoder.jp/contests/abc157/tasks/abc157_f  
**VJudge Tag**: `[problem:AtCoder-abc157_f]`  
**Category File**: [`../categories/geometry/yakiniku_optimization_circle_intersections.md`](../categories/geometry/yakiniku_optimization_circle_intersections.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Circles, Circle Relations, Intersections, Inscribed Circles and Circumcircles(2D)`  

---

## 1. Problem Statement & Key Idea
Given $N$ pieces of meat at coordinates $(x_i, y_i)$ with heat parameters $c_i$, cooking meat $i$ to level 1 takes time $c_i \cdot \text{dist}(P, (x_i, y_i))$. Placing a heat source at point $P$, cooking takes time $T$. The condition that meat $i$ is cooked in time $T$ is $c_i \cdot \text{dist}(P, (x_i, y_i)) \le T \iff \text{dist}(P, (x_i, y_i)) \le T / c_i$. That is, $P$ must lie inside the disk centered at $(x_i, y_i)$ with radius $R_i = T / c_i$. We must find the minimum $T$ such that some point $P$ is covered by at least $K$ disks.

## 2. Core Observation & Invariant
Binary search on time $T \in [0, 4 \times 10^5]$. For a fixed $T$, we have $N$ disks with radii $R_i = T / c_i$. An optimal point $P$ maximizing disk coverage can always be chosen either as one of the circle centers, or as an intersection point of the boundaries of two circles. With $N \le 60$, there are $O(N^2)$ candidate points. Testing coverage of all candidate points takes $O(N^3)$ per binary search step.

## 3. Step-by-Step Algorithm
1. 1. Binary search $T \in [0, 4 \times 10^5]$ for 80 iterations.
2. 2. For a candidate $T$, compute radii $R_i = T / c_i$.
3. 3. Candidate points $P$:
4.    a. All circle centers $(x_i, y_i)$.
5.    b. For every pair of circles $(i, j)$: if distance $d \le R_i + R_j$ and $d \ge |R_i - R_j|$, compute their two intersection points using standard trigonometry/vector geometry.
6. 4. For each candidate point $P$, count how many circles cover $P$ (with tolerance $\text{dist}(P, C_k) \le R_k + 10^{-9}$).
7. 5. If max coverage $\ge K$, set $high = T$; else set $low = T$.
8. 6. Output $T$ with high precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 \log(\text{range} / \epsilon))`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Meat {
    double x, y, c;
};

struct Point {
    double x, y;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<Meat> meats(n);
    for (int i = 0; i < n; ++i) {
        cin >> meats[i].x >> meats[i].y >> meats[i].c;
    }

    if (k == 1) {
        cout << fixed << setprecision(10) << 0.0 << "\n";
        return 0;
    }

    auto check = [&](double T) -> bool {
        vector<double> R(n);
        for (int i = 0; i < n; ++i) {
            R[i] = T / meats[i].c;
        }

        vector<Point> candidates;
        for (int i = 0; i < n; ++i) {
            candidates.push_back({meats[i].x, meats[i].y});
        }

        for (int i = 0; i < n; ++i) {
            double x1 = meats[i].x, y1 = meats[i].y, r1 = R[i];
            for (int j = i + 1; j < n; ++j) {
                double x2 = meats[j].x, y2 = meats[j].y, r2 = R[j];
                double dx = x2 - x1;
                double dy = y2 - y1;
                double d = hypot(dx, dy);
                if (d == 0 || d > r1 + r2 || d < abs(r1 - r2)) continue;

                double a = (r1 * r1 - r2 * r2 + d * d) / (2.0 * d);
                double h2 = r1 * r1 - a * a;
                if (h2 < 0) h2 = 0;
                double h = sqrt(h2);

                double p0x = x1 + a * dx / d;
                double p0y = y1 + a * dy / d;

                double rx = -dy / d;
                double ry = dx / d;

                candidates.push_back({p0x + h * rx, p0y + h * ry});
                if (h > 1e-9) {
                    candidates.push_back({p0x - h * rx, p0y - h * ry});
                }
            }
        }

        for (const auto& pt : candidates) {
            int cnt = 0;
            for (int i = 0; i < n; ++i) {
                double dist = hypot(pt.x - meats[i].x, pt.y - meats[i].y);
                if (meats[i].c * dist <= T + 1e-7) {
                    cnt++;
                }
            }
            if (cnt >= k) return true;
        }
        return false;
    };

    double low = 0.0, high = 400000.0;
    for (int iter = 0; iter < 60; ++iter) {
        double mid = (low + high) / 2.0;
        if (check(mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    cout << fixed << setprecision(10) << high << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
