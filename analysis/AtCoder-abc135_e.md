# Problem Analysis: AtCoder-abc135_e — Golf

**Problem ID**: `AtCoder-abc135_e`  
**Contest**: `abc135`  
**Rating / Difficulty**: 2665  
**URL**: https://atcoder.jp/contests/abc135/tasks/abc135_e  
**VJudge Tag**: `[problem:AtCoder-abc135_e]`  
**Category File**: [`../categories/basics/golf_manhattan_vector_steps.md`](../categories/basics/golf_manhattan_vector_steps.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Reach target coordinate (X, Y) in the minimum number of steps from (0, 0), where each step has Manhattan distance exactly K. The minimum number of steps n satisfies n * K >= |X| + |Y| and n * K = |X| + |Y| (mod 2). If K is even and |X| + |Y| is odd, it is impossible (-1). Otherwise, n steps are constructible by greedily aligning steps along the dominant axis and adjusting the overshoot via triangular adjustments.

## 2. Core Observation & Invariant
By symmetry, assume X, Y >= 0. In n steps of Manhattan length K, the total sum of step lengths is nK. The overshoot 2D = nK - (X + Y) must be non-negative and even. This overshoot 2D is compensated by making moves in the negative direction totaling D. For valid n, we allocate X and Y displacements into n vectors of Manhattan norm K.

## 3. Step-by-Step Algorithm
1. 1. Reflect X, Y to the first quadrant (X >= 0, Y >= 0) and track signs.
2. 2. Parity check: if K is even and X + Y is odd, output -1.
3. 3. Determine minimum n: start with n = ceil((X + Y) / K). Adjust n so that n * K = X + Y (mod 2) and handle boundary cases n=1, 2.
4. 4. Allocate x-steps and y-steps with positive displacement X + D and negative displacement D.
5. 5. Accumulate coordinates, restore original signs, and output n and the sequence of points.

## 4. Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>

using namespace std;

struct Point {
    long long x, y;
};

vector<Point> solve_2step(long long x0, long long y0, long long xt, long long yt, long long K) {
    long long dx = xt - x0;
    long long dy = yt - y0;
    long long sx = (dx < 0) ? -1 : 1;
    long long sy = (dy < 0) ? -1 : 1;
    long long Xp = llabs(dx);
    long long Yp = llabs(dy);
    long long Dp = Xp + Yp;

    long long mx, my;
    if (Xp >= Yp) {
        mx = Dp / 2;
        my = Dp / 2 - K;
    } else {
        mx = Dp / 2 - K;
        my = Dp / 2;
    }

    long long xmid = x0 + sx * mx;
    long long ymid = y0 + sy * my;
    return {{xmid, ymid}, {xt, yt}};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long K, X, Y;
    if (!(cin >> K >> X >> Y)) return 0;

    long long D = llabs(X) + llabs(Y);
    if (K % 2 == 0 && D % 2 != 0) {
        cout << -1 << "\n";
        return 0;
    }

    if (D == K) {
        cout << 1 << "\n";
        cout << X << " " << Y << "\n";
        return 0;
    }

    if (D < K) {
        if (D % 2 == 0) {
            auto pts = solve_2step(0, 0, X, Y, K);
            cout << 2 << "\n";
            for (auto& p : pts) {
                cout << p.x << " " << p.y << "\n";
            }
            return 0;
        } else {
            long long sx = (X < 0) ? -1 : 1;
            long long sy = (Y < 0) ? -1 : 1;
            long long x1 = sx * llabs(X);
            long long y1 = sy * (K - llabs(X));
            auto pts2 = solve_2step(x1, y1, X, Y, K);
            cout << 3 << "\n";
            cout << x1 << " " << y1 << "\n";
            for (auto& p : pts2) {
                cout << p.x << " " << p.y << "\n";
            }
            return 0;
        }
    }

    // D > K
    long long n = (D + K - 1) / K;
    if ((n * K) % 2 != D % 2) {
        n++;
    }

    long long sx = (X < 0) ? -1 : 1;
    long long sy = (Y < 0) ? -1 : 1;
    long long absX = llabs(X);
    long long absY = llabs(Y);

    long long cx = 0, cy = 0;
    vector<Point> pts;
    for (int i = 0; i < n - 2; ++i) {
        long long move_x = min(K, absX - cx);
        long long move_y = K - move_x;
        cx += move_x;
        cy += move_y;
        pts.push_back({sx * cx, sy * cy});
    }

    long long cur_x = pts.empty() ? 0 : pts.back().x;
    long long cur_y = pts.empty() ? 0 : pts.back().y;
    auto pts2 = solve_2step(cur_x, cur_y, X, Y, K);
    for (auto& p : pts2) {
        pts.push_back(p);
    }

    cout << pts.size() << "\n";
    for (auto& p : pts) {
        cout << p.x << " " << p.y << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
