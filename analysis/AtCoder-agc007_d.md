# Problem Analysis: AtCoder-agc007_d — D - Shik and Game

**Problem ID**: `AtCoder-agc007_d`  
**Contest**: `agc007`  
**Rating / Difficulty**: 2754  
**URL**: https://atcoder.jp/contests/agc007/tasks/agc007_d  
**VJudge Tag**: `[problem:AtCoder-agc007_d]`  
**Category File**: [`../categories/dynamic_programming_dp/shik_and_game_dp_queue_optimization.md`](../categories/dynamic_programming_dp/shik_and_game_dp_queue_optimization.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `DP Optimization using Data Structures [Some Practice Problems]`  

---

## 1. Problem Statement & Key Idea
There are N bears at coordinates x_1 < x_2 < ... < x_N on a line of length E. When Shik gives a candy to a bear, it produces a coin after time T. Shik starts at 0, must collect all coins, and reach E. Find the minimum time to collect all coins and reach E.

## 2. Core Observation & Invariant
Shik collects coins in contiguous segments. If Shik gives candies to bears j+1 through i and then returns to collect their coins, the extra turnaround time is max(T, 2 * (x_i - x_{j+1})). The DP transition is: DP[i] = min_{0 <= j < i} (DP[j] - x_j + x_i + max(T, 2 * (x_i - x_{j+1}))). For a given i, the condition 2 * (x_i - x_{j+1}) <= T is monotonic in j. Thus, there is a threshold p such that for j < p, the turnaround cost is 2 * (x_i - x_{j+1}), and for j >= p, the cost is T. For j < p, the transition simplifies to DP[j] - x_j + 3 * x_i - 2 * x_{j+1}, which is optimized by maintaining the prefix minimum of DP[j] - x_j - 2 * x_{j+1}. For j >= p, it simplifies to DP[j] - x_j + x_i + T, optimized by maintaining the prefix minimum of DP[j] - x_j. This allows computing DP[i] in O(1) amortized time.

## 3. Step-by-Step Algorithm
1. 1. Initialize DP[0] = 0 and pointers for two-pointer deque maintenance.
2. 2. Maintain prefix minimums for DP[j] - x_j and DP[j] - x_j - 2 * x_{j+1}.
3. 3. As i advances, increase pointer p while 2 * (x_i - x_{p+1}) > T.
4. 4. Compute DP[i] as the minimum of the two optimized cases.
5. 5. Answer is DP[N] + (E - x_N).

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long E, T;
    if (!(cin >> n >> E >> T)) return 0;

    vector<long long> X(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        cin >> X[i];
    }

    vector<long long> dp(n + 1, 0);

    const long long INF = 4e18; // 4 * 10^18 to prevent overflow
    long long min_part1 = INF;
    deque<int> q;
    int p = 0;

    for (int i = 1; i <= n; i++) {
        int j_add = i - 1;
        long long val_add = dp[j_add] - X[j_add];
        while (!q.empty() && (dp[q.back()] - X[q.back()]) >= val_add) {
            q.pop_back();
        }
        q.push_back(j_add);

        while (p < i && 2 * (X[i] - X[p + 1]) > T) {
            long long val_p1 = dp[p] - X[p] - 2 * X[p + 1];
            if (val_p1 < min_part1) min_part1 = val_p1;
            if (!q.empty() && q.front() == p) {
                q.pop_front();
            }
            p++;
        }

        long long best = INF;
        if (min_part1 != INF) {
            best = min(best, min_part1 + 3 * X[i]);
        }
        if (!q.empty()) {
            best = min(best, dp[q.front()] - X[q.front()] + X[i] + T);
        }

        dp[i] = best;
    }

    long long ans = dp[n] + (E - X[n]);
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
