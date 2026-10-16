# Problem Analysis: AtCoder-dp_u — Grouping

**Problem ID**: `AtCoder-dp_u`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1850  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_u  
**VJudge Tag**: `[problem:AtCoder-dp_u]`  
**Category File**: [`../categories/dp/bitmask_dp.md`](../categories/dp/bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP / O(3^N) Submask Enumeration`  

---

## 1. Problem Statement & Key Idea
Partition N rabbits into arbitrary groups to maximize total compatibility score (N <= 16).

**Core Idea**: Precompute standalone group scores in O(N^2 * 2^N). Then dp[mask] = max_{sub is submask of mask} (score[sub] + dp[mask ^ sub]).

## 2. Core Observation & Invariant
Iterating submasks via `sub = (sub - 1) & mask` visits each submask without redundant branches. Over all 2^N masks, total operations equal sum_{k=0}^N binom(N, k) 2^k = 3^N.

## 3. Step-by-Step Algorithm
1. Precompute score[mask] for all 2^N subsets.
2. Loop mask from 1 to 2^N - 1:
   sub = mask; while sub > 0: dp[mask] = max(dp[mask], score[sub] + dp[mask ^ sub]); sub = (sub - 1) & mask.
3. Return dp[(1<<N) - 1].

## 4. Complexity Analysis
Time: O(3^N + N^2 * 2^N), Space: O(2^N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<long long>> a(n, vector<long long>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> a[i][j];
    }

    int total_masks = 1 << n;
    vector<long long> score(total_masks, 0);

    for (int mask = 0; mask < total_masks; ++mask) {
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) continue;
            for (int j = i + 1; j < n; ++j) {
                if (mask & (1 << j)) {
                    score[mask] += a[i][j];
                }
            }
        }
    }

    vector<long long> dp(total_masks, 0);

    for (int mask = 1; mask < total_masks; ++mask) {
        for (int sub = mask; sub > 0; sub = (sub - 1) & mask) {
            dp[mask] = max(dp[mask], score[sub] + dp[mask ^ sub]);
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Textbook submask enumeration.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: The (sub - 1) & mask bit trick and set partition dynamic programming.
- **Reusable Pattern**: `O(3^N) submask iteration: sub = (sub - 1) & mask.`

---
Back to [Bitmask DP / O(3^N) Submask Enumeration](../categories/dp/bitmask_dp.md) | [Categories Directory](../categories/README.md)