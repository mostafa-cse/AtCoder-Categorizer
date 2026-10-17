# Problem Analysis: AtCoder-arc104_d — D. Multiset Mean

**Problem ID**: `AtCoder-arc104_d`  
**Contest**: `arc104`  
**Rating / Difficulty**: 2251  
**URL**: https://atcoder.jp/contests/arc104/tasks/arc104_d  
**VJudge Tag**: `[problem:AtCoder-arc104_d]`  
**Category File**: [`../categories/dp/bounded_knapsack_average_deviation_sliding_window.md`](../categories/dp/bounded_knapsack_average_deviation_sliding_window.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Subset Sum Optimizations`  

---

## 1. Problem Statement & Key Idea
Given positive integers $N, K$ and prime $M$, for every integer $x \in [1, N]$, find the number of non-empty multisets of elements from $\{1, \dots, N\}$ with multiplicity at most $K$ such that the average of the elements is $x$.

## 2. Core Observation & Invariant
The average of a multiset is $x$ if and only if the sum of deviations $\sum_{i=1}^N c_i (i - x) = 0$. For elements $i < x$, deviations are negative with weights $d = x - i \in [1, x-1]$; for elements $i > x$, deviations are positive with weights $d = i - x \in [1, N-x]$. The positive and negative deviation sums must be equal to some sum $S \ge 0$.
Let $DP[L][S]$ be the number of ways to form sum $S$ using weights $\{1, \dots, L\}$ with multiplicity $\le K$. For each $x$, the answer is $K + (K+1) \sum_{S \ge 1} DP[x-1][S] \cdot DP[N-x][S] \pmod M$. Precomputing $DP[L][S]$ takes $O(K N^3)$ via prefix sliding window.

## 3. Step-by-Step Algorithm
1. Initialize $DP[0][0] = 1$.
2. For $L = 1 \dots N$, compute $DP[L][S]$ from $DP[L-1]$ by adding item $L$ with multiplicity up to $K$ using sliding window sums modulo $L$.
3. For each $x \in [1, N]$, sum $DP[x-1][S] \cdot DP[N-x][S]$ over all valid $S > 0$.
4. Multiply by $(K + 1)$, add $K$ for the $S=0$ case, and output the result modulo $M$.

## 4. Complexity Analysis
- **Time Complexity**: `O(K N^3)`
- **Space Complexity**: `O(K N^3)`

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
    long long M;
    if (!(cin >> N >> K >> M)) return 0;

    vector<vector<int>> dp(N + 1);
    dp[0].assign(1, 1);

    for (int L = 1; L <= N; ++L) {
        int cur_max = K * L * (L + 1) / 2;
        dp[L].assign(cur_max + 1, 0);
        int prev_max = dp[L - 1].size() - 1;

        for (int r = 0; r < L; ++r) {
            long long window_sum = 0;
            for (int s = r, j = 0; s <= cur_max; s += L, ++j) {
                if (s <= prev_max) {
                    window_sum = (window_sum + dp[L - 1][s]) % M;
                }
                if (j >= K + 1) {
                    int old_s = s - (K + 1) * L;
                    if (old_s <= prev_max) {
                        window_sum = (window_sum - dp[L - 1][old_s] + M) % M;
                    }
                }
                dp[L][s] = window_sum;
            }
        }
    }

    for (int x = 1; x <= N; ++x) {
        int left_L = x - 1;
        int right_L = N - x;
        int limit = min(dp[left_L].size(), dp[right_L].size());

        long long total = 0;
        for (int s = 1; s < limit; ++s) {
            total = (total + 1LL * dp[left_L][s] * dp[right_L][s]) % M;
        }

        long long ans = (K + (K + 1) % M * total) % M;
        cout << ans << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
