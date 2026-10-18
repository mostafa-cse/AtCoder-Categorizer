# Problem Analysis: AtCoder-abc275_g — G. Infinite Knapsack

**Problem ID**: `AtCoder-abc275_g`  
**Contest**: `abc275`  
**Rating / Difficulty**: 2522  
**URL**: https://atcoder.jp/contests/abc275/tasks/abc275_g  
**VJudge Tag**: `[problem:AtCoder-abc275_g]`  
**Category File**: [`../categories/math/infinite_knapsack_convex_hull_lp.md`](../categories/math/infinite_knapsack_convex_hull_lp.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Mathematical Optimization`  
- **Topic (Skill)**: `Linear Programming / Simplex Algorithm`  

---

## 1. Problem Statement & Key Idea
Given items with values $A_i, B_i$ and costs $C_i$, find $\lim_{X \to \infty} f(X) / X$, where $f(X)$ is the minimum cost to achieve at least $X$ of both resources $A$ and $B$. In the asymptotic limit, this is a continuous linear program: minimize $\sum x_i C_i$ subject to $\sum x_i A_i \ge 1, \sum x_i B_i \ge 1, x_i \ge 0$. By duality, this is equivalent to finding the maximum of $\min(u, v)$ on the lower-left boundary of the convex hull of points $(C_i / A_i, C_i / B_i)$, or equivalently minimizing $\max(u, v)$ in the dual space.

## 2. Core Observation & Invariant
Each item $i$ can produce resource rates $u_i = A_i / C_i$ and $v_i = B_i / C_i$ per unit cost. We want to choose convex combinations of points $(u_i, v_i)$ in the 2D plane to maximize $\min(u, v)$. The optimal point is either an individual vertex $(u_i, v_i)$ (giving $\min(u_i, v_i)$), or the intersection of a segment between two hull vertices with the line $u = v$.

## 3. Step-by-Step Algorithm
1. 1. For each item $i$, convert to rates $P_i = (A_i / C_i, B_i / C_i)$.
2. 2. Sort points by $u_i$ ascending (and $v_i$ descending). Remove points dominated by others.
3. 3. Compute the upper-right convex hull of points using Graham scan / Monotone chain.
4. 4. For each vertex on the hull, evaluate $\min(u, v)$.
5. 5. For each adjacent pair of vertices on the hull $(u_1, v_1)$ and $(u_2, v_2)$, if they bracket the line $u = v$ (i.e. $(u_1 - v_1)(u_2 - v_2) \le 0$), compute the exact intersection with $u = v$ via linear interpolation: $t = \frac{v_1 - u_1}{(u_2 - u_1) - (v_2 - v_1)}$, rate $= u_1 + t(u_2 - u_1)$.
6. 6. Output the inverse of the maximum rate: $\text{ans} = 1.0 / \text{max\_rate}$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Point {
    double u, v;
    long long a, b, c;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    double ans = 0.0;
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].a >> pts[i].b >> pts[i].c;
        pts[i].u = (double)pts[i].a / pts[i].c;
        pts[i].v = (double)pts[i].b / pts[i].c;
        ans = max(ans, 1.0 / max(pts[i].u, pts[i].v));
    }

    sort(pts.begin(), pts.end(), [](const Point& p1, const Point& p2) {
        if (p1.u != p2.u) return p1.u < p2.u;
        return p1.v < p2.v;
    });

    vector<Point> filtered;
    for (const auto& p : pts) {
        if (filtered.empty() || p.v < filtered.back().v) {
            filtered.push_back(p);
        }
    }

    vector<Point> hull;
    for (const auto& p : filtered) {
        while (hull.size() >= 2) {
            const Point& p1 = hull[hull.size() - 2];
            const Point& p2 = hull.back();
            double cross = (p2.u - p1.u) * (p.v - p1.v) - (p2.v - p1.v) * (p.u - p1.u);
            if (cross <= 0) {
                hull.pop_back();
            } else {
                break;
            }
        }
        hull.push_back(p);
    }

    for (size_t i = 0; i + 1 < hull.size(); ++i) {
        const Point& p1 = hull[i];
        const Point& p2 = hull[i + 1];
        double diff1 = p1.v - p1.u;
        double diff2 = p2.v - p2.u;
        if ((diff1 >= 0 && diff2 <= 0) || (diff1 <= 0 && diff2 >= 0)) {
            double denom = diff1 - diff2;
            if (denom != 0) {
                double t = diff1 / denom;
                double u_val = (1.0 - t) * p1.u + t * p2.u;
                ans = max(ans, 1.0 / u_val);
            }
        }
    }

    cout << fixed << setprecision(16) << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
