# Problem Analysis: AtCoder-dp_o — Matching

**Problem ID**: `AtCoder-dp_o`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1650  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_o  
**VJudge Tag**: `[problem:AtCoder-dp_o]`  
**Category File**: [`../categories/dp/bitmask_dp.md`](../categories/dp/bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Count perfect matchings in a bipartite graph with N men and N women (N <= 21).

**Core Idea**: When matching men 0, 1, ..., i-1, exactly i women must be chosen. Thus, i = popcount(mask). The index of the active man is implicit in the bitmask!

## 2. Core Observation & Invariant
By iterating masks by popcount or sequentially from 0 to 2^N - 1, we eliminate the man dimension entirely: dp[mask | (1 << j)] += dp[mask].

## 3. Step-by-Step Algorithm
1. dp[0] = 1, all other dp = 0.
2. For mask from 0 to 2^N - 1: let i = popcount(mask). If i == N, continue.
3. For each woman j in 0..N-1: if compatible(i, j) and not (mask & (1 << j)): dp[mask | (1 << j)] = (dp[mask | (1 << j)] + dp[mask]) mod MOD.
4. Return dp[(1<<N) - 1].

## 4. Complexity Analysis
Time: O(N * 2^N), Space: O(2^N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) cin >> a[i][j];
    }

    int total_masks = 1 << n;
    vector<int> dp(total_masks, 0);
    dp[0] = 1;

    for (int mask = 0; mask < total_masks; ++mask) {
        if (dp[mask] == 0) continue;
        int i = __builtin_popcount(mask);
        if (i == n) continue;

        for (int j = 0; j < n; ++j) {
            if (a[i][j] && !(mask & (1 << j))) {
                int next_mask = mask | (1 << j);
                dp[next_mask] = (dp[next_mask] + dp[mask]) % MOD;
            }
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Popcount dimension-reduced bitmask DP.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Dimension reduction in Bitmask DP using subset cardinality invariants.
- **Reusable Pattern**: `Popcount implicit state matching: i = popcount(mask).`

---
Back to [Bitmask DP](../categories/dp/bitmask_dp.md) | [Categories Directory](../categories/README.md)