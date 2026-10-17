# Problem Analysis: AtCoder-arc180_c — Subsequence and Prefix Sum

**Problem ID**: `AtCoder-arc180_c`  
**Contest**: `arc180`  
**Rating / Difficulty**: 2221  
**URL**: https://atcoder.jp/contests/arc180/tasks/arc180_c  
**VJudge Tag**: `[problem:AtCoder-arc180_c]`  
**Category File**: [`../categories/dp/subsequence_cumulative_sums_distinct_canonical_dp.md`](../categories/dp/subsequence_cumulative_sums_distinct_canonical_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Count the number of distinct sequences obtainable by replacing a chosen non-empty subsequence with its cumulative prefix sums.

## 2. Core Observation & Invariant
Only elements where the added cumulative sum is non-zero actually change. To avoid double-counting distinct subsequences producing the same modified array, canonicalize transitions: maintain dp1[i][j] (number of valid modified prefixes ending at i with current cumulative sum j) and dp2[i][j] (count where the last selected element was j, meaning sum before was 0). When transitioning from sum 0, subtract dp2[i][a_{i+1}] to eliminate duplicate prefix sums.

## 3. Step-by-Step Algorithm
1. 1. Initialize dp1[0][OFFSET] = 1, all others 0 (OFFSET = 1100).
2. 2. For each element x in A:
3.    - Copy dp1 and dp2 to next states.
4.    - For each non-zero running sum j != 0: transition next_dp1[j + x] += dp1[j].
5.    - For running sum j == 0: if x != 0, compute diff = dp1[0] - dp2[x], update next_dp1[x] += diff and set next_dp2[x] = dp1[0].
6. 3. The total number of distinct achievable sequences is sum(dp1) - sum(dp2) modulo 10^9+7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * max|A_i|)`
- **Space Complexity**: `O(N * max|A_i|)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

static const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    const int OFFSET = 1100;
    const int MAX_V = 2300;

    vector<int> dp1(MAX_V, 0);
    vector<int> dp2(MAX_V, 0);
    dp1[OFFSET] = 1;

    for (int x : a) {
        vector<int> next_dp1 = dp1;
        vector<int> next_dp2 = dp2;

        for (int j = -1050; j <= 1050; ++j) {
            if (j == 0) continue;
            int v = dp1[OFFSET + j];
            if (v) {
                int nj = j + x;
                next_dp1[OFFSET + nj] = (next_dp1[OFFSET + nj] + v) % MOD;
            }
        }

        if (x != 0) {
            int diff = (dp1[OFFSET + 0] - dp2[OFFSET + x] + MOD) % MOD;
            next_dp1[OFFSET + x] = (next_dp1[OFFSET + x] + diff) % MOD;
            next_dp2[OFFSET + x] = dp1[OFFSET + 0];
        }

        dp1 = move(next_dp1);
        dp2 = move(next_dp2);
    }

    long long sum1 = 0, sum2 = 0;
    for (int v : dp1) sum1 = (sum1 + v) % MOD;
    for (int v : dp2) sum2 = (sum2 + v) % MOD;

    long long ans = (sum1 - sum2 + MOD) % MOD;
    cout << ans << "\n";

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
