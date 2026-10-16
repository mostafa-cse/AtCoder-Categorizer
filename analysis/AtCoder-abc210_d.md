# Problem Analysis: AtCoder-abc210_d — National Railway

**Problem ID**: `AtCoder-abc210_d`  
**Contest**: `abc210`  
**Rating / Difficulty**: 1507  
**URL**: https://atcoder.jp/contests/abc210/tasks/abc210_d  
**VJudge Tag**: `[problem:AtCoder-abc210_d]`  
**Category File**: [`../categories/dp/grid_dp_manhattan_distance.md`](../categories/dp/grid_dp_manhattan_distance.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `2D Grid DP`  
- **Topic (Skill)**: `2D Grid DP Coordinate Manhattan Distance Transformation`  

---

## 1. Problem Statement & Key Idea
An H x W grid with station construction costs A[i][j]. Cost to connect stations at (i, j) and (i', j') is A[i][j] + A[i'][j'] + C * (|i - i'| + |j - j'|). Minimize total cost over all pairs.

**Key Insight**: Remove the absolute value by orienting the relative position: either (i' <= i, j' <= j) or (i' <= i, j' >= j). The second case is solved by horizontally reversing the grid.

## 2. Core Observation & Invariant
For i' <= i and j' <= j: cost = (A[i][j] + C*(i + j)) + (A[i'][j'] - C*(i' + j')). Let dp[i][j] be min over all (i', j') in the top-left subgrid (excluding (i, j)) of A[i'][j'] + C * ((i - i') + (j - j')). dp[i][j] = min(A[i-1][j] + C, dp[i-1][j] + C, A[i][j-1] + C, dp[i][j-1] + C).

## 3. Step-by-Step Algorithm
1. Define solve(A, H, W):
2.   dp[H][W] initialized to INF.
3.   For r from 0 to H-1, c from 0 to W-1:
4.     If r > 0: dp[r][c] = min(dp[r][c], min(A[r - 1][c], dp[r - 1][c]) + C).
5.     If c > 0: dp[r][c] = min(dp[r][c], min(A[r][c - 1], dp[r][c - 1]) + C).
6.     ans = min(ans, A[r][c] + dp[r][c]).
7. Compute ans1 = solve(A).
8. Reverse each row of A, compute ans2 = solve(A).
9. Print min(ans1, ans2).

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

long long solve_directed(int h, int w, long long C, const vector<vector<long long>>& A) {
    vector<vector<long long>> dp(h, vector<long long>(w, INF));
    long long best = INF;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (r > 0) {
                dp[r][c] = min(dp[r][c], min(A[r - 1][c], dp[r - 1][c]) + C);
            }
            if (c > 0) {
                dp[r][c] = min(dp[r][c], min(A[r][c - 1], dp[r][c - 1]) + C);
            }
            if (dp[r][c] < INF) {
                best = min(best, A[r][c] + dp[r][c]);
            }
        }
    }
    return best;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    long long C;
    if (!(cin >> h >> w >> C)) return 0;

    vector<vector<long long>> A(h, vector<long long>(w));
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            cin >> A[r][c];
        }
    }

    long long ans1 = solve_directed(h, w, C, A);

    // Flip horizontally
    for (int r = 0; r < h; ++r) {
        reverse(A[r].begin(), A[r].end());
    }

    long long ans2 = solve_directed(h, w, C, A);

    cout << min(ans1, ans2) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Manhattan distance minimization via directional prefix DP sweeps and grid symmetry flips.
- **Reusable Pattern**: `Grid Manhattan Distance DP: top-left DP sweep, reverse rows, repeat top-left DP sweep.`
