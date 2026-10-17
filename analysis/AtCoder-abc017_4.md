# Problem Analysis: AtCoder-abc017_4 — サプリメント

**Problem ID**: `AtCoder-abc017_4`  
**Contest**: `abc017`  
**Rating / Difficulty**: 1956  
**URL**: https://atcoder.jp/contests/abc017/tasks/abc017_4  
**VJudge Tag**: `[problem:AtCoder-abc017_4]`  
**Category File**: [`../categories/dp/non_duplicate_partition_prefix_sum_dp.md`](../categories/dp/non_duplicate_partition_prefix_sum_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Two Pointers / Prefix Sum DP`  
- **Topic (Skill)**: `Non-Duplicate Contiguous Partition DP Accelerated by Monotonic Left-Bound Prefix Sums`  

---

## 1. Problem Statement & Key Idea
Given N supplements of types f_1, ..., f_N. Partition the sequence into contiguous packs such that no pack contains duplicate supplement types. Find the number of valid partitionings modulo 10^9 + 7.

Let dp[i] be the number of valid partitions of prefix 1..i. dp[i] = sum_{j = L_i}^{i - 1} dp[j], where L_i is the smallest index such that subarray f[L_i + 1..i] contains no duplicates. The boundary L_i is monotonically non-decreasing: L_i = max(L_{i-1}, last_pos[f_i]). Because L_i is monotonic, the transition is a range sum query over dp[L_i..i-1], maintained in O(1) via prefix sums of dp.

## 2. Core Observation & Invariant
Monotonicity of valid left boundaries enables O(1) DP transitions via prefix sums.

## 3. Step-by-Step Algorithm
1. Initialize dp[0] = 1, pref[0] = 0, pref[1] = 1.
2. Maintain last_pos[type] initialized to 0.
3. L = 0.
4. For i = 1 to N:
5.   L = max(L, last_pos[f[i]]).
6.   dp[i] = (pref[i] - pref[L] + MOD) % MOD.
7.   pref[i + 1] = (pref[i] + dp[i]) % MOD.
8.   last_pos[f[i]] = i.
9. Print dp[N].

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N + M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> f(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> f[i];
    }

    vector<int> dp(n + 1, 0);
    vector<int> pref(n + 2, 0);
    vector<int> last_pos(m + 1, 0);

    dp[0] = 1;
    pref[1] = 1;

    int L = 0;
    for (int i = 1; i <= n; ++i) {
        L = max(L, last_pos[f[i]]);
        dp[i] = (pref[i] - pref[L] + MOD) % MOD;
        pref[i + 1] = (pref[i] + dp[i]) % MOD;
        last_pos[f[i]] = i;
    }

    cout << dp[n] << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Combining two-pointer monotonic boundaries with prefix sum arrays for linear-time partition DP.
- **Reusable Pattern**: `Non-Duplicate Partition DP: L = max(L, last_seen[val]), dp[i] = pref[i] - pref[L].`
