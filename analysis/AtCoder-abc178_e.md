# Problem Analysis: AtCoder-abc178_e — Dist Max

**Problem ID**: `AtCoder-abc178_e`  
**Contest**: `abc178`  
**Rating / Difficulty**: 1054  
**URL**: https://atcoder.jp/contests/abc178/tasks/abc178_e  
**VJudge Tag**: `[problem:AtCoder-abc178_e]`  
**Category File**: [`../categories/math/manhattan_coordinate_rotation_max.md`](../categories/math/manhattan_coordinate_rotation_max.md)  

- **Tag (Domain)**: `Math`  
- **Subtopic**: `Manhattan & Chebyshev`  
- **Topic (Skill)**: `45-degree Coordinate Rotation for Manhattan Maxima`  

---

## 1. Problem Statement & Key Idea
Given N points (x_i, y_i) in 2D plane (N <= 2 * 10^5). Find the maximum Manhattan distance |x_i - x_j| + |y_i - y_j| over all pairs.

**Key Idea**: Manhattan distance can be rewritten as max(|(x_i + y_i) - (x_j + y_j)|, |(x_i - y_i) - (x_j - y_j)|) via 45-degree coordinate rotation.

## 2. Core Observation & Invariant
Let u_i = x_i + y_i and v_i = x_i - y_i. Then Manhattan distance between point i and point j is max(|u_i - u_j|, |v_i - v_j|). The maximum distance over all pairs is max(max(u) - min(u), max(v) - min(v)), computable in a single pass O(N)!

## 3. Step-by-Step Algorithm
1. Compute u_i = x_i + y_i and v_i = x_i - y_i for all N points.
2. Find max_u, min_u, max_v, min_v.
3. Output max(max_u - min_u, max_v - min_v).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    long long max_u = -4e18, min_u = 4e18;
    long long max_v = -4e18, min_v = 4e18;

    for (int i = 0; i < n; ++i) {
        long long x, y;
        cin >> x >> y;
        long long u = x + y;
        long long v = x - y;
        max_u = max(max_u, u);
        min_u = min(min_u, u);
        max_v = max(max_v, v);
        min_v = min(min_v, v);
    }

    cout << max(max_u - min_u, max_v - min_v) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 45-degree coordinate rotation converting Manhattan distance to Chebyshev distance.
- **Reusable Pattern**: `Max Manhattan distance in 2D: max(max(x+y) - min(x+y), max(x-y) - min(x-y)).`
