# Problem Analysis: AtCoder-arc126_d — D. Pure Permutation

**Problem ID**: `AtCoder-arc126_d`  
**Contest**: `arc126`  
**Rating / Difficulty**: 2332  
**URL**: https://atcoder.jp/contests/arc126/tasks/arc126_d  
**VJudge Tag**: `[problem:AtCoder-arc126_d]`  
**Category File**: [`../categories/dynamic_programming/subsequence_permutation_clustering_bitmask_dp.md`](../categories/dynamic_programming/subsequence_permutation_clustering_bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Find the minimum operations to form a contiguous subsegment containing a permutation of $1 \dots K$. Bitmask DP over subset of chosen elements adds inversion counts and median clustering costs in $O(N 2^K)$.

## 2. Core Observation & Invariant
The cost to bring $K$ chosen elements together and sort them equals the number of inversions between them plus the number of skips required to cluster them adjacent to their median. In a bitmask DP over the set of chosen values, skipping an unchosen element costs $\min(c, K - c)$ where $c = \text{popcount}(mask)$.

## 3. Step-by-Step Algorithm
1. Define $dp[mask]$ as the minimum cost to form the subset of chosen values indicated by $mask \in [0, 2^K - 1]$.
2. For each element $A_i = v$, transition: either skip $A_i$ adding $\min(c, K - c)$, or choose $A_i$ transitioning from $mask$ to $mask \mid 2^v$ adding $\text{popcount}(mask \gg (v + 1))$ inversions.
3. Evaluate all $N$ elements across $2^K$ masks in $O(N 2^K)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N 2^K)`
- **Space Complexity**: `O(2^K)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    const int INF = 1e9;
    int num_masks = 1 << k;
    vector<int> dp(num_masks, INF);
    dp[0] = 0;

    vector<int> popcnt(num_masks);
    for (int mask = 0; mask < num_masks; ++mask) {
        popcnt[mask] = __builtin_popcount(mask);
    }

    for (int x : a) {
        int v = x - 1;
        vector<int> next_dp(num_masks, INF);
        // Option 1: don't pick
        for (int mask = 0; mask < num_masks; ++mask) {
            if (dp[mask] != INF) {
                int c = popcnt[mask];
                next_dp[mask] = min(next_dp[mask], dp[mask] + min(c, k - c));
            }
        }
        // Option 2: pick x
        for (int mask = 0; mask < num_masks; ++mask) {
            if (dp[mask] != INF && !((mask >> v) & 1)) {
                int new_mask = mask | (1 << v);
                int inv = __builtin_popcount(mask >> (v + 1));
                next_dp[new_mask] = min(next_dp[new_mask], dp[mask] + inv);
            }
        }
        dp = std::move(next_dp);
    }

    cout << dp[(1 << k) - 1] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
