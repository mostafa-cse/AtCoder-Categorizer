# Problem Analysis: AtCoder-abc041_d — Footrace

**Problem ID**: `AtCoder-abc041_d`  
**Contest**: `abc041`  
**Rating / Difficulty**: 1670  
**URL**: https://atcoder.jp/contests/abc041/tasks/abc041_d  
**VJudge Tag**: `[problem:AtCoder-abc041_d]`  
**Category File**: [`../categories/dp/topological_sort_count_bitmask_dp.md`](../categories/dp/topological_sort_count_bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Bitmask DP`  
- **Topic (Skill)**: `Topological Ordering Count via Bitmask DP`  

---

## 1. Problem Statement & Key Idea
N runners (N <= 16) and M precedence conditions: runner x_i finished before runner y_i. Find the total number of valid finishing orders (topological sorts) compatible with all conditions.

**Key Insight**: Dynamic programming on subsets! `dp[mask]` = number of valid topological orderings of the subset of runners in mask. To transition, append a runner v not in mask provided no predecessor of v is missing from mask.

## 2. Core Observation & Invariant
A runner v can be placed next iff all runners that must precede v are ALREADY present in mask: `(pred[v] & ~mask) == 0`. Then `dp[mask | (1 << v)] += dp[mask]`.

## 3. Step-by-Step Algorithm
1. Store predecessor bitmask pred[v]: bit u is set if u must precede v.
2. Initialize dp[1 << N] with 0; dp[0] = 1.
3. For mask from 0 to (1 << N) - 1:
4.   If dp[mask] == 0 continue.
5.   For v from 0 to N - 1:
6.     If (!(mask & (1 << v))):
7.       If ((pred[v] & ~mask) == 0):
8.         dp[mask | (1 << v)] += dp[mask];
9. Print dp[(1 << N) - 1].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> pred(n, 0);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        pred[v] |= (1 << u);
    }

    int total_masks = 1 << n;
    vector<long long> dp(total_masks, 0);
    dp[0] = 1;

    for (int mask = 0; mask < total_masks; ++mask) {
        if (!dp[mask]) continue;

        for (int v = 0; v < n; ++v) {
            if (!(mask & (1 << v))) {
                if ((pred[v] & ~mask) == 0) {
                    dp[mask | (1 << v)] += dp[mask];
                }
            }
        }
    }

    cout << dp[total_masks - 1] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting linear extensions of partially ordered sets via Bitmask DP.
- **Reusable Pattern**: `Topological Sort Count Bitmask DP: append v if (pred[v] & ~mask) == 0.`
