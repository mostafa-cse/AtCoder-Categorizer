# Problem Analysis: AtCoder-typical90_aj — Max Manhattan Distance

**Problem ID**: `AtCoder-typical90_aj`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 036)  
**Rating / Difficulty**: 1600 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_aj  
**VJudge Tag**: `[problem:AtCoder-typical90_aj]`  
**Category File**: [`../categories/math/coordinate_rotation.md`](../categories/math/coordinate_rotation.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Coordinate Geometry & Metrics`  
- **Topic (Skill)**: `45-Degree Coordinate Rotation / Manhattan to Chebyshev Distance Transformation`  

---

## 1. Problem Statement & Key Idea
Given N points (x_i, y_i), answer Q queries: for point q, find max Manhattan distance |x_q - x_j| + |y_q - y_j| to any point j.

**Core Idea**: Rotate coordinates by 45 degrees: (X, Y) = (x + y, x - y). Manhattan distance transforms into Chebyshev distance: max(|X_1 - X_2|, |Y_1 - Y_2|).

## 2. Core Observation & Invariant
After transforming, max Chebyshev distance from (X_q, Y_q) is max(|X_q - min X|, |X_q - max X|, |Y_q - min Y|, |Y_q - max Y|), which evaluates in O(1)!

## 3. Step-by-Step Algorithm
1. For each point i: X_i = x_i + y_i, Y_i = x_i - y_i.
2. Find min_X, max_X, min_Y, max_Y over all N points.
3. For each query q: output max({|X_q - min_X|, |X_q - max_X|, |Y_q - min_Y|, |Y_q - max_Y|}).

## 4. Complexity Analysis
Time: O(N + Q), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> X(n), Y(n);
    long long min_X = 4e18, max_X = -4e18;
    long long min_Y = 4e18, max_Y = -4e18;

    for (int i = 0; i < n; ++i) {
        long long x, y;
        cin >> x >> y;
        X[i] = x + y;
        Y[i] = x - y;
        min_X = min(min_X, X[i]);
        max_X = max(max_X, X[i]);
        min_Y = min(min_Y, Y[i]);
        max_Y = max(max_Y, Y[i]);
    }

    while (q--) {
        int idx;
        cin >> idx;
        --idx;
        long long qx = X[idx], qy = Y[idx];
        long long ans = max({abs(qx - min_X), abs(qx - max_X),
                             abs(qy - min_Y), abs(qy - max_Y)});
        cout << ans << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
45-degree rotation converting Manhattan metric to Chebyshev metric.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Transforming coupled L1 distance dimensions into independent L_infinity coordinate extremes.
- **Reusable Pattern**: `45-Degree Coordinate Rotation (Manhattan to Chebyshev).`

---
Back to [45-Degree Coordinate Rotation / Manhattan to Chebyshev Distance Transformation](../categories/math/coordinate_rotation.md) | [Categories Directory](../categories/README.md)