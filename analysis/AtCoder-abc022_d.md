# Problem Analysis: AtCoder-abc022_d — Big Bang

**Problem ID**: `AtCoder-abc022_d`  
**Contest**: `abc022`  
**Rating / Difficulty**: 1857  
**URL**: https://atcoder.jp/contests/abc022/tasks/abc022_d  
**VJudge Tag**: `[problem:AtCoder-abc022_d]`  
**Category File**: [`../categories/geometry/centroid_invariant_similarity_scaling.md`](../categories/geometry/centroid_invariant_similarity_scaling.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Centroid Invariant`  
- **Topic (Skill)**: `Centroid Invariant Distance Ratio for 2D Similarity Transformations`  

---

## 1. Problem Statement & Key Idea
Given two sets of N points A and B in 2D. Set B is obtained from set A by translating, rotating, and scaling by a factor P. Find P.

**Key Insight**: Translation and rotation preserve distances from the centroid (center of mass). The scaling factor P scales the distance of every point from its respective centroid by exactly P. Thus, P = max_{i} dist(B_i, G_B) / max_{i} dist(A_i, G_A).

## 2. Core Observation & Invariant
Finding the centroids G_A and G_B takes O(N). Finding the maximum Euclidean distance to the centroid takes O(N).

## 3. Step-by-Step Algorithm
1. Compute centroid G_A = (sum X_A / N, sum Y_A / N).
2. Compute centroid G_B = (sum X_B / N, sum Y_B / N).
3. max_dist_A = max_i hypot(A_i.x - G_A.x, A_i.y - G_A.y).
4. max_dist_B = max_i hypot(B_i.x - G_B.x, B_i.y - G_B.y).
5. Print max_dist_B / max_dist_A with 12 decimal places.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> a(n), b(n);
    double sum_ax = 0, sum_ay = 0;
    for (int i = 0; i < n; ++i) {
        cin >> a[i].x >> a[i].y;
        sum_ax += a[i].x;
        sum_ay += a[i].y;
    }

    double sum_bx = 0, sum_by = 0;
    for (int i = 0; i < n; ++i) {
        cin >> b[i].x >> b[i].y;
        sum_bx += b[i].x;
        sum_by += b[i].y;
    }

    Point ga = {sum_ax / n, sum_ay / n};
    Point gb = {sum_bx / n, sum_by / n};

    double max_da = 0;
    for (int i = 0; i < n; ++i) {
        max_da = max(max_da, hypot(a[i].x - ga.x, a[i].y - ga.y));
    }

    double max_db = 0;
    for (int i = 0; i < n; ++i) {
        max_db = max(max_db, hypot(b[i].x - gb.x, b[i].y - gb.y));
    }

    cout << fixed << setprecision(12) << max_db / max_da << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Using center-of-mass invariants to factor out translations and rotations in geometric similarity checks.
- **Reusable Pattern**: `Centroid Distance Scaling: Scale factor P = max_dist(B, G_B) / max_dist(A, G_A).`
