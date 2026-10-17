# Problem Analysis: AtCoder-abc203_f — F. Weed

**Problem ID**: `AtCoder-abc203_f`  
**Contest**: `abc203`  
**Rating / Difficulty**: 2252  
**URL**: https://atcoder.jp/contests/abc203/tasks/abc203_f  
**VJudge Tag**: `[problem:AtCoder-abc203_f]`  
**Category File**: [`../categories/dp/logarithmic_halving_operations_greedy_dp.md`](../categories/dp/logarithmic_halving_operations_greedy_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Given $N$ weeds with heights $A_1, \dots, A_N$. Aoki can pull at most $K$ weeds. Then Takahashi repeatedly pulls all weeds with height $> H / 2$ where $H$ is the maximum remaining weed height. Aoki wants to minimize Takahashi's operations, and then minimize Aoki's pulls.

## 2. Core Observation & Invariant
Because each Takahashi operation halves the maximum height, Takahashi can perform at most $\approx 32$ operations even if Aoki pulls 0 weeds. Sort $A$ ascending. For weed $i$, Takahashi's operation eliminates all weeds in $(prev[i], i]$ where $A_{prev[i]} \le \lfloor A_i / 2 \rfloor$.
Let $DP[i][j]$ be the minimum Aoki pulls to clear prefix $1 \dots i$ using at most $j$ Takahashi operations. Transitions: Aoki pulls weed $i$ ($DP[i][j] = DP[i-1][j] + 1$), or Takahashi operates on weed $i$ ($DP[i][j] = \min(DP[i][j], DP[prev[i]][j-1])$).

## 3. Step-by-Step Algorithm
1. Sort $A$ in ascending order.
2. Compute $prev[i]$ for all $i$ using two pointers.
3. Compute $DP[i][j]$ for $i \in [1, N]$ and $j \in [0, 34]$.
4. Find the smallest $j$ such that $DP[N][j] \le K$.
5. Output $j$ and $DP[N][j]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N + 35 N)`
- **Space Complexity**: `O(35 N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, K;
    if (!(cin >> N >> K)) return 0;

    vector<int> A(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }
    sort(A.begin() + 1, A.end());

    vector<int> prev_idx(N + 1, 0);
    int p = 0;
    for (int i = 1; i <= N; ++i) {
        while (p + 1 < i && A[p + 1] <= A[i] / 2) {
            p++;
        }
        prev_idx[i] = p;
    }

    const int MAX_OPS = 35;
    // dp[i][j]: min Aoki pulls to eliminate prefix i with at most j Takahashi operations
    vector<vector<int>> dp(N + 1, vector<int>(MAX_OPS, 1e9));

    for (int j = 0; j < MAX_OPS; ++j) {
        dp[0][j] = 0;
    }

    for (int i = 1; i <= N; ++i) {
        for (int j = 0; j < MAX_OPS; ++j) {
            // Option 1: Aoki pulls weed i
            dp[i][j] = dp[i - 1][j] + 1;
            // Option 2: Takahashi operates on weed i
            if (j > 0) {
                dp[i][j] = min(dp[i][j], dp[prev_idx[i]][j - 1]);
            }
        }
    }

    for (int j = 0; j < MAX_OPS; ++j) {
        if (dp[N][j] <= K) {
            cout << j << " " << dp[N][j] << "\n";
            break;
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
