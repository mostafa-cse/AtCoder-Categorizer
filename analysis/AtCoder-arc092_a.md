# Problem Analysis: AtCoder-arc092_a — 2D Plane 2N Points

**Problem ID**: `AtCoder-arc092_a`  
**Contest**: `abc091`  
**Rating / Difficulty**: 1268  
**URL**: https://atcoder.jp/contests/abc091/tasks/arc092_a  
**VJudge Tag**: `[problem:AtCoder-arc092_a]`  
**Category File**: [`../categories/graph_theory/bipartite_matching_sweepline.md`](../categories/graph_theory/bipartite_matching_sweepline.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Bipartite Matching`  
- **Topic (Skill)**: `Bipartite Matching / Greedy Sweepline on 2D Coordinates`  

---

## 1. Problem Statement & Key Idea
N red points (a_i, b_i) and N blue points (c_i, d_i). A red point can be paired with a blue point if a_i < c_j and b_i < d_j. Maximize the number of disjoint pairs (N <= 100).

**Key Idea**: Sort blue points by x-coordinate in ascending order. Process blue points from left to right.

## 2. Core Observation & Invariant
For a blue point (c, d), any red point with a < c and b < d is eligible. To preserve flexibility for subsequent blue points (which have even larger c), greedily pair with the eligible red point that has the MAXIMUM y-coordinate b!

## 3. Step-by-Step Algorithm
1. Sort blue points in ascending order of x-coordinate c_j.
2. Maintain a list of unused red points.
3. For each blue point (c, d): find an unused red point with a < c and b < d that maximizes b.
4. If such a red point exists: pair them, mark red point as used, increment count.
5. Print count.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
    int x, y;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> red(n), blue(n);
    for (int i = 0; i < n; ++i) cin >> red[i].x >> red[i].y;
    for (int i = 0; i < n; ++i) cin >> blue[i].x >> blue[i].y;

    sort(blue.begin(), blue.end(), [](const Point& p1, const Point& p2) {
        return p1.x < p2.x;
    });

    vector<bool> used(n, false);
    int pairs = 0;

    for (int j = 0; j < n; ++j) {
        int best_i = -1;
        int max_y = -1;

        for (int i = 0; i < n; ++i) {
            if (!used[i] && red[i].x < blue[j].x && red[i].y < blue[j].y) {
                if (red[i].y > max_y) {
                    max_y = red[i].y;
                    best_i = i;
                }
            }
        }

        if (best_i != -1) {
            used[best_i] = true;
            pairs++;
        }
    }

    cout << pairs << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Greedy interval/coordinate matching equivalent to maximum bipartite matching.
- **Reusable Pattern**: `2D Point Matching: sweep blue by X ascending, match red with max Y < blue.Y.`
