# Problem Analysis: AtCoder-abc207_d — Congruence Points

**Problem ID**: `AtCoder-abc207_d`  
**Contest**: `abc207`  
**Rating / Difficulty**: 2074  
**URL**: https://atcoder.jp/contests/abc207/tasks/abc207_d  
**VJudge Tag**: `[problem:AtCoder-abc207_d]`  
**Category File**: [`../categories/geometry/point_set_congruence_centroid_rotation.md`](../categories/geometry/point_set_congruence_centroid_rotation.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`  

---

## 1. Problem Statement & Key Idea
You are given two sets of N points on a 2D plane, S and T. Determine if S can be made to coincide with T by translating and rotating S around the origin by some angle theta.

**Key Insight**: Translation invariance is eliminated by shifting both point sets so their centroids lie at the origin (scaling coordinates by N to retain exact integer arithmetic). Under rotation around the origin, Euclidean distance from the origin is preserved. To test rotational congruence, pick a non-origin anchor point in S, test aligning it with every candidate point in T having the identical squared norm. The rotation angle theta is uniquely determined by the dot and cross product of the two vectors, which allows rotating every point of S using integer arithmetic and testing set equality in O(N log N) via sorting.

## 2. Core Observation & Invariant
Aligning centroids removes the 2D translational degree of freedom. A 2D rotation preserving norm is uniquely fixed by mapping one non-zero vector to another.

## 3. Step-by-Step Algorithm
1. Compute centroid sums (sx, sy) and (tx, ty) for S and T.
2. Center both sets by setting (x, y) -> (N*x - sx, N*y - sy). If N == 1, trivially Yes.
3. Sort T to enable fast equality comparison.
4. Find an anchor point s0 in S that is non-zero (if none, all points are at origin, return Yes).
5. For each candidate point t in T with ||t||^2 == ||s0||^2:
6.   Compute cos_theta * ||s0||^2 = s0 . t and sin_theta * ||s0||^2 = s0 x t.
7.   Rotate each point s in S using the integer transformation matrix.
8.   If all coordinates remain integers and the sorted rotated set equals T, output Yes.
9. If no candidate works, output No.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 log N)`
- **Space Complexity**: `O(N)`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Centroid normalization to eliminate translation and exact integer matrix transformation for rotation verification.
- **Reusable Pattern**: For 2D point cloud matching, normalize by centroid and anchor one non-zero vector to test all O(N) candidate rotational alignments exactly without floating-point error.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
    bool operator<(const Point& o) const {
        if (x != o.x) return x < o.x;
        return y < o.y;
    }
    bool operator==(const Point& o) const {
        return x == o.x && y == o.y;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> S(n), T(n);
    long long sx = 0, sy = 0, tx = 0, ty = 0;
    for (int i = 0; i < n; ++i) {
        cin >> S[i].x >> S[i].y;
        sx += S[i].x;
        sy += S[i].y;
    }
    for (int i = 0; i < n; ++i) {
        cin >> T[i].x >> T[i].y;
        tx += T[i].x;
        ty += T[i].y;
    }

    if (n == 1) {
        cout << "Yes\n";
        return 0;
    }

    for (int i = 0; i < n; ++i) {
        S[i].x = S[i].x * n - sx;
        S[i].y = S[i].y * n - sy;
        T[i].x = T[i].x * n - tx;
        T[i].y = T[i].y * n - ty;
    }

    sort(T.begin(), T.end());

    int non_zero = -1;
    for (int i = 0; i < n; ++i) {
        if (S[i].x != 0 || S[i].y != 0) {
            non_zero = i;
            break;
        }
    }

    if (non_zero == -1) {
        cout << "Yes\n";
        return 0;
    }

    long long x0 = S[non_zero].x, y0 = S[non_zero].y;
    long long norm0 = x0 * x0 + y0 * y0;

    for (int j = 0; j < n; ++j) {
        long long xt = T[j].x, yt = T[j].y;
        if (xt * xt + yt * yt != norm0) continue;

        long long c = x0 * xt + y0 * yt;
        long long s = x0 * yt - y0 * xt;

        vector<Point> S_rot(n);
        bool ok = true;
        for (int i = 0; i < n; ++i) {
            long long rx = S[i].x * c - S[i].y * s;
            long long ry = S[i].x * s + S[i].y * c;
            if (rx % norm0 != 0 || ry % norm0 != 0) {
                ok = false;
                break;
            }
            S_rot[i] = {rx / norm0, ry / norm0};
        }
        if (!ok) continue;

        sort(S_rot.begin(), S_rot.end());
        if (S_rot == T) {
            cout << "Yes\n";
            return 0;
        }
    }

    cout << "No\n";
    return 0;
}
```
