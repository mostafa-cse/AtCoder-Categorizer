# Problem Analysis: AtCoder-abc008_4 — 金塊ゲーム

**Problem ID**: `AtCoder-abc008_4`  
**Contest**: `abc008`  
**Rating / Difficulty**: 2203  
**URL**: https://atcoder.jp/contests/abc008/tasks/abc008_4  
**VJudge Tag**: `[problem:AtCoder-abc008_4]`  
**Category File**: [`../categories/dp/gold_rush_2d_divide_and_conquer_range_dp.md`](../categories/dp/gold_rush_2d_divide_and_conquer_range_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
2D Divide-and-Conquer Range DP decomposing activated machines into four independent rectangular sub-regions.

## 2. Core Observation & Invariant
When the first machine inside a bounding box [x1, x2] x [y1, y2] is activated at (X_i, Y_i), it collects all gold in its row and column within the box, collecting (x2 - x1 + 1) + (y2 - y1 + 1) - 1 gold. This laser divides the remaining gold into four completely independent sub-rectangles: Top-Left, Top-Right, Bottom-Left, and Bottom-Right.

## 3. Step-by-Step Algorithm
1. 1. Memoized 2D Range DP solve(x1, x2, y1, y2).
2. 2. Iterate over all machines i in the current rectangle.
3. 3. The value is laser gold + solve(x1, X[i]-1, y1, Y[i]-1) + solve(X[i]+1, x2, y1, Y[i]-1) + solve(x1, X[i]-1, Y[i]+1, y2) + solve(X[i]+1, x2, Y[i]+1, y2).
4. 4. Memoize over reachable bounding boxes defined by machine coordinates (at most O(N^4) states, in practice << 10^4).

## 4. Complexity Analysis
- **Time Complexity**: `O(N^5) worst-case, << 10^5 operations in practice`
- **Space Complexity**: `O(N^4) memoized states`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int W, H, N;
int X[35], Y[35];

map<tuple<int, int, int, int>, int> memo;

int solve(int x1, int x2, int y1, int y2) {
    if (x1 > x2 || y1 > y2) return 0;
    auto key = make_tuple(x1, x2, y1, y2);
    if (memo.count(key)) return memo[key];

    int res = 0;
    for (int i = 0; i < N; ++i) {
        if (X[i] >= x1 && X[i] <= x2 && Y[i] >= y1 && Y[i] <= y2) {
            int cur = (x2 - x1 + 1) + (y2 - y1 + 1) - 1;
            cur += solve(x1, X[i] - 1, y1, Y[i] - 1);
            cur += solve(X[i] + 1, x2, y1, Y[i] - 1);
            cur += solve(x1, X[i] - 1, Y[i] + 1, y2);
            cur += solve(X[i] + 1, x2, Y[i] + 1, y2);
            res = max(res, cur);
        }
    }

    return memo[key] = res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> W >> H >> N)) return 0;
    for (int i = 0; i < N; ++i) {
        cin >> X[i] >> Y[i];
    }

    cout << solve(1, W, 1, H) << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
