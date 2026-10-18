# Problem Analysis: AtCoder-abc286_h — Ex. Don't Swim

**Problem ID**: `AtCoder-abc286_h`  
**Contest**: `abc286`  
**Rating / Difficulty**: 2526  
**URL**: https://atcoder.jp/contests/abc286/tasks/abc286_h  
**VJudge Tag**: `[problem:AtCoder-abc286_h]`  
**Category File**: [`../categories/geometry/dont_swim_tangents_convex_polygon.md`](../categories/geometry/dont_swim_tangents_convex_polygon.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Tangents from Point to Convex and Convex to Convex(2D)`  

---

## 1. Problem Statement & Key Idea
Find the shortest path between $S$ and $T$ in 2D that does not enter the strict interior of a strictly convex polygon with $N$ vertices. If the straight line segment $ST$ does not intersect the polygon interior, the answer is simply the Euclidean distance $|ST|$. Otherwise, the shortest path must follow a tangent line from $S$ to some polygon vertex $V_i$, travel along the polygon perimeter, and leave via a tangent line from some polygon vertex $V_j$ to $T$.

## 2. Core Observation & Invariant
Because the obstacle is a convex polygon, shortest paths that touch the obstacle must follow the boundary in either clockwise or counter-clockwise orientation between tangent points. For any external point $P$, there are exactly two tangent vertices to the convex polygon, found by finding the vertices that achieve the extreme cross-products (orientations) with respect to $P$. Connecting $S$'s tangents to $T$'s tangents along both perimeter paths yields at most 4 candidate routes.

## 3. Step-by-Step Algorithm
1. 1. Check if line segment $ST$ intersects the convex polygon interior:
2.    - Check if $ST$ intersects any polygon edge properly, or if midpoint of $ST$ is strictly inside polygon. If no intersection, output Euclidean distance $|ST|$.
3. 2. Find the two tangent vertices from $S$ to the polygon, $s_1$ and $s_2$, by checking sign changes of cross-products of vectors from $S$ to consecutive vertices.
4. 3. Find the two tangent vertices from $T$ to the polygon, $t_1$ and $t_2$, similarly.
5. 4. For each tangent vertex pair $(u, v)$ where $u \in \{s_1, s_2\}$ and $v \in \{t_1, t_2\}$:
6.    - Compute the perimeter distance from $u$ to $v$ moving clockwise and counter-clockwise along polygon edges.
7.    - Add $|S - u| + |T - v| + \text{perimeter\_dist}$.
8. 5. Output the minimum total distance among all valid obstacle-avoiding paths.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
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

double cross(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

double dist(Point a, Point b) {
    return hypot(a.x - b.x, a.y - b.y);
}

bool seg_intersect_strict(Point p1, Point p2, Point p3, Point p4) {
    double d1 = cross(p3, p4, p1);
    double d2 = cross(p3, p4, p2);
    double d3 = cross(p1, p2, p3);
    double d4 = cross(p1, p2, p4);
    if (((d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0)) &&
        ((d3 > 0 && d4 < 0) || (d3 < 0 && d4 > 0))) {
        return true;
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> poly(n);
    for (int i = 0; i < n; ++i) {
        cin >> poly[i].x >> poly[i].y;
    }

    Point S, T;
    cin >> S.x >> S.y >> T.x >> T.y;

    bool blocked = false;
    for (int i = 0; i < n; ++i) {
        if (seg_intersect_strict(S, T, poly[i], poly[(i + 1) % n])) {
            blocked = true;
            break;
        }
    }

    if (!blocked) {
        cout << fixed << setprecision(16) << dist(S, T) << "\n";
        return 0;
    }

    auto get_tangents = [&](Point P) -> pair<int, int> {
        int t1 = -1, t2 = -1;
        for (int i = 0; i < n; ++i) {
            int prev_i = (i - 1 + n) % n;
            int next_i = (i + 1) % n;
            double c_prev = cross(P, poly[i], poly[prev_i]);
            double c_next = cross(P, poly[i], poly[next_i]);
            if (c_prev >= 0 && c_next >= 0) t1 = i;
            if (c_prev <= 0 && c_next <= 0) t2 = i;
        }
        return {t1, t2};
    };

    auto [s1, s2] = get_tangents(S);
    auto [t1, t2] = get_tangents(T);

    vector<double> edge_len(n);
    double total_perim = 0;
    for (int i = 0; i < n; ++i) {
        edge_len[i] = dist(poly[i], poly[(i + 1) % n]);
        total_perim += edge_len[i];
    }

    vector<double> pref(n + 1, 0.0);
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + edge_len[i];
    }

    auto perim_dist = [&](int u, int v, int dir) -> double {
        if (dir == 1) {
            if (v >= u) return pref[v] - pref[u];
            return total_perim - (pref[u] - pref[v]);
        } else {
            if (u >= v) return pref[u] - pref[v];
            return total_perim - (pref[v] - pref[u]);
        }
    };

    double ans = 1e18;
    vector<int> s_cands = {s1, s2};
    vector<int> t_cands = {t1, t2};

    for (int u : s_cands) {
        if (u == -1) continue;
        for (int v : t_cands) {
            if (v == -1) continue;
            for (int d : {1, -1}) {
                int next_u = (u + d + n) % n;
                if (cross(S, poly[u], poly[next_u]) * d < -1e-9) continue;
                int prev_v = (v - d + n) % n;
                if (cross(poly[prev_v], poly[v], T) * d < -1e-9) continue;

                double d_val = dist(S, poly[u]) + perim_dist(u, v, d) + dist(poly[v], T);
                ans = min(ans, d_val);
            }
        }
    }

    cout << fixed << setprecision(16) << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
