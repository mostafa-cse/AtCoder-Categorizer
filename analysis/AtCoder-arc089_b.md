# Problem Analysis: AtCoder-arc089_b — Checker

**Problem ID**: `AtCoder-arc089_b`  
**Contest**: `abc086`  
**Rating / Difficulty**: 1797  
**URL**: https://atcoder.jp/contests/abc086/tasks/arc089_b  
**VJudge Tag**: `[problem:AtCoder-arc089_b]`  
**Category File**: [`../categories/basics/2d_periodic_chessboard_reduction.md`](../categories/basics/2d_periodic_chessboard_reduction.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `2D Prefix Sums`  
- **Topic (Skill)**: `2D Periodic Chessboard Coordinate Reduction and 2D Prefix Sums`  

---

## 1. Problem Statement & Key Idea
Given N points with target colors ('B' or 'W') on an infinite 2D plane. An infinite chessboard grid with tile size K has alternating black and white squares. Find the shift (dx, dy) that maximizes satisfied points.

**Key Insight**: The chessboard pattern has period 2K in both X and Y dimensions. A white point at (x, y) is equivalent to a black point at (x, y + K). Fold all points modulo 2K: (x % 2K, y % 2K). Then use 2D prefix sums to evaluate all (2K) x (2K) shift offsets in O(K^2).

## 2. Core Observation & Invariant
Construct a (2K) x (2K) grid counting folded black points. Duplicate the grid into a (4K) x (4K) array so that any K x K subgrid query wraps seamlessly via standard 2D prefix sums.

## 3. Step-by-Step Algorithm
1. For each point (x, y, color):
2.   If color == 'W': y += K.
3.   grid[x % (2K)][y % (2K)]++.
4. Tile the (2K) x (2K) counts across a (4K) x (4K) board.
5. Compute 2D prefix sums on the board.
6. For dx in 0..K-1, dy in 0..K-1:
7.   sum_black = query(dx, dy, dx + K, dy + K) + query(dx + K, dy + K, dx + 2K, dy + 2K).
8.   max_satisfied = max(max_satisfied, max(sum_black, N - sum_black)).
9. Print max_satisfied.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + K^2)`
- **Space Complexity**: `O(K^2)`

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

    int k2 = 2 * k;
    vector<vector<int>> cnt(k2, vector<int>(k2, 0));

    for (int i = 0; i < n; ++i) {
        int x, y;
        char c;
        cin >> x >> y >> c;
        if (c == 'W') y += k;
        cnt[x % k2][y % k2]++;
    }

    vector<vector<int>> pref(2 * k2 + 1, vector<int>(2 * k2 + 1, 0));
    for (int i = 0; i < 2 * k2; ++i) {
        for (int j = 0; j < 2 * k2; ++j) {
            pref[i + 1][j + 1] = cnt[i % k2][j % k2] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j];
        }
    }

    auto get_sum = [&](int x1, int y1, int x2, int y2) -> int {
        return pref[x2][y2] - pref[x1][y2] - pref[x2][y1] + pref[x1][y1];
    };

    int max_ans = 0;
    for (int i = 0; i < k; ++i) {
        for (int j = 0; j < k; ++j) {
            int black_count = get_sum(i, j, i + k, j + k) +
                              get_sum(i + k, j + k, i + 2 * k, j + 2 * k);
            max_ans = max(max_ans, max(black_count, n - black_count));
        }
    }

    cout << max_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Periodic grid coordinate folding and wrapping 2D prefix sums.
- **Reusable Pattern**: `Periodic 2D Grid Folding: Map (x, y) mod 2K and query K x K blocks via 2D prefix sum.`
