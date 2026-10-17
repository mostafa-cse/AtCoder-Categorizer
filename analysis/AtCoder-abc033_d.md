# Problem Analysis: AtCoder-abc033_d — 三角形の分類

**Problem ID**: `AtCoder-abc033_d`  
**Contest**: `abc033`  
**Rating / Difficulty**: 2248  
**URL**: https://atcoder.jp/contests/abc033/tasks/abc033_d  
**VJudge Tag**: `[problem:AtCoder-abc033_d]`  
**Category File**: [`../categories/geometry/polar_sort_triangle_classification_sweep.md`](../categories/geometry/polar_sort_triangle_classification_sweep.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`  

---

## 1. Problem Statement & Key Idea
Count the number of acute, right, and obtuse triangles formed by N <= 2000 points in the plane with no three points collinear.

## 2. Core Observation & Invariant
Total triangles is C(N, 3). Each triangle has at most one right angle and at most one obtuse angle. Thus, counting right triangles and obtuse triangles reduces to counting pairs of vectors from a common pivot vertex that form an angle of exactly 90 degrees or > 90 degrees. For each point P_i, polar sorting the angles of all other N - 1 points allows finding right and obtuse angles in O(N log N) using two pointers.

## 3. Step-by-Step Algorithm
1. 1. Compute total triangles = N * (N - 1) * (N - 2) / 6.
2. 2. For each point i from 0 to N - 1:
3.    - Compute polar angle theta_j = atan2(y_j - y_i, x_j - x_i) for all j != i.
4.    - Sort the N - 1 angles and duplicate them with +2*PI to handle circular wrap-around.
5.    - Using two pointers, for each angle theta_j, find points with angle equal to theta_j + PI/2 (right angle) and angle in (theta_j + PI/2, theta_j + PI) (obtuse angle).
6. 3. Acute triangles = Total - Right - Obtuse. Output all three counts.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

const double PI = acos(-1.0);
const double EPS = 1e-10;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<double> x(n), y(n);
    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i];
    }

    long long total_tri = (long long)n * (n - 1) * (n - 2) / 6;
    long long right_cnt = 0;
    long long obtuse_cnt = 0;

    vector<double> angles;
    angles.reserve(2 * n);

    for (int i = 0; i < n; ++i) {
        angles.clear();
        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
            angles.push_back(atan2(y[j] - y[i], x[j] - x[i]));
        }
        sort(angles.begin(), angles.end());

        int m = angles.size();
        for (int j = 0; j < m; ++j) {
            angles.push_back(angles[j] + 2.0 * PI);
        }

        // For each angle j, find angles in [angles[j] + PI/2 - EPS, angles[j] + PI/2 + EPS]
        // and in (angles[j] + PI/2 + EPS, angles[j] + PI - EPS)
        int p1 = 0, p2 = 0, p3 = 0;
        for (int j = 0; j < m; ++j) {
            double target_right_low = angles[j] + PI / 2.0 - EPS;
            double target_right_high = angles[j] + PI / 2.0 + EPS;
            double target_pi = angles[j] + PI - EPS;

            while (p1 < 2 * m && angles[p1] < target_right_low) p1++;
            while (p2 < 2 * m && angles[p2] <= target_right_high) p2++;
            while (p3 < 2 * m && angles[p3] < target_pi) p3++;

            // [p1, p2) have angle == PI/2
            right_cnt += (p2 - p1);
            // [p2, p3) have angle in (PI/2, PI)
            obtuse_cnt += (p3 - p2);
        }
    }

    long long acute_cnt = total_tri - right_cnt - obtuse_cnt;

    cout << acute_cnt << " " << right_cnt << " " << obtuse_cnt << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
