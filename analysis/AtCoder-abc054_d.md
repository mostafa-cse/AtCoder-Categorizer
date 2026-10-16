# Problem Analysis: AtCoder-abc054_d — Mixing Experiment

**Problem ID**: `AtCoder-abc054_d`  
**Contest**: `abc054`  
**Rating / Difficulty**: 1655  
**URL**: https://atcoder.jp/contests/abc054/tasks/abc054_d  
**VJudge Tag**: `[problem:AtCoder-abc054_d]`  
**Category File**: [`../categories/dp/two_ratio_knapsack_dp.md`](../categories/dp/two_ratio_knapsack_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `2-Ratio Knapsack DP / Ratio Reduction to Target GCD`  

---

## 1. Problem Statement & Key Idea
N chemicals, chemical i has a_i grams of substance A, b_i grams of substance B, and costs c_i. Find the minimum cost to obtain a mixture with substance ratio exactly Ma : Mb, or -1 if impossible.

**Key Insight**: 2D Knapsack DP maintaining the exact weights of substance A and B: dp[a][b] = minimum cost to obtain a grams of A and b grams of B. At the end, minimize dp[k * Ma][k * Mb] over all k >= 1.

## 2. Core Observation & Invariant
Max total weight of A or B is at most 40 * 10 = 400. The DP table size is 401 x 401, taking O(N * (max_A) * (max_B)) ~ 40 * 400 * 400 = 6.4 * 10^6 operations.

## 3. Step-by-Step Algorithm
1. Initialize dp[401][401] with INF. dp[0][0] = 0.
2. For each chemical (a_i, b_i, c_i):
3.   For a from 400 down to a_i:
4.     For b from 400 down to b_i:
5.       dp[a][b] = min(dp[a][b], dp[a - a_i][b - b_i] + c_i).
6. min_cost = INF.
7. For k from 1 such that k * Ma <= 400 and k * Mb <= 400:
8.   min_cost = min(min_cost, dp[k * Ma][k * Mb]).
9. Print min_cost < INF ? min_cost : -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * max_A * max_B)`
- **Space Complexity**: `O(max_A * max_B)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, ma, mb;
    if (!(cin >> n >> ma >> mb)) return 0;

    vector<vector<int>> dp(401, vector<int>(401, INF));
    dp[0][0] = 0;

    for (int i = 0; i < n; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        for (int sa = 400; sa >= a; --sa) {
            for (int sb = 400; sb >= b; --sb) {
                if (dp[sa - a][sb - b] < INF) {
                    dp[sa][sb] = min(dp[sa][sb], dp[sa - a][sb - b] + c);
                }
            }
        }
    }

    int ans = INF;
    for (int k = 1; k * ma <= 400 && k * mb <= 400; ++k) {
        ans = min(ans, dp[k * ma][k * mb]);
    }

    cout << (ans >= INF ? -1 : ans) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multi-dimensional knapsack tracking exact additive resource pairs to match target ratios.
- **Reusable Pattern**: `Exact Ratio Knapsack: dp[a][b] + query min_k dp[k*Ma][k*Mb].`
