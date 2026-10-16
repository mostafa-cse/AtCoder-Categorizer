# Problem Analysis: AtCoder-typical90_as — Simple Grouping

**Problem ID**: `AtCoder-typical90_as`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 045)  
**Rating / Difficulty**: 2150 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_as  
**VJudge Tag**: `[problem:AtCoder-typical90_as]`  
**Category File**: [`../categories/dp/bitmask_dp.md`](../categories/dp/bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Minimax Subset Partition Bitmask DP with O(3^N) Submask Iteration`  

---

## 1. Problem Statement & Key Idea
N points in 2D plane (N <= 15). Partition points into K non-empty groups. Cost of a group is the maximum squared distance between any pair of points in the group. Minimize the maximum cost among all K groups.

**Core Idea**: Precompute standalone group costs in O(N^2 * 2^N), then solve minimax subset partition DP in O(K * 3^N).

## 2. Core Observation & Invariant
dp[k][mask] = min_{sub in mask} max(dp[k - 1][mask ^ sub], cost[sub]). Submask iteration sub = (sub - 1) & mask iterates all submasks in sum binom(N, i) 2^i = 3^N operations.

## 3. Step-by-Step Algorithm
1. Precompute cost[mask] for all 2^N subsets.
2. dp[1][mask] = cost[mask].
3. For step from 2 to K: for mask from 1 to 2^N - 1:
   sub = (mask - 1) & mask; while sub > 0: dp[step][mask] = min(dp[step][mask], max(dp[step - 1][mask ^ sub], cost[sub])); sub = (sub - 1) & mask.
4. Output dp[K][(1<<N) - 1].

## 4. Complexity Analysis
Time: O(K * 3^N + N^2 * 2^N), Space: O(K * 2^N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 4e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<pair<long long, long long>> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].first >> pts[i].second;
    }

    int total_masks = 1 << n;
    vector<long long> cost(total_masks, 0);

    for (int mask = 0; mask < total_masks; ++mask) {
        long long max_d2 = 0;
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) continue;
            for (int j = i + 1; j < n; ++j) {
                if (!(mask & (1 << j))) continue;
                long long dx = pts[i].first - pts[j].first;
                long long dy = pts[i].second - pts[j].second;
                max_d2 = max(max_d2, dx * dx + dy * dy);
            }
        }
        cost[mask] = max_d2;
    }

    vector<vector<long long>> dp(k + 1, vector<long long>(total_masks, INF));
    for (int mask = 1; mask < total_masks; ++mask) {
        dp[1][mask] = cost[mask];
    }

    for (int step = 2; step <= k; ++step) {
        for (int mask = 1; mask < total_masks; ++mask) {
            for (int sub = (mask - 1) & mask; sub > 0; sub = (sub - 1) & mask) {
                dp[step][mask] = min(dp[step][mask],
                                     max(dp[step - 1][mask ^ sub], cost[sub]));
            }
        }
    }

    cout << dp[k][total_masks - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
O(3^N) submask iteration for minimax set partition DP.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Minimax set partition dynamic programming, submask iteration idiom, and precomputing subset metric diameters.
- **Reusable Pattern**: `O(3^N) Minimax Subset Partition DP.`

---
Back to [Minimax Subset Partition Bitmask DP with O(3^N) Submask Iteration](../categories/dp/bitmask_dp.md) | [Categories Directory](../categories/README.md)