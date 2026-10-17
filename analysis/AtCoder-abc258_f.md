# Problem Analysis: AtCoder-abc258_f — F. Main Street

**Problem ID**: `AtCoder-abc258_f`  
**Contest**: `abc258`  
**Rating / Difficulty**: 2306  
**URL**: https://atcoder.jp/contests/abc258/tasks/abc258_f  
**VJudge Tag**: `[problem:AtCoder-abc258_f]`  
**Category File**: [`../categories/graph_theory/grid_highway_projection_shortest_path.md`](../categories/graph_theory/grid_highway_projection_shortest_path.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra's Algorithm`  

---

## 1. Problem Statement & Key Idea
On an integer grid where lines $x = Bn$ and $y = Bn$ are highways (cost 1/unit) and other lines cost $K$/unit, find the minimum time to travel from $(S_x, S_y)$ to $(G_x, G_y)$.

## 2. Core Observation & Invariant
Any optimal trajectory between arbitrary grid points uses at most one entry and exit segment on regular streets to access the highway grid, projecting $S$ and $G$ onto their 4 bounding highway lines.

## 3. Step-by-Step Algorithm
1. Generate the 4 orthogonal projection points of $S$ onto adjacent highway grid lines $x = \lfloor S_x/B \rfloor B, \dots$ and similarly for $G$.
2. Compute shortest path distances along the regular highway grid between all $4 \times 4 = 16$ pairs of access points, taking detours into account if both points lie on the same cell boundary.
3. Take the minimum over all 16 highway paths and the direct regular street Manhattan distance.

## 4. Complexity Analysis
- **Time Complexity**: `O(T)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct AccessPoint {
    long long x, y;
    long long cost;
};

long long highway_dist(long long x1, long long y1, long long x2, long long y2, long long B) {
    bool v1 = (x1 % B == 0);
    bool h1 = (y1 % B == 0);
    bool v2 = (x2 % B == 0);
    bool h2 = (y2 % B == 0);

    if (v1 && v2) {
        if (x1 == x2) return abs(y1 - y2);
        long long min_y = min(y1, y2);
        long long max_y = max(y1, y2);
        long long next_B = (min_y / B) * B;
        if (next_B < min_y) next_B += B;
        if (next_B <= max_y) {
            return abs(x1 - x2) + abs(y1 - y2);
        } else {
            long long Y0 = (min_y / B) * B;
            long long Y1 = Y0 + B;
            long long d0 = (y1 - Y0) + (y2 - Y0);
            long long d1 = (Y1 - y1) + (Y1 - y2);
            return abs(x1 - x2) + min(d0, d1);
        }
    }

    if (h1 && h2) {
        if (y1 == y2) return abs(x1 - x2);
        long long min_x = min(x1, x2);
        long long max_x = max(x1, x2);
        long long next_B = (min_x / B) * B;
        if (next_B < min_x) next_B += B;
        if (next_B <= max_x) {
            return abs(x1 - x2) + abs(y1 - y2);
        } else {
            long long X0 = (min_x / B) * B;
            long long X1 = X0 + B;
            long long d0 = (x1 - X0) + (x2 - X0);
            long long d1 = (X1 - x1) + (X1 - x2);
            return abs(y1 - y2) + min(d0, d1);
        }
    }

    return abs(x1 - x2) + abs(y1 - y2);
}

void solve() {
    long long B, K, Sx, Sy, Gx, Gy;
    cin >> B >> K >> Sx >> Sy >> Gx >> Gy;

    long long ans = K * (abs(Sx - Gx) + abs(Sy - Gy));

    vector<AccessPoint> pts_S;
    long long xL = (Sx / B) * B;
    long long xR = xL + B;
    long long yD = (Sy / B) * B;
    long long yU = yD + B;

    pts_S.push_back({xL, Sy, K * abs(Sx - xL)});
    pts_S.push_back({xR, Sy, K * abs(Sx - xR)});
    pts_S.push_back({Sx, yD, K * abs(Sy - yD)});
    pts_S.push_back({Sx, yU, K * abs(Sy - yU)});

    vector<AccessPoint> pts_G;
    long long gxL = (Gx / B) * B;
    long long gxR = gxL + B;
    long long gyD = (Gy / B) * B;
    long long gyU = gyD + B;

    pts_G.push_back({gxL, Gy, K * abs(Gx - gxL)});
    pts_G.push_back({gxR, Gy, K * abs(Gx - gxR)});
    pts_G.push_back({Gx, gyD, K * abs(Gy - gyD)});
    pts_G.push_back({Gx, gyU, K * abs(Gy - gyU)});

    for (const auto& ps : pts_S) {
        for (const auto& pg : pts_G) {
            long long cur = ps.cost + pg.cost + highway_dist(ps.x, ps.y, pg.x, pg.y, B);
            ans = min(ans, cur);
        }
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
