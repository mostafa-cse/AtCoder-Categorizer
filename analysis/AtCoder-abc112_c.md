# Problem Analysis: AtCoder-abc112_c — Pyramid

**Problem ID**: `AtCoder-abc112_c`  
**Contest**: `abc112`  
**Rating / Difficulty**: 1147  
**URL**: https://atcoder.jp/contests/abc112/tasks/abc112_c  
**VJudge Tag**: `[problem:AtCoder-abc112_c]`  
**Category File**: [`../categories/basics/center_parameter_brute_force.md`](../categories/basics/center_parameter_brute_force.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Complete Search`  
- **Topic (Skill)**: `Center Parameter Brute Force with Positive Reference Anchor`  

---

## 1. Problem Statement & Key Idea
A pyramid has center (C_X, C_Y) and height H (0 <= C_X, C_Y <= 100, H >= 1). Height at (x, y) is max(0, H - |x - C_X| - |y - C_Y|). Given N observations (x_i, y_i, h_i), find (C_X, C_Y, H).

**Key Idea**: The search space for (C_X, C_Y) is tiny: 101 x 101 = 10,201 candidate coordinate pairs.

## 2. Core Observation & Invariant
For any fixed candidate (cx, cy), pick an observation with h_i > 0. Since h_i > 0, the equation h_i = H - |x_i - cx| - |y_i - cy| holds without truncation, uniquely fixing H = h_i + |x_i - cx| + |y_i - cy|! Then verify this H against all other N observations in O(N).

## 3. Step-by-Step Algorithm
1. Iterate cx from 0 to 100 and cy from 0 to 100.
2. Find an observation k with h_k > 0; set H = h_k + abs(x_k - cx) + abs(y_k - cy).
3. Verify for all i in 0..N-1: check if h_i == max(0LL, H - abs(x_i - cx) - abs(y_i - cy)).
4. If all match, output cx, cy, H and terminate.

## 4. Complexity Analysis
- **Time Complexity**: `O(101^2 * N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y, h;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Point> pts(n);
    int pos_idx = -1;
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].x >> pts[i].y >> pts[i].h;
        if (pts[i].h > 0) pos_idx = i;
    }

    for (int cx = 0; cx <= 100; ++cx) {
        for (int cy = 0; cy <= 100; ++cy) {
            long long H = pts[pos_idx].h + abs(pts[pos_idx].x - cx) + abs(pts[pos_idx].y - cy);
            bool ok = true;
            for (int i = 0; i < n; ++i) {
                long long expected = max(0LL, H - abs(pts[i].x - cx) - abs(pts[i].y - cy));
                if (pts[i].h != expected) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                cout << cx << " " << cy << " " << H << "\n";
                return 0;
            }
        }
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Uniquely solving dependent parameters using positive anchor references in complete search.
- **Reusable Pattern**: `Fix coordinate center -> use positive anchor h > 0 to resolve H -> verify consistency.`
