# Problem Analysis: AtCoder-abc404_f — Lost and Pound

**Problem ID**: `AtCoder-abc404_f`  
**Contest**: `abc404`  
**Rating / Difficulty**: 2162  
**URL**: https://atcoder.jp/contests/abc404/tasks/abc404_f  
**VJudge Tag**: `[problem:AtCoder-abc404_f]`  
**Category File**: [`../categories/dynamic_programming/integer_partition_knapsack_optimal_resource_game.md`](../categories/dynamic_programming/integer_partition_knapsack_optimal_resource_game.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Sequential decision game with N buttons (1 winner) and T turns of M presses. Takahashi maximizes probability of winning >= K times. Backward induction on turns and presses solved via bounded integer partition knapsack DP.

## 2. Core Observation & Invariant
Let DP[t][k] be the winning probability from turn t with k winning presses so far. At each turn, Takahashi chooses press counts c_1 + ... + c_N = M. Since the winning button is uniformly random, the winning probability is (1/N) sum DP[t+1][k + c_i]. Non-zero presses occur on at most min(N, M) buttons; the optimal choice of positive parts is found via an integer partition knapsack.

## 3. Step-by-Step Algorithm
1. Initialize base case DP[T][k] = 1 for k >= K, and 0 otherwise.
2. For turn t from T-1 down to 0 and current winning count k from 0 to K:
3. Precompute bounded partition knapsack dp_parts[count][s]: maximum sum of DP[t+1][min(K, k + c_i)] where count positive parts sum to s.
4. Evaluate best_sum = max_{1 <= count <= min(N, M)} (dp_parts[count][M] + (N - count) * DP[t+1][k]).
5. Set DP[t][k] = best_sum / N. Output DP[0][0].

## 4. Complexity Analysis
- **Time Complexity**: `O(T * K * M^3)`
- **Space Complexity**: `O(T * K + M^2)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, t_total, m_press, k_target;
    if (!(cin >> n >> t_total >> m_press >> k_target)) return 0;

    vector<vector<double>> dp(t_total + 1, vector<double>(k_target + 1, 0.0));
    for (int k = 0; k <= k_target; ++k) {
        dp[t_total][k] = (k >= k_target ? 1.0 : 0.0);
    }

    for (int t = t_total - 1; t >= 0; --t) {
        for (int k = 0; k <= k_target; ++k) {
            vector<vector<double>> dp_parts(m_press + 1, vector<double>(m_press + 1, -1.0));
            dp_parts[0][0] = 0.0;

            for (int count = 1; count <= min(n, m_press); ++count) {
                for (int s = count; s <= m_press; ++s) {
                    for (int c = 1; c <= s - count + 1; ++c) {
                        if (dp_parts[count - 1][s - c] >= 0.0) {
                            int next_k = min(k_target, k + c);
                            dp_parts[count][s] = max(dp_parts[count][s], dp_parts[count - 1][s - c] + dp[t + 1][next_k]);
                        }
                    }
                }
            }

            double best_sum = 0.0;
            for (int count = 1; count <= min(n, m_press); ++count) {
                if (dp_parts[count][m_press] >= 0.0) {
                    double total = dp_parts[count][m_press] + (double)(n - count) * dp[t + 1][k];
                    best_sum = max(best_sum, total);
                }
            }

            dp[t][k] = best_sum / n;
        }
    }

    cout << fixed << setprecision(12) << dp[0][0] << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
