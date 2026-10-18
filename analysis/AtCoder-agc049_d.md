# Problem Analysis: AtCoder-agc049_d — D. Convex Sequence

**Problem ID**: `AtCoder-agc049_d`  
**Contest**: `agc049`  
**Rating / Difficulty**: 2602  
**URL**: https://atcoder.jp/contests/agc049/tasks/agc049_d  
**VJudge Tag**: `[problem:AtCoder-agc049_d]`  
**Category File**: [`../categories/dynamic_programming_dp/convex_sequence_second_difference_knapsack.md`](../categories/dynamic_programming_dp/convex_sequence_second_difference_knapsack.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Subset Sum Optimizations`  

---

## 1. Problem Statement & Key Idea
Count the number of non-negative integer sequences A of length N summing to M such that 2 A_i <= A_{i-1} + A_{i+1} for all 2 <= i <= N-1 (convexity), modulo 10^9+7.

## 2. Core Observation & Invariant
Any convex sequence is uniquely determined by its leftmost minimum at index m, plus a flat base of weight N, rays of weights k(k+1)/2 to the left (requiring ray m-1 at least once if m > 1), and rays of weights j(j+1)/2 to the right. Since weights grow quadratically, only at most sqrt(2M) <= 450 distinct item weights can ever be used.

## 3. Step-by-Step Algorithm
1. Precompute triangular numbers T[k] <= M. Maintain an unbounded knapsack DP array of size M+1.
2. Initialize DP with base item N and right rays for m = 1.
3. For each m from 2 to N: add item T[m-2] to left items, and remove item T[N-m] from right items (via O(M) knapsack undo). Add dp[M - (m-1)m/2] to total answer.

## 4. Complexity Analysis
- **Time Complexity**: `O(M sqrt(M))`
- **Space Complexity**: `O(M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<int> T;
    for (int k = 1; ; ++k) {
        long long val = (long long)k * (k + 1) / 2;
        if (val > M) break;
        T.push_back((int)val);
    }
    int K_MAX = (int)T.size();

    vector<int> dp(M + 1, 0);
    dp[0] = 1;

    auto add_item = [&](int w) {
        for (int v = w; v <= M; ++v) {
            dp[v] += dp[v - w];
            if (dp[v] >= MOD) dp[v] -= MOD;
        }
    };

    auto remove_item = [&](int w) {
        for (int v = M; v >= w; --v) {
            dp[v] -= dp[v - w];
            if (dp[v] < 0) dp[v] += MOD;
        }
    };

    if (N <= M) {
        add_item(N);
    }

    int right_limit = min(N - 1, K_MAX);
    for (int j = 0; j < right_limit; ++j) {
        add_item(T[j]);
    }

    long long ans = 0;
    // m = 1
    ans = (ans + dp[M]) % MOD;

    for (int m = 2; m <= N; ++m) {
        long long req = (long long)(m - 1) * m / 2;
        if (req > M) break;

        // Left: add T[m - 2]
        add_item(T[m - 2]);

        // Right: remove T[N - m] if it was included
        if (N - m < K_MAX) {
            remove_item(T[N - m]);
        }

        ans = (ans + dp[M - (int)req]) % MOD;
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
