# Problem Analysis: AtCoder-abc004_4 — マーブル

**Problem ID**: `AtCoder-abc004_4`  
**Contest**: `abc004`  
**Rating / Difficulty**: 1861  
**URL**: https://atcoder.jp/contests/abc004/tasks/abc004_4  
**VJudge Tag**: `[problem:AtCoder-abc004_4]`  
**Category File**: [`../categories/dp/contiguous_block_placement_dp_marbles.md`](../categories/dp/contiguous_block_placement_dp_marbles.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Interval DP`  
- **Topic (Skill)**: `Contiguous Block Placement DP for Colored Particles on 1D Line`  

---

## 1. Problem Statement & Key Idea
Place R red marbles (initially at -100), G green marbles (initially at 0), and B blue marbles (initially at 100) into distinct integer positions to minimize total distance traveled.

**Key Insight**: The optimal placement places all red marbles into a contiguous block [r_L, r_R], all green into [g_L, g_R], and all blue into [b_L, b_R] such that r_R < g_L and g_R < b_L. Iterate over green's center/start position, and place red and blue greedily closest to their origins.

## 2. Core Observation & Invariant
Green's starting position g_L can be restricted to [-500, 500]. For a fixed [g_L, g_R]: red marbles are placed in the interval of length R <= g_L - 1 that minimizes sum |pos - (-100)|, and blue marbles in length B >= g_R + 1 that minimizes sum |pos - 100|.

## 3. Step-by-Step Algorithm
1. Write a function cost(start_pos, count, origin): sum_{i=0}^{count-1} |start_pos + i - origin|.
2. Function best_cost(max_pos, count, origin): optimal start is approx origin - count / 2 clamped to <= max_pos - count + 1.
3. ans = INF.
4. For g_L = -500 to 500:
5.   g_R = g_L + G - 1.
6.   cur = cost(g_L, G, 0) + best_left(g_L - 1, R, -100) + best_right(g_R + 1, B, 100).
7.   ans = min(ans, cur).
8. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(Range * (R + G + B))`
- **Space Complexity**: `O(1)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const long long INF = 1e18;

long long range_cost(int start, int len, int origin) {
    long long total = 0;
    for (int i = 0; i < len; ++i) {
        total += abs(start + i - origin);
    }
    return total;
}

long long best_left(int max_r, int len, int origin) {
    int ideal_start = origin - len / 2;
    int actual_start = min(ideal_start, max_r - len + 1);
    return range_cost(actual_start, len, origin);
}

long long best_right(int min_l, int len, int origin) {
    int ideal_start = origin - len / 2;
    int actual_start = max(ideal_start, min_l);
    return range_cost(actual_start, len, origin);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, G, B;
    if (!(cin >> R >> G >> B)) return 0;

    long long min_cost = INF;

    for (int g_start = -500; g_start <= 500; ++g_start) {
        int g_end = g_start + G - 1;
        long long cost_g = range_cost(g_start, G, 0);
        long long cost_r = best_left(g_start - 1, R, -100);
        long long cost_b = best_right(g_end + 1, B, 100);

        min_cost = min(min_cost, cost_g + cost_r + cost_b);
    }

    cout << min_cost << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Optimizing non-overlapping contiguous intervals of multiple particle types.
- **Reusable Pattern**: `3-Group Contiguous Interval Optimization: Fix middle interval and greedily clamp outer intervals.`
