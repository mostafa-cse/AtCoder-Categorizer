# Problem Analysis: AtCoder-dwango2016qual_d — 庭園

**Problem ID**: `AtCoder-dwango2016qual_d`  
**Contest**: `dwango2016-prelims`  
**Rating / Difficulty**: 2233  
**URL**: https://atcoder.jp/contests/dwango2016-prelims/tasks/dwango2016qual_d  
**VJudge Tag**: `[problem:AtCoder-dwango2016qual_d]`  
**Category File**: [`../categories/basics/two_dimensional_prefix_sums_disjoint_rectangles_kadane.md`](../categories/basics/two_dimensional_prefix_sums_disjoint_rectangles_kadane.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `2D Prefix Sum`  
- **Topic (Skill)**: `2D Prefix Sum`  

---

## 1. Problem Statement & Key Idea
Find the maximum possible sum of two disjoint subrectangles in an H x W grid with H, W <= 300.

## 2. Core Observation & Invariant
Any two disjoint axis-aligned rectangles can be separated by either a horizontal dividing line (one rectangle in rows <= r, the other in rows > r) or a vertical dividing line (one in columns <= c, the other in columns > c). For every pair of rows (r1, r2), Kadane's algorithm on column sums finds the maximum subrectangle spanning those rows in O(W). Running prefix and suffix dynamic programming over row and column boundaries solves the problem in O(H^2 W + H W^2).

## 3. Step-by-Step Algorithm
1. 1. Compute 2D prefix sums for the H x W grid.
2. 2. For all pairs of rows (r1, r2), apply 1D Kadane's algorithm across columns to find the maximum subrectangle bounded by rows [r1, r2].
3. 3. Similarly, for all pairs of columns (c1, c2), apply Kadane across rows.
4. 4. Compute top[r] and bottom[r]: maximum subrectangle contained in rows [0, r] and [r, H-1] respectively.
5. 5. Compute left[c] and right[c]: maximum subrectangle contained in columns [0, c] and [c, W-1] respectively.
6. 6. Evaluate max(top[r] + bottom[r+1]) over r in [0, H-2] and max(left[c] + right[c+1]) over c in [0, W-2].

## 4. Complexity Analysis
- **Time Complexity**: `O(H^2 W + H W^2)`
- **Space Complexity**: `O(H^2 + W^2 + H W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long INF = 2e18;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<vector<long long>> B(H, vector<long long>(W));
    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            cin >> B[r][c];
        }
    }

    vector<vector<long long>> pref(H + 1, vector<long long>(W + 1, 0));
    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            pref[r + 1][c + 1] = pref[r][c + 1] + pref[r + 1][c] - pref[r][c] + B[r][c];
        }
    }

    vector<vector<long long>> rect_rows(H, vector<long long>(H, -INF));
    for (int r1 = 0; r1 < H; ++r1) {
        for (int r2 = r1; r2 < H; ++r2) {
            long long best = -INF;
            long long cur = 0;
            for (int c = 0; c < W; ++c) {
                long long val = pref[r2 + 1][c + 1] - pref[r1][c + 1] - pref[r2 + 1][c] + pref[r1][c];
                cur += val;
                if (cur > best) best = cur;
                if (cur < 0) cur = 0;
            }
            rect_rows[r1][r2] = best;
        }
    }

    vector<vector<long long>> rect_cols(W, vector<long long>(W, -INF));
    for (int c1 = 0; c1 < W; ++c1) {
        for (int c2 = c1; c2 < W; ++c2) {
            long long best = -INF;
            long long cur = 0;
            for (int r = 0; r < H; ++r) {
                long long val = pref[r + 1][c2 + 1] - pref[r + 1][c1] - pref[r][c2 + 1] + pref[r][c1];
                cur += val;
                if (cur > best) best = cur;
                if (cur < 0) cur = 0;
            }
            rect_cols[c1][c2] = best;
        }
    }

    vector<long long> top(H, -INF);
    for (int r = 0; r < H; ++r) {
        long long val = (r > 0 ? top[r - 1] : -INF);
        for (int r1 = 0; r1 <= r; ++r1) {
            val = max(val, rect_rows[r1][r]);
        }
        top[r] = val;
    }

    vector<long long> bottom(H, -INF);
    for (int r = H - 1; r >= 0; --r) {
        long long val = (r + 1 < H ? bottom[r + 1] : -INF);
        for (int r2 = r; r2 < H; ++r2) {
            val = max(val, rect_rows[r][r2]);
        }
        bottom[r] = val;
    }

    vector<long long> left(W, -INF);
    for (int c = 0; c < W; ++c) {
        long long val = (c > 0 ? left[c - 1] : -INF);
        for (int c1 = 0; c1 <= c; ++c1) {
            val = max(val, rect_cols[c1][c]);
        }
        left[c] = val;
    }

    vector<long long> right(W, -INF);
    for (int c = W - 1; c >= 0; --c) {
        long long val = (c + 1 < W ? right[c + 1] : -INF);
        for (int c2 = c; c2 < W; ++c2) {
            val = max(val, rect_cols[c][c2]);
        }
        right[c] = val;
    }

    long long ans = -INF;
    for (int r = 0; r < H - 1; ++r) {
        ans = max(ans, top[r] + bottom[r + 1]);
    }
    for (int c = 0; c < W - 1; ++c) {
        ans = max(ans, left[c] + right[c + 1]);
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
