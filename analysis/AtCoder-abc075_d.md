# Problem Analysis: AtCoder-abc075_d — Axis-Parallel Rectangle

**Problem ID**: `AtCoder-abc075_d`  
**Contest**: `abc075`  
**Rating / Difficulty**: 1470  
**URL**: https://atcoder.jp/contests/abc075/tasks/abc075_d  
**VJudge Tag**: `[problem:AtCoder-abc075_d]`  
**Category File**: [`../categories/basics/coordinate_selection_rectangle_search.md`](../categories/basics/coordinate_selection_rectangle_search.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Exhaustive Search`  
- **Topic (Skill)**: `2D Coordinate Selection O(N^4) Search for K Points`  

---

## 1. Problem Statement & Key Idea
Given N 2D points (N <= 50) and an integer K (2 <= K <= N). Find the minimum area of an axis-parallel rectangle containing at least K points on or inside its boundary.

**Key Insight**: The optimal rectangle has its four sides aligned with the coordinates of some subset of the given points. Enumerate all pairs of x-coordinates and all pairs of y-coordinates.

## 2. Core Observation & Invariant
There are at most N distinct x-coordinates and N distinct y-coordinates. Choosing 2 x-coordinates and 2 y-coordinates yields C(N, 2)^2 <= 1.5 * 10^6 rectangles. Testing each in O(N) takes ~ 7 * 10^7 operations.

## 3. Step-by-Step Algorithm
1. Store points (X[i], Y[i]).
2. Collect sorted unique x-coordinates and y-coordinates.
3. min_area = INF.
4. For each pair of x-bounds (x1, x2) with x1 < x2:
5.   For each pair of y-bounds (y1, y2) with y1 < y2:
6.     Count how many points (X[i], Y[i]) satisfy x1 <= X[i] <= x2 and y1 <= Y[i] <= y2.
7.     If count >= K, min_area = min(min_area, (x2 - x1) * (y2 - y1)).
8. Print min_area.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^5) with small constant, runs in < 0.2s`
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

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> x(n), y(n);
    vector<long long> x_vals, y_vals;

    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i];
        x_vals.push_back(x[i]);
        y_vals.push_back(y[i]);
    }

    sort(x_vals.begin(), x_vals.end());
    sort(y_vals.begin(), y_vals.end());

    unsigned long long min_area = ~0ULL;

    for (int xi = 0; xi < n; ++xi) {
        for (int xj = xi + 1; xj < n; ++xj) {
            long long x1 = x_vals[xi];
            long long x2 = x_vals[xj];

            for (int yi = 0; yi < n; ++yi) {
                for (int yj = yi + 1; yj < n; ++yj) {
                    long long y1 = y_vals[yi];
                    long long y2 = y_vals[yj];

                    int count = 0;
                    for (int p = 0; p < n; ++p) {
                        if (x[p] >= x1 && x[p] <= x2 && y[p] >= y1 && y[p] <= y2) {
                            count++;
                        }
                    }

                    if (count >= k) {
                        unsigned long long area = (unsigned long long)(x2 - x1) * (y2 - y1);
                        if (area < min_area) {
                            min_area = area;
                        }
                    }
                }
            }
        }
    }

    cout << min_area << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Coordinate compression boundary enumeration for optimal 2D enclosing regions.
- **Reusable Pattern**: `Minimal Bounding Box: test all pairs of existing x and y coordinates as candidates.`
