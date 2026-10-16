# Problem Analysis: AtCoder-abc142_e — Get Everything

**Problem ID**: `AtCoder-abc142_e`  
**Contest**: `abc142`  
**Rating / Difficulty**: 1397  
**URL**: https://atcoder.jp/contests/abc142/tasks/abc142_e  
**VJudge Tag**: `[problem:AtCoder-abc142_e]`  
**Category File**: [`../categories/dp/set_cover_bitmask_dp.md`](../categories/dp/set_cover_bitmask_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Bitmask DP`  
- **Topic (Skill)**: `Exact Set Cover Shortest Path / Bitmask Knapsack DP`  

---

## 1. Problem Statement & Key Idea
N treasure boxes and M keys (N <= 12). Key i costs a_i yen and unlocks a subset of boxes c_1..c_b. Find the minimum cost to unlock all N boxes (or -1 if impossible).

**Key Idea**: Each key unlocks a subset of boxes represented by a bitmask of length N. This is the classic Minimum Weight Set Cover Problem.

## 2. Core Observation & Invariant
Because N <= 12, the total number of states is 2^N <= 4096. Define dp[mask] = minimum cost to unlock the subset of boxes in mask. Base case: dp[0] = 0. For each key with cost a and mask key_mask: for each state s from 0 to 2^N - 1: dp[s | key_mask] = min(dp[s | key_mask], dp[s] + a).

## 3. Step-by-Step Algorithm
1. Initialize dp array of size (1 << N) to INF; dp[0] = 0.
2. For each key (cost, key_mask):
3.   For mask from (1 << N) - 1 down to 0:
4.     dp[mask | key_mask] = min(dp[mask | key_mask], dp[mask] + cost).
5. Output dp[(1 << N) - 1] (or -1 if INF).

## 4. Complexity Analysis
- **Time Complexity**: `O(M * 2^N)`
- **Space Complexity**: `O(2^N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e15;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    int total_masks = 1 << n;
    vector<long long> dp(total_masks, INF);
    dp[0] = 0;

    for (int i = 0; i < m; ++i) {
        long long cost;
        int b;
        cin >> cost >> b;
        int key_mask = 0;
        for (int j = 0; j < b; ++j) {
            int box;
            cin >> box;
            key_mask |= (1 << (box - 1));
        }

        for (int mask = 0; mask < total_masks; ++mask) {
            if (dp[mask] == INF) continue;
            int nxt = mask | key_mask;
            dp[nxt] = min(dp[nxt], dp[mask] + cost);
        }
    }

    long long ans = dp[total_masks - 1];
    cout << (ans == INF ? -1 : ans) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bitmask shortest path / Set Cover dynamic programming.
- **Reusable Pattern**: `Set cover bitmask: dp[mask | key] = min(dp[mask | key], dp[mask] + cost).`
