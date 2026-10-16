# Problem Analysis: AtCoder-abc189_e — Rotate and Flip

**Problem ID**: `AtCoder-abc189_e`  
**Contest**: `abc189`  
**Rating / Difficulty**: 1526  
**URL**: https://atcoder.jp/contests/abc189/tasks/abc189_e  
**VJudge Tag**: `[problem:AtCoder-abc189_e]`  
**Category File**: [`../categories/math/affine_transformation_composition.md`](../categories/math/affine_transformation_composition.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Linear Algebra`  
- **Topic (Skill)**: `2D Affine Transformation Matrix Composition`  

---

## 1. Problem Statement & Key Idea
N 2D points. M operations of 4 types: 1) clockwise 90 rotation; 2) counterclockwise 90 rotation; 3) reflection across x = p; 4) reflection across y = p. Answer Q queries: coordinates of point A after first B operations.

**Key Insight**: Every operation is a 2D affine transformation. Composition of any sequence of these transformations can be maintained in O(1) prefix table form as X' = sx * (orig_coord) + cx, Y' = sy * (orig_coord) + cy.

## 2. Core Observation & Invariant
At any step, either X' is an affine function of X and Y' is an affine function of Y, or the axes are swapped. Precomputing the affine matrix at every prefix step 0..M takes O(M). Each query is answered in O(1).

## 3. Step-by-Step Algorithm
1. Represent affine transformation as a 3x3 matrix or explicit (is_swapped, sx, sy, cx, cy).
2. Precompute state after operation step i = 0..M.
3. For each operation:
4.   Apply transformation to current representation in O(1).
5. For each query (A, B):
6.   Apply transformation state at step B to initial coordinates of point A.
7.   Print X' and Y'.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M + Q)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Affine {
    // x' = x_src == 0 ? sx * x + cx : sx * y + cx
    // y' = y_src == 1 ? sy * y + cy : sy * x + cy
    int x_src; // 0 for x, 1 for y
    int y_src; // 0 for x, 1 for y
    long long sx, sy;
    long long cx, cy;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> pts(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    int m;
    cin >> m;

    vector<Affine> pref(m + 1);
    pref[0] = {0, 1, 1, 1, 0, 0};

    for (int i = 1; i <= m; ++i) {
        int type;
        cin >> type;
        Affine prev = pref[i - 1];

        if (type == 1) {
            // (x, y) -> (y, -x)
            pref[i] = {prev.y_src, prev.x_src, prev.sy, -prev.sx, prev.cy, -prev.cx};
        } else if (type == 2) {
            // (x, y) -> (-y, x)
            pref[i] = {prev.y_src, prev.x_src, -prev.sy, prev.sx, -prev.cy, prev.cx};
        } else if (type == 3) {
            // (x, y) -> (2p - x, y)
            long long p;
            cin >> p;
            pref[i] = {prev.x_src, prev.y_src, -prev.sx, prev.sy, 2 * p - prev.cx, prev.cy};
        } else if (type == 4) {
            // (x, y) -> (x, 2p - y)
            long long p;
            cin >> p;
            pref[i] = {prev.x_src, prev.y_src, prev.sx, -prev.sy, prev.cx, 2 * p - prev.cy};
        }
    }

    int q;
    cin >> q;
    while (q--) {
        int b, a_idx;
        cin >> b >> a_idx;
        long long orig[2] = {pts[a_idx].first, pts[a_idx].second};
        Affine trans = pref[b];

        long long res_x = trans.sx * orig[trans.x_src] + trans.cx;
        long long res_y = trans.sy * orig[trans.y_src] + trans.cy;

        cout << res_x << " " << res_y << "\n";
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Prefix composition of 2D affine reflection/rotation transformations for O(1) evaluation.
- **Reusable Pattern**: `Affine Composition: compose linear map + translation vector prefix tables.`
