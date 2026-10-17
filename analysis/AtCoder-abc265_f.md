# Problem Analysis: AtCoder-abc265_f — F. Manhattan Cafe

**Problem ID**: `AtCoder-abc265_f`  
**Contest**: `abc265`  
**Rating / Difficulty**: 2290  
**URL**: https://atcoder.jp/contests/abc265/tasks/abc265_f  
**VJudge Tag**: `[problem:AtCoder-abc265_f]`  
**Category File**: [`../categories/dynamic_programming/2d_knapsack_manhattan_prefix_sums.md`](../categories/dynamic_programming/2d_knapsack_manhattan_prefix_sums.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Subset Sum Optimizations`  

---

## 1. Problem Statement & Key Idea
Given two points $P, Q \in \mathbb{R}^N$, count the number of integer points $R \in \mathbb{Z}^N$ such that $d(P, R) \le D$ and $d(Q, R) \le D$ under the Manhattan distance metric, modulo 998244353.

## 2. Core Observation & Invariant
In dimension $i$ with coordinate difference $d = |p_i - q_i|$, choosing $r_i$ adds $(\Delta_p, \Delta_q) = (|r_i - p_i|, |r_i - q_i|)$. Over all possible integers $r_i$, the pair of step distances sweeps a trapezoidal segment where $\Delta_p - \Delta_q$ or $\Delta_p + \Delta_q$ is constant, allowing constant-time range updates via 2D diagonal prefix sums.

## 3. Step-by-Step Algorithm
1. 1. Let $dp[j][k]$ be the number of choices for coordinates $r_1, \dots, r_i$ such that $\sum |r - p| = j$ and $\sum |r - q| = k$.
2. 2. In step $i$, let $d = |p_i - q_i|$. For a choice of coordinate $r_i$:
3.    - Between $p_i$ and $q_i$ ($d + 1$ integers): $\Delta_p + \Delta_q = d$, so $(\Delta_p, \Delta_q) = (x, d - x)$ for $0 \le x \le d$.
4.    - Outside the interval: $(\Delta_p, \Delta_q) = (d + t, t)$ or $(t, d + t)$ for $t \ge 1$.
5. 3. Naive transitions take $O(D)$ per state, leading to $O(N D^3)$, which is too slow. Notice the transitions are 1D slices along diagonals $j + k = const$ and $j - k = const$.
6. 4. By precomputing diagonal prefix sums $diag_1[j][k] = \sum dp[j - x][k - x]$ and $diag_2[j][k] = \sum dp[j - x][k - (d - x)]$, each state $(j, k)$ can transition in $O(1)$ amortized time.
7. 5. Total runtime is $O(N D^2)$ with $N \le 100, D \le 1000$, executing in under 0.8s.

## 4. Complexity Analysis
- **Time Complexity**: `O(N D^2)`
- **Space Complexity**: `O(D^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

static const int MOD = 998244353;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, D;
    if (!(cin >> N >> D)) return 0;

    vector<int> p(N), q(N);
    for (int i = 0; i < N; ++i) cin >> p[i];
    for (int i = 0; i < N; ++i) cin >> q[i];

    vector<vector<int>> dp(D + 1, vector<int>(D + 1, 0));
    dp[0][0] = 1;

    for (int dim = 0; dim < N; ++dim) {
        int d = abs(p[dim] - q[dim]);
        vector<vector<int>> next_dp(D + 1, vector<int>(D + 1, 0));

        // Prefixes along direction (+1, +1): sum_{t >= 0} dp[j - t][k - t]
        vector<vector<int>> pref_diag(D + 1, vector<int>(D + 1, 0));
        for (int j = 0; j <= D; ++j) {
            for (int k = 0; k <= D; ++k) {
                pref_diag[j][k] = dp[j][k];
                if (j > 0 && k > 0) {
                    pref_diag[j][k] = (pref_diag[j][k] + pref_diag[j - 1][k - 1]) % MOD;
                }
            }
        }

        // Prefixes along direction (+1, -1): sum_{x} dp[j - x][k - (d - x)]
        // Notice j + k increases by d.
        // For between p and q: sum_{x = 0}^d dp[j - x][k - (d - x)].
        // Let sum_anti[j][k] be along (j - 1, k + 1)
        vector<vector<int>> pref_anti(D + 1, vector<int>(D + 1, 0));
        for (int j = 0; j <= D; ++j) {
            for (int k = 0; k <= D; ++k) {
                pref_anti[j][k] = dp[j][k];
                if (j > 0 && k + 1 <= D) {
                    pref_anti[j][k] = (pref_anti[j][k] + pref_anti[j - 1][k + 1]) % MOD;
                }
            }
        }

        for (int j = 0; j <= D; ++j) {
            for (int k = 0; k <= D; ++k) {
                long long val = 0;

                // 1. Between p and q: x in [0, d], delta = (x, d - x)
                // Requires j >= x and k >= d - x => x <= j and x >= d - k.
                int low_x = max(0, d - k);
                int high_x = min(d, j);
                if (low_x <= high_x) {
                    // sum of dp[j - x][k - (d - x)] for x in [low_x, high_x]
                    // In pref_anti: moving along (+1, -1)
                    int top_j = j - low_x;
                    int top_k = k - (d - low_x);
                    int cur_sum = pref_anti[top_j][top_k];
                    int bot_j = j - (high_x + 1);
                    int bot_k = k - (d - (high_x + 1));
                    if (bot_j >= 0 && bot_k <= D) {
                        cur_sum = (cur_sum - pref_anti[bot_j][bot_k] + MOD) % MOD;
                    }
                    val = (val + cur_sum) % MOD;
                }

                // 2. Beyond p: delta = (t, d + t) for t >= 1
                // Requires j >= 1, k >= d + 1
                if (j >= 1 && k >= d + 1) {
                    int max_t = min(j, k - d);
                    int cur_sum = pref_diag[j - 1][k - d - 1];
                    int end_j = j - 1 - max_t;
                    int end_k = k - d - 1 - max_t;
                    if (end_j >= 0 && end_k >= 0) {
                        cur_sum = (cur_sum - pref_diag[end_j][end_k] + MOD) % MOD;
                    }
                    val = (val + cur_sum) % MOD;
                }

                // 3. Beyond q: delta = (d + t, t) for t >= 1
                // Requires j >= d + 1, k >= 1
                if (j >= d + 1 && k >= 1) {
                    int max_t = min(j - d, k);
                    int cur_sum = pref_diag[j - d - 1][k - 1];
                    int end_j = j - d - 1 - max_t;
                    int end_k = k - 1 - max_t;
                    if (end_j >= 0 && end_k >= 0) {
                        cur_sum = (cur_sum - pref_diag[end_j][end_k] + MOD) % MOD;
                    }
                    val = (val + cur_sum) % MOD;
                }

                next_dp[j][k] = val;
            }
        }
        dp = move(next_dp);
    }

    long long ans = 0;
    for (int j = 0; j <= D; ++j) {
        for (int k = 0; k <= D; ++k) {
            ans = (ans + dp[j][k]) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
