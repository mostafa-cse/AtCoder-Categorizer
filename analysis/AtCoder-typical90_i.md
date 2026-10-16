# Problem Analysis: AtCoder-typical90_i — Three Point Angle

**Problem ID**: `AtCoder-typical90_i`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 009)  
**Rating / Difficulty**: 2100 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_i  
**VJudge Tag**: `[problem:AtCoder-typical90_i]`  
**Category File**: [`../categories/geometry/polar_angle_sort.md`](../categories/geometry/polar_angle_sort.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Angular Sweep / Polar Angles`  
- **Topic (Skill)**: `Polar Angle Sort + Binary Search for Opposite Vector`  

---

## 1. Problem Statement & Key Idea
Given N points in 2D plane (N <= 2000), choose three distinct points p_j, p_i, p_k to maximize the angle between vectors (p_j - p_i) and (p_k - p_i). Output maximum angle in degrees.

**Core Idea**: Fix the central vertex p_i (N choices). Compute the polar angle of all other N-1 points with respect to p_i.

## 2. Core Observation & Invariant
Sort polar angles in [0, 360). For any angle theta_j, the optimal opposite angle is closest to (theta_j + 180). Use std::lower_bound to find the closest angles in O(log N).

## 3. Step-by-Step Algorithm
1. Iterate each point i as pivot.
2. Calculate angles theta = atan2(y - y_i, x - x_i) * 180 / PI in [0, 360).
3. Sort angles array.
4. For each angle t: binary search for (t + 180) % 360; check adjacent candidates and update max angle.
5. Return global max.

## 4. Complexity Analysis
Time: O(N^2 log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

const double PI = acos(-1.0);

double get_diff(double a, double b) {
    double d = abs(a - b);
    if (d > 180.0) d = 360.0 - d;
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<double, double>> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    double max_angle = 0.0;

    for (int i = 0; i < n; ++i) {
        vector<double> angles;
        angles.reserve(n - 1);
        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
            double deg = atan2(pts[j].second - pts[i].second, pts[j].first - pts[i].first) * 180.0 / PI;
            if (deg < 0) deg += 360.0;
            angles.push_back(deg);
        }
        sort(angles.begin(), angles.end());

        int m = angles.size();
        for (int j = 0; j < m; ++j) {
            double target = angles[j] + 180.0;
            if (target >= 360.0) target -= 360.0;

            auto it = lower_bound(angles.begin(), angles.end(), target);
            int idx = it - angles.begin();

            for (int offset : {-1, 0, 1}) {
                int cand = (idx + offset + m) % m;
                max_angle = max(max_angle, get_diff(angles[j], angles[cand]));
            }
        }
    }

    cout << fixed << setprecision(10) << max_angle << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Polar angle sorting and binary searching target opposite rays.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Polar coordinate transformations, atan2 angle sorting, and binary searching for antipodal vectors.
- **Reusable Pattern**: `Polar Angle Sort + Binary Search for Opposite Vector.`

---
Back to [Polar Angle Sort + Binary Search for Opposite Vector](../categories/geometry/polar_angle_sort.md) | [Categories Directory](../categories/README.md)