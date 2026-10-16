# Problem Analysis: AtCoder-abc183_e — Queen on Grid

**Problem ID**: `AtCoder-abc183_e`  
**Contest**: `abc183`  
**Rating / Difficulty**: 1288  
**URL**: https://atcoder.jp/contests/abc183/tasks/abc183_e  
**VJudge Tag**: `[problem:AtCoder-abc183_e]`  
**Category File**: [`../categories/dp/queen_grid_dp_prefix_sums.md`](../categories/dp/queen_grid_dp_prefix_sums.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Grid DP`  
- **Topic (Skill)**: `2D Grid DP with 3-Way Running Prefix Sums`  

---

## 1. Problem Statement & Key Idea
An H x W grid of '.' and '#'. Start at (1, 1), reach (H, W). A piece can move any number of steps right, down, or down-right without passing obstacles '#'. Find the number of paths modulo 10^9 + 7.

**Key Idea**: Moving any number of steps in 3 directions means dp[r][c] is the sum of previous DP values along the current row, column, and main diagonal.

## 2. Core Observation & Invariant
Naive summation takes O(H * W * max(H, W)). Maintain 3 running prefix sums at each cell: X[r][c] (horizontal prefix), Y[r][c] (vertical prefix), and Z[r][c] (diagonal prefix). If cell is '#', all prefixes reset to 0. Else dp[r][c] = X + Y + Z in O(1)!

## 3. Step-by-Step Algorithm
1. Initialize dp, X, Y, Z matrices of size H x W to 0; dp[0][0] = 1.
2. Iterate r from 0 to H - 1, c from 0 to W - 1:
3.   If grid[r][c] == '#': reset X[r][c] = Y[r][c] = Z[r][c] = 0, continue.
4.   If (r > 0 || c > 0): dp[r][c] = (X[r][c] + Y[r][c] + Z[r][c]) % MOD.
5.   Update prefixes for neighbors: X[r][c + 1] = (X[r][c] + dp[r][c]) % MOD; Y[r + 1][c] = (Y[r][c] + dp[r][c]) % MOD; Z[r + 1][c + 1] = (Z[r][c] + dp[r][c]) % MOD.
6. Output dp[H-1][W-1].

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    vector<vector<long long>> dp(h, vector<long long>(w, 0));
    vector<vector<long long>> X(h, vector<long long>(w, 0));
    vector<vector<long long>> Y(h, vector<long long>(w, 0));
    vector<vector<long long>> Z(h, vector<long long>(w, 0));

    dp[0][0] = 1;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '#') continue;

            if (r > 0 || c > 0) {
                dp[r][c] = (X[r][c] + Y[r][c] + Z[r][c]) % MOD;
            }

            // Propagate to right
            if (c + 1 < w) X[r][c + 1] = (X[r][c] + dp[r][c]) % MOD;
            // Propagate down
            if (r + 1 < h) Y[r + 1][c] = (Y[r][c] + dp[r][c]) % MOD;
            // Propagate diagonal
            if (r + 1 < h && c + 1 < w) Z[r + 1][c + 1] = (Z[r][c] + dp[r][c]) % MOD;
        }
    }

    cout << dp[h - 1][w - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Accelerating multi-directional grid ray DP via running prefix arrays.
- **Reusable Pattern**: `Queen move DP: maintain horizontal, vertical, and diagonal running prefix sums.`
