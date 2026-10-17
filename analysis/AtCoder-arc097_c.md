# Problem Analysis: AtCoder-arc097_c — Sorted and Sorted

**Problem ID**: `AtCoder-arc097_c`  
**Contest**: `arc097`  
**Rating / Difficulty**: 2247  
**URL**: https://atcoder.jp/contests/arc097/tasks/arc097_c  
**VJudge Tag**: `[problem:AtCoder-arc097_c]`  
**Category File**: [`../categories/dp/sorted_and_sorted_adjacent_swaps_2d_dp.md`](../categories/dp/sorted_and_sorted_adjacent_swaps_2d_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Find the minimum number of adjacent swaps to reorder 2N balls (N white, N black) so that white balls and black balls are each internally sorted 1 to N.

## 2. Core Observation & Invariant
In any valid arrangement, the prefix of length i + j contains the first i white balls and the first j black balls. The number of adjacent swaps to construct a permutation equals the number of inversions. Placing white ball i + 1 next costs the number of remaining unplaced balls that initially appeared before pos(W_{i+1}). This cost decomposes into costW_W[i+1] (unplaced white balls before it) plus costW_B[i+1][j] (unplaced black balls before it), both precomputable in O(N^2).

## 3. Step-by-Step Algorithm
1. 1. Record initial 1-based positions posW[1..N] and posB[1..N].
2. 2. Precompute costW_W[i] = count of k > i with posW[k] < posW[i], and costB_B[j] = count of k > j with posB[k] < posB[j].
3. 3. Precompute costW_B[i][j] = count of k > j with posB[k] < posW[i] via suffix sums, and costB_W[j][i] similarly.
4. 4. Run 2D DP: dp[i][j] is the minimum swaps for placing i white and j black balls.
5.    - Transition to dp[i+1][j]: add costW_W[i+1] + costW_B[i+1][j].
6.    - Transition to dp[i][j+1]: add costB_B[j+1] + costB_W[j+1][i].
7. 5. Output dp[N][N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> posW(n + 1), posB(n + 1);
    for (int i = 1; i <= 2 * n; ++i) {
        char c;
        int a;
        cin >> c >> a;
        if (c == 'W') posW[a] = i;
        else posB[a] = i;
    }

    // costW_W[i]: count of k > i such that posW[k] < posW[i]
    vector<int> costW_W(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        for (int k = i + 1; k <= n; ++k) {
            if (posW[k] < posW[i]) costW_W[i]++;
        }
    }

    // costB_B[j]: count of k > j such that posB[k] < posB[j]
    vector<int> costB_B(n + 1, 0);
    for (int j = 1; j <= n; ++j) {
        for (int k = j + 1; k <= n; ++k) {
            if (posB[k] < posB[j]) costB_B[j]++;
        }
    }

    // costW_B[i][j]: count of k > j such that posB[k] < posW[i]
    vector<vector<int>> costW_B(n + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= n; ++i) {
        int cnt = 0;
        for (int k = n; k >= 1; --k) {
            if (posB[k] < posW[i]) cnt++;
            costW_B[i][k - 1] = cnt;
        }
    }

    // costB_W[j][i]: count of k > i such that posW[k] < posB[j]
    vector<vector<int>> costB_W(n + 1, vector<int>(n + 1, 0));
    for (int j = 1; j <= n; ++j) {
        int cnt = 0;
        for (int k = n; k >= 1; --k) {
            if (posW[k] < posB[j]) cnt++;
            costB_W[j][k - 1] = cnt;
        }
    }

    // dp[i][j] = min swaps to place i white balls and j black balls
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, INF));
    dp[0][0] = 0;

    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= n; ++j) {
            if (dp[i][j] == INF) continue;

            // Transition: place W_{i+1}
            if (i < n) {
                int cost = costW_W[i + 1] + costW_B[i + 1][j];
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + cost);
            }

            // Transition: place B_{j+1}
            if (j < n) {
                int cost = costB_B[j + 1] + costB_W[j + 1][i];
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + cost);
            }
        }
    }

    cout << dp[n][n] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
