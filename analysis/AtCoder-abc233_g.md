# Problem Analysis: AtCoder-abc233_g — G. Strongest Takahashi

**Problem ID**: `AtCoder-abc233_g`  
**Contest**: `abc233`  
**Rating / Difficulty**: 2438  
**URL**: https://atcoder.jp/contests/abc233/tasks/abc233_g  
**VJudge Tag**: `[problem:AtCoder-abc233_g]`  
**Category File**: [`../categories/dynamic_programming/strongest_takahashi_subgrid_interval_dp.md`](../categories/dynamic_programming/strongest_takahashi_subgrid_interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Given an $N \times N$ grid ($N \le 50$) with '#' squares, find the minimum cost to destroy all '#' using $D \times D$ subsquares at cost $D$. A 4D subgrid interval DP $dp[r_1][r_2][c_1][c_2]$ computes the optimal cost by taking the base square cost $\max(r_2 - r_1 + 1, c_2 - c_1 + 1)$ and taking the minimum over all horizontal cuts $r_1 \le k < r_2$ and vertical cuts $c_1 \le k < c_2$.

## 2. Core Observation & Invariant
Any subgrid without '#' costs 0. For any subgrid with '#', we can either cover it entirely with one square of size $\max(\Delta r, \Delta c)$, or divide it into two independent subproblems by cutting across a row or column.

## 3. Step-by-Step Algorithm
1. 1. Build 2D prefix sums to check in $O(1)$ whether any subgrid contains any '#'.
2. 2. Define memoized function $get\_dp(r_1, r_2, c_1, c_2)$:
3.    - If no '#' exists in subgrid, return 0.
4.    - Base cost: $\max(r_2 - r_1 + 1, c_2 - c_1 + 1)$.
5.    - For $k = r_1 \dots r_2 - 1$: $cost = \min(cost, get\_dp(r_1, k, c_1, c_2) + get\_dp(k+1, r_2, c_1, c_2))$.
6.    - For $k = c_1 \dots c_2 - 1$: $cost = \min(cost, get\_dp(r_1, r_2, c_1, k) + get\_dp(r_1, r_2, k+1, c_2))$.
7. 3. Return $get\_dp(0, N-1, 0, N-1)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^5)`
- **Space Complexity**: `O(N^4)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int memo[55][55][55][55];
int pref[55][55];

int has_hash(int r1, int r2, int c1, int c2) {
    return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1] > 0;
}

int get_dp(int r1, int r2, int c1, int c2) {
    if (!has_hash(r1, r2, c1, c2)) return 0;
    if (memo[r1][r2][c1][c2] != -1) return memo[r1][r2][c1][c2];

    int res = max(r2 - r1 + 1, c2 - c1 + 1);

    for (int k = r1; k < r2; ++k) {
        res = min(res, get_dp(r1, k, c1, c2) + get_dp(k + 1, r2, c1, c2));
    }
    for (int k = c1; k < c2; ++k) {
        res = min(res, get_dp(r1, r2, c1, k) + get_dp(r1, r2, k + 1, c2));
    }

    return memo[r1][r2][c1][c2] = res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<string> grid(N);
    for (int i = 0; i < N; ++i) {
        cin >> grid[i];
        for (int j = 0; j < N; ++j) {
            pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + (grid[i][j] == '#' ? 1 : 0);
        }
    }

    for (int r1 = 0; r1 < N; ++r1)
        for (int r2 = 0; r2 < N; ++r2)
            for (int c1 = 0; c1 < N; ++c1)
                for (int c2 = 0; c2 < N; ++c2)
                    memo[r1][r2][c1][c2] = -1;

    cout << get_dp(0, N - 1, 0, N - 1) << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
