# Problem Analysis: AtCoder-arc109_d — D. L

**Problem ID**: `AtCoder-arc109_d`  
**Contest**: `arc109`  
**Rating / Difficulty**: 2394  
**URL**: https://atcoder.jp/contests/arc109/tasks/arc109_d  
**VJudge Tag**: `[problem:AtCoder-arc109_d]`  
**Category File**: [`../categories/geometry/l_tromino_coordinate_transformation_chebyshev_distance.md`](../categories/geometry/l_tromino_coordinate_transformation_chebyshev_distance.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`  

---

## 1. Problem Statement & Key Idea
Summing coordinates uniquely identifies L-tromino configurations. A geometric transformation reduces moves to Chebyshev metric distance with parity adjustment on the diagonal, answering each testcase in O(1) time.

## 2. Core Observation & Invariant
Any L-tromino is uniquely characterized by the coordinate sum (X, Y) = (ax + bx + cx, ay + by + cy). Applying coordinate transformation x' = f(X) and y' = f(Y) maps the state space onto a grid where one stone move corresponds to Chebyshev distance with a parity correction: dist = max(|x'|, |y'|) + [x' == y'].

## 3. Step-by-Step Algorithm
1. Compute coordinate sums X = ax + bx + cx and Y = ay + by + cy.
2. Transform coordinates: x' = (X > 0 ? X - X/3 : X + (2 - X)/3) - 1, and similarly for y'.
3. Base cases: if x' == 0 and y' == 0 return 0; if x' == 1 and y' == 1 return 1.
4. General distance is max(|x'|, |y'|) + (x' == y') in O(1) time per testcase.

## 4. Complexity Analysis
- **Time Complexity**: `O(1) \text{ per testcase}`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll solve_case(ll x, ll y) {
    x = (x > 0 ? x - x / 3 : x + (2 - x) / 3) - 1;
    y = (y > 0 ? y - y / 3 : y + (2 - y) / 3) - 1;
    if (x == 0 && y == 0) return 0;
    if (x == 1 && y == 1) return 1;
    return max({x, -x, y, -y}) + (x == y);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    if (cin >> T) {
        while (T--) {
            ll ax, ay, bx, by, cx, cy;
            cin >> ax >> ay >> bx >> by >> cx >> cy;
            ll X = ax + bx + cx;
            ll Y = ay + by + cy;
            cout << solve_case(X, Y) << "\n";
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
