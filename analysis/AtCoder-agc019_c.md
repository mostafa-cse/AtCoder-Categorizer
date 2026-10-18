# Problem Analysis: AtCoder-agc019_c — C. Fountain Walk

**Problem ID**: `AtCoder-agc019_c`  
**Contest**: `agc019`  
**Rating / Difficulty**: 2495  
**URL**: https://atcoder.jp/contests/agc019/tasks/agc019_c  
**VJudge Tag**: `[problem:AtCoder-agc019_c]`  
**Category File**: [`../categories/dynamic_programming_dp/fountain_walk_quarter_circle_savings_lis.md`](../categories/dynamic_programming_dp/fountain_walk_quarter_circle_savings_lis.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Longest Increasing Subsequence (LIS)`  

---

## 1. Problem Statement & Key Idea
Find the shortest distance from $(x_1, y_1)$ to $(x_2, y_2)$ on a grid of roads where fountains of radius 10 occupy integer intersections. Walking along the circular circumference of a fountain saves $20 - 5\pi$ distance compared to walking around its bounding square, provided the path turns by 90 degrees around the quarter-circle. Within the bounding box $[x_1, x_2] \times [y_1, y_2]$, any monotone path that turns at fountains can utilize at most one fountain per $x$ and $y$ coordinate. Finding the maximum number of usable fountains is equivalent to finding the Longest Increasing Subsequence (LIS) of fountain coordinates.

## 2. Core Observation & Invariant
If the path can turn at $k$ fountains without forcing a U-turn, it saves $k \times (20 - 5\pi)$. If $k = \min(|x_2 - x_1|, |y_2 - y_1|) + 1$, the path is forced to pass through every row and column, meaning one fountain must be traversed via a semicircle (adding $10\pi - 20$) rather than a quarter-circle.

## 3. Step-by-Step Algorithm
1. 1. Normalize coordinates so $x_1 < x_2$ and $y_1 < y_2$ (flipping $y$ if necessary).
2. 2. Filter fountains that lie strictly inside the bounding box $[x_1, x_2] \times [y_1, y_2]$.
3. 3. Sort filtered fountains by $x$ ascending.
4. 4. Compute the LIS of their $y$-coordinates in $O(N \log N)$ using binary search (`std::lower_bound`).
5. 5. If $LIS = \min(x_2 - x_1, y_2 - y_1) + 1$, the optimal path touches all grid lines, requiring a half-circle adjustment.
6. 6. Compute final distance: $(x_2 - x_1 + y_2 - y_1) \times 100 - LIS \times (20 - 5\pi)$ (plus semicircle adjustment if applicable) with high-precision floating point.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

const double PI = acos(-1.0);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long x1, y1, x2, y2;
    if (!(cin >> x1 >> y1 >> x2 >> y2)) return 0;

    int n;
    cin >> n;

    if (x1 > x2) {
        swap(x1, x2);
        swap(y1, y2);
    }

    long long sign_y = (y1 <= y2 ? 1 : -1);
    long long ymin = min(y1, y2);
    long long ymax = max(y1, y2);

    vector<pair<long long, long long>> valid;
    valid.reserve(n);
    for (int i = 0; i < n; ++i) {
        long long x, y;
        cin >> x >> y;
        if (x1 <= x && x <= x2 && ymin <= y && y <= ymax) {
            valid.push_back({x, sign_y * y});
        }
    }

    sort(valid.begin(), valid.end(), [](const pair<long long, long long>& a, const pair<long long, long long>& b) {
        if (a.first != b.first) return a.first < b.first;
        return a.second > b.second;
    });

    vector<long long> tails;
    for (auto& p : valid) {
        long long y = p.second;
        auto it = lower_bound(tails.begin(), tails.end(), y);
        if (it == tails.end()) {
            tails.push_back(y);
        } else {
            *it = y;
        }
    }

    int K = tails.size();
    long long dx = x2 - x1;
    long long dy = abs(y2 - y1);

    double base = (dx + dy) * 100.0;
    double ans = 0;

    if (K == min(dx, dy) + 1) {
        ans = base - (K - 1) * (20.0 - 5.0 * PI) + (10.0 * PI - 20.0);
    } else {
        ans = base - K * (20.0 - 5.0 * PI);
    }

    cout << fixed << setprecision(15) << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
