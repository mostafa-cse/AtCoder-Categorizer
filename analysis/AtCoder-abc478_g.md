# Problem Analysis: AtCoder-abc478_g — G. Division Point Hull

**Problem ID**: `AtCoder-abc478_g`  
**Contest**: `abc478`  
**Rating / Difficulty**: 2582  
**URL**: https://atcoder.jp/contests/abc478/tasks/abc478_g  
**VJudge Tag**: `[problem:AtCoder-abc478_g]`  
**Category File**: [`../categories/geometry/division_point_hull_minkowski_sum.md`](../categories/geometry/division_point_hull_minkowski_sum.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Convex Polygon`  
- **Topic (Skill)**: `Minkowski Sum`  

---

## 1. Problem Statement & Key Idea
Given N points P_1, ..., P_N and ratio p : q, each pair (i, j) with 1 <= i < j <= N generates a division point Q_{i,j} = (q * P_i + p * P_j) / (p + q). Find the area of the convex hull of all Q_{i,j}.

## 2. Core Observation & Invariant
The set of all division points Q[l, r) on an interval [l, r) with midpoint m satisfies Q[l, r) = Q[l, m) U Q[m, r) U (q/(p+q) * P[l, m) + p/(p+q) * P[m, r)). Taking convex hulls on both sides: conv(Q[l, r)) = conv(conv(Q[l, m)) U conv(Q[m, r)) U (q * conv(P[l, m)) + p * conv(P[m, r)))). The Minkowski sum of two convex polygons of sizes A and B has size at most A + B and can be computed in linear time O(A + B) by merging edge vectors by polar angle. Across all levels of the divide-and-conquer tree, the total vertices processed is O(N log N), yielding an O(N log^2 N) algorithm.

## 3. Step-by-Step Algorithm
1. Scale coordinates by (p + q) so all points are integers: Q'_{i,j} = q * P_i + p * P_j.
2. Define recursive function solve_dc(l, r) returning {conv(P[l, r)), conv(Q[l, r))}.
3. At base case r - l = 1: return {{P[l]}, {}}.
4. For r - l > 1: recursively solve left and right halves.
5. Compute Minkowski sum M = q * left.ch_P + p * right.ch_P by merging edge vectors in polar angle order.
6. Combine left.ch_P U right.ch_P into new ch_P via Monotone Chain convex hull.
7. Combine left.ch_Q U right.ch_Q U M into new ch_Q via Monotone Chain convex hull.
8. At root: compute 2 * Area of conv(Q[0, N)) via Shoelace formula, and divide by 2 * (p + q)^2 in lowest terms using gcd.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log^2 N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

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
    Point operator+(const Point& o) const {
        return {x + o.x, y + o.y};
    }
    Point operator-(const Point& o) const {
        return {x - o.x, y - o.y};
    }
};

long long cross_prod(const Point& o, const Point& a, const Point& b) {
    __int128 v = (__int128)(a.x - o.x) * (b.y - o.y) - (__int128)(a.y - o.y) * (b.x - o.x);
    if (v > 0) return 1;
    if (v < 0) return -1;
    return 0;
}

vector<Point> get_convex_hull(vector<Point>& pts) {
    if (pts.size() <= 1) return pts;
    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    if (pts.size() <= 1) return pts;

    vector<Point> lower, upper;
    for (const auto& p : pts) {
        while (lower.size() >= 2 && cross_prod(lower[lower.size() - 2], lower.back(), p) <= 0) {
            lower.pop_back();
        }
        lower.push_back(p);
    }
    for (int i = (int)pts.size() - 1; i >= 0; i--) {
        const auto& p = pts[i];
        while (upper.size() >= 2 && cross_prod(upper[upper.size() - 2], upper.back(), p) <= 0) {
            upper.pop_back();
        }
        upper.push_back(p);
    }
    lower.pop_back();
    upper.pop_back();
    lower.insert(lower.end(), upper.begin(), upper.end());
    return lower;
}

// Minkowski sum of two convex hulls A and B
vector<Point> minkowski_sum(vector<Point>& A, vector<Point>& B) {
    if (A.empty() || B.empty()) return {};
    if (A.size() <= 2 || B.size() <= 2) {
        vector<Point> pts;
        pts.reserve(A.size() * B.size());
        for (const auto& a : A) {
            for (const auto& b : B) {
                pts.push_back(a + b);
            }
        }
        return get_convex_hull(pts);
    }

    // Both sizes >= 3
    // Find bottom-leftmost vertex in each
    int posA = 0, posB = 0;
    for (size_t i = 1; i < A.size(); i++) {
        if (A[i].y < A[posA].y || (A[i].y == A[posA].y && A[i].x < A[posA].x)) posA = i;
    }
    for (size_t i = 1; i < B.size(); i++) {
        if (B[i].y < B[posB].y || (B[i].y == B[posB].y && B[i].x < B[posB].x)) posB = i;
    }
    rotate(A.begin(), A.begin() + posA, A.end());
    rotate(B.begin(), B.begin() + posB, B.end());

    int n = A.size(), m = B.size();
    vector<Point> res;
    res.reserve(n + m + 5);
    int i = 0, j = 0;
    while (i < n || j < m) {
        res.push_back(A[i % n] + B[j % m]);
        if (i == n) {
            j++;
        } else if (j == m) {
            i++;
        } else {
            Point da = A[(i + 1) % n] - A[i % n];
            Point db = B[(j + 1) % m] - B[j % m];
            __int128 cp = (__int128)da.x * db.y - (__int128)da.y * db.x;
            if (cp > 0) {
                i++;
            } else if (cp < 0) {
                j++;
            } else {
                i++;
                j++;
            }
        }
    }
    return get_convex_hull(res);
}

int N;
long long P_scale, Q_scale;
vector<Point> P;

struct Result {
    vector<Point> ch_P;
    vector<Point> ch_Q;
};

Result solve_dc(int l, int r) {
    if (r - l == 1) {
        return {{P[l]}, {}};
    }
    int mid = (l + r) / 2;
    Result left_res = solve_dc(l, mid);
    Result right_res = solve_dc(mid, r);

    // Minkowski sum of Q_scale * left_res.ch_P and P_scale * right_res.ch_P
    vector<Point> scaled_A = left_res.ch_P;
    for (auto& pt : scaled_A) {
        pt.x *= Q_scale;
        pt.y *= Q_scale;
    }
    vector<Point> scaled_B = right_res.ch_P;
    for (auto& pt : scaled_B) {
        pt.x *= P_scale;
        pt.y *= P_scale;
    }
    vector<Point> M = minkowski_sum(scaled_A, scaled_B);

    // Combine ch_P
    vector<Point> all_P;
    all_P.reserve(left_res.ch_P.size() + right_res.ch_P.size());
    all_P.insert(all_P.end(), left_res.ch_P.begin(), left_res.ch_P.end());
    all_P.insert(all_P.end(), right_res.ch_P.begin(), right_res.ch_P.end());
    vector<Point> combined_ch_P = get_convex_hull(all_P);

    // Combine ch_Q
    vector<Point> all_Q;
    all_Q.reserve(left_res.ch_Q.size() + right_res.ch_Q.size() + M.size());
    all_Q.insert(all_Q.end(), left_res.ch_Q.begin(), left_res.ch_Q.end());
    all_Q.insert(all_Q.end(), right_res.ch_Q.begin(), right_res.ch_Q.end());
    all_Q.insert(all_Q.end(), M.begin(), M.end());
    vector<Point> combined_ch_Q = get_convex_hull(all_Q);

    return {combined_ch_P, combined_ch_Q};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> N >> P_scale >> Q_scale)) return 0;
    P.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> P[i].x >> P[i].y;
    }

    Result res = solve_dc(0, N);
    const vector<Point>& hull = res.ch_Q;

    if (hull.size() < 3) {
        cout << "0 1\n";
        return 0;
    }

    __int128 area2 = 0;
    int k = hull.size();
    for (int i = 0; i < k; i++) {
        int j = (i + 1) % k;
        area2 += (__int128)hull[i].x * hull[j].y - (__int128)hull[j].x * hull[i].y;
    }
    if (area2 < 0) area2 = -area2;

    long long denom = 2LL * (P_scale + Q_scale) * (P_scale + Q_scale);
    long long num = (long long)area2;
    long long g = std::gcd(num, denom);
    cout << (num / g) << " " << (denom / g) << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
