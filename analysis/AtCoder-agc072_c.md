# Problem Analysis: AtCoder-agc072_c — C - Human Exercise

**Problem ID**: `AtCoder-agc072_c`  
**Contest**: `agc072`  
**Rating / Difficulty**: 2984  
**URL**: https://atcoder.jp/contests/agc072/tasks/agc072_c  
**VJudge Tag**: `[problem:AtCoder-agc072_c]`  
**Category File**: [`../categories/miscellaneous/antidiagonal_symmetry_periodic_grid_flow_invariants.md`](../categories/miscellaneous/antidiagonal_symmetry_periodic_grid_flow_invariants.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Invariants and Monovariants`  

---

## 1. Problem Statement & Key Idea
On an N x N grid, a runner starts at (1, 1) and moves 2N-2 steps to (N, N), always choosing the adjacent cell visited fewer times in past exercises (ties broken by Down). Determine the path of the K-th exercise for N <= 100 and K <= 10^18.

## 2. Core Observation & Invariant
By antidiagonal reflection symmetry across i + j = N + 1, the second half of the path is the reversed and character-inverted (D <-> R) first half. For any cell (i, j) in the upper triangle, the departure direction is strictly periodic with cycle i + j consisting of i Down moves followed by j Right moves. The visit counts after K-1 exercises can be computed by grid flow DP.

## 3. Step-by-Step Algorithm
1. 1. Initialize dp[1][1] = K - 1.
2. 2. For each diagonal sum s from 2 to N, compute flow from each cell (i, j): c = dp[i][j] // (i+j), rem = dp[i][j] % (i+j). Flow to (i+1, j) is c*i + min(rem, i), and remainder flows to (i, j+1).
3. 3. Simulate Aoki's K-th path from (1, 1) for N-1 steps: at cell (i, j), if (dp[i][j] % (i+j)) < i, move D; else move R.
4. 4. Construct the second half by reversing the first half and swapping 'D' and 'R'.
5. 5. Output the full string of length 2N-2.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    long long K;
    if (!(cin >> N >> K)) return 0;

    long long t = K - 1;

    vector<vector<long long>> dp(N + 2, vector<long long>(N + 2, 0));
    dp[1][1] = t;

    for (int s = 2; s <= N; ++s) {
        for (int i = 1; i < s; ++i) {
            int j = s - i;
            long long cnt = dp[i][j];
            long long cycle = i + j;
            long long c = cnt / cycle;
            long long rem = cnt % cycle;
            long long d_moves = c * i + min(rem, (long long)i);
            long long r_moves = cnt - d_moves;
            dp[i + 1][j] += d_moves;
            dp[i][j + 1] += r_moves;
        }
    }

    int curr_i = 1, curr_j = 1;
    string first_half = "";
    for (int step = 0; step < N - 1; ++step) {
        long long cnt = dp[curr_i][curr_j];
        long long cycle = curr_i + curr_j;
        long long rem = cnt % cycle;
        if (rem < curr_i) {
            first_half.push_back('D');
            curr_i += 1;
        } else {
            first_half.push_back('R');
            curr_j += 1;
        }
    }

    string second_half = "";
    for (int step = N - 2; step >= 0; --step) {
        if (first_half[step] == 'R') second_half.push_back('D');
        else second_half.push_back('R');
    }

    cout << first_half << second_half << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
