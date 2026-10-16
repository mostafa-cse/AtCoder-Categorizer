# Problem Analysis: AtCoder-dp_d — Knapsack 1

**Problem ID**: `AtCoder-dp_d`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1150  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_d  
**VJudge Tag**: `[problem:AtCoder-dp_d]`  
**Category File**: [`../categories/dp/knapsack.md`](../categories/dp/knapsack.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Given N items with weights w_i and values v_i, choose items with total weight <= W (W <= 10^5) maximizing total value.

**Core Idea**: Classical 0/1 Knapsack where capacity W <= 10^5 serves as the DP state index.

## 2. Core Observation & Invariant
By iterating weight downwards from W to w_i, 1D array space is sufficient without using an item multiple times.

## 3. Step-by-Step Algorithm
1. Initialize dp[0..W] = 0.
2. For each item (w_i, v_i): for cap from W down to w_i: dp[cap] = max(dp[cap], dp[cap - w_i] + v_i).
3. Result is max(dp).

## 4. Complexity Analysis
Time: O(N * W), Space: O(W).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, W;
    if (!(cin >> n >> W)) return 0;

    vector<long long> dp(W + 1, 0);

    for (int i = 0; i < n; ++i) {
        int w;
        long long v;
        cin >> w >> v;
        for (int cap = W; cap >= w; --cap) {
            dp[cap] = max(dp[cap], dp[cap - w] + v);
        }
    }

    cout << dp[W] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Textbook 0/1 Knapsack with 1D memory compression.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Reverse-order state traversal to prevent unbounded repetition in subset selection.
- **Reusable Pattern**: `1D space-optimized 0/1 knapsack.`

---
Back to [Knapsack and Basic Dynamic Programming](../categories/dp/knapsack.md) | [Categories Directory](../categories/README.md)