# Problem Analysis: AtCoder-abc130_f — Minimum Bounding Box

**Problem ID**: `AtCoder-abc130_f`  
**Contest**: `abc130`  
**Rating / Difficulty**: 2240  
**URL**: https://atcoder.jp/contests/abc130/tasks/abc130_f  
**VJudge Tag**: `[problem:AtCoder-abc130_f]`  
**Category File**: [`../categories/miscellaneous/ternary_search_minimum_bounding_box_envelope.md`](../categories/miscellaneous/ternary_search_minimum_bounding_box_envelope.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Search Techniques`  
- **Topic (Skill)**: `Ternary Search`  

---

## 1. Problem Statement & Key Idea
Find the minimum bounding box area (x_max - x_min) * (y_max - y_min) over all times t >= 0 for N points moving at unit speed in orthogonal directions.

## 2. Core Observation & Invariant
For each coordinate axis, points move with velocity +1, -1, or 0. The maximum coordinate x_max(t) is the upper envelope of at most 3 linear functions, and x_min(t) is the lower envelope of at most 3 linear functions. Thus, X(t) = x_max(t) - x_min(t) is a convex piecewise linear function with at most 6 slope changes. The same holds for Y(t). The product f(t) = X(t) * Y(t) is piecewise quadratic on each interval between breakpoints. The minimum can only occur at t = 0, at breakpoints where envelope lines intersect, or at the vertex of a convex quadratic segment, which can be found via ternary search on each interval.

## 3. Step-by-Step Algorithm
1. 1. Group points by their velocity in X and Y into R, L, S (stationary) for X, and U, D, S for Y.
2. 2. Compute candidate inflection times t >= 0 where lines in x_max, x_min, y_max, y_min intersect.
3. 3. Add t = 0 to candidate times, sort and remove duplicates.
4. 4. For each interval [t_k, t_{k+1}], evaluate f(t) at the endpoints and perform continuous ternary search within the interval to locate any quadratic interior minimum.
5. 5. Output the global minimum area with high floating-point precision.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + K log(1/eps)) where K <= 15 intervals`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

const double INF = 1e18;

struct Group {
    double min_val = INF;
    double max_val = -INF;
    void add(double v) {
        min_val = min(min_val, v);
        max_val = max(max_val, v);
    }
    bool empty() const {
        return min_val > max_val;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    Group xR, xL, xS;
    Group yU, yD, yS;

    for (int i = 0; i < n; ++i) {
        double x, y;
        char d;
        cin >> x >> y >> d;
        if (d == 'R') {
            xR.add(x);
            yS.add(y);
        } else if (d == 'L') {
            xL.add(x);
            yS.add(y);
        } else if (d == 'U') {
            xS.add(x);
            yU.add(y);
        } else if (d == 'D') {
            xS.add(x);
            yD.add(y);
        }
    }

    auto get_eval = [&](double t) {
        double x_max = -INF, x_min = INF;
        if (!xR.empty()) {
            x_max = max(x_max, xR.max_val + t);
            x_min = min(x_min, xR.min_val + t);
        }
        if (!xL.empty()) {
            x_max = max(x_max, xL.max_val - t);
            x_min = min(x_min, xL.min_val - t);
        }
        if (!xS.empty()) {
            x_max = max(x_max, xS.max_val);
            x_min = min(x_min, xS.min_val);
        }

        double y_max = -INF, y_min = INF;
        if (!yU.empty()) {
            y_max = max(y_max, yU.max_val + t);
            y_min = min(y_min, yU.min_val + t);
        }
        if (!yD.empty()) {
            y_max = max(y_max, yD.max_val - t);
            y_min = min(y_min, yD.min_val - t);
        }
        if (!yS.empty()) {
            y_max = max(y_max, yS.max_val);
            y_min = min(y_min, yS.min_val);
        }

        return (x_max - x_min) * (y_max - y_min);
    };

    vector<double> candidate_t = {0.0};

    auto add_cross = [&](double v1, double s1, double v2, double s2) {
        if (s1 == s2) return;
        // v1 + s1 * t = v2 + s2 * t => (s1 - s2) * t = v2 - v1
        double t = (v2 - v1) / (s1 - s2);
        if (t >= 0.0) {
            candidate_t.push_back(t);
        }
    };

    // For x_max: lines are xR.max + t, xL.max - t, xS.max
    if (!xR.empty() && !xL.empty()) add_cross(xR.max_val, 1, xL.max_val, -1);
    if (!xR.empty() && !xS.empty()) add_cross(xR.max_val, 1, xS.max_val, 0);
    if (!xL.empty() && !xS.empty()) add_cross(xL.max_val, -1, xS.max_val, 0);

    // For x_min: lines are xR.min + t, xL.min - t, xS.min
    if (!xR.empty() && !xL.empty()) add_cross(xR.min_val, 1, xL.min_val, -1);
    if (!xR.empty() && !xS.empty()) add_cross(xR.min_val, 1, xS.min_val, 0);
    if (!xL.empty() && !xS.empty()) add_cross(xL.min_val, -1, xS.min_val, 0);

    // For y_max: lines are yU.max + t, yD.max - t, yS.max
    if (!yU.empty() && !yD.empty()) add_cross(yU.max_val, 1, yD.max_val, -1);
    if (!yU.empty() && !yS.empty()) add_cross(yU.max_val, 1, yS.max_val, 0);
    if (!yD.empty() && !yS.empty()) add_cross(yD.max_val, -1, yS.max_val, 0);

    // For y_min: lines are yU.min + t, yD.min - t, yS.min
    if (!yU.empty() && !yD.empty()) add_cross(yU.min_val, 1, yD.min_val, -1);
    if (!yU.empty() && !yS.empty()) add_cross(yU.min_val, 1, yS.min_val, 0);
    if (!yD.empty() && !yS.empty()) add_cross(yD.min_val, -1, yS.min_val, 0);

    sort(candidate_t.begin(), candidate_t.end());
    candidate_t.erase(unique(candidate_t.begin(), candidate_t.end()), candidate_t.end());

    double ans = get_eval(0.0);

    for (size_t i = 0; i < candidate_t.size(); ++i) {
        double t1 = candidate_t[i];
        ans = min(ans, get_eval(t1));

        double t2 = (i + 1 < candidate_t.size()) ? candidate_t[i + 1] : (t1 + 1e9);

        // Within [t1, t2], perform ternary search or evaluate vertex of quadratic
        // Ternary search is very robust on this interval
        double left = t1, right = min(t2, t1 + 1e9);
        for (int iter = 0; iter < 80; ++iter) {
            double m1 = left + (right - left) / 3.0;
            double m2 = right - (right - left) / 3.0;
            double e1 = get_eval(m1);
            double e2 = get_eval(m2);
            if (e1 < e2) {
                right = m2;
            } else {
                left = m1;
            }
        }
        ans = min(ans, get_eval(left));
    }

    cout << fixed << setprecision(10) << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
