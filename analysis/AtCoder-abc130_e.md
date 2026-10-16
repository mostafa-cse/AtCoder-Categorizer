# Problem Analysis: AtCoder-abc130_e — Common Subsequence

**Problem ID**: `AtCoder-abc130_e`  
**Contest**: `abc130`  
**Rating / Difficulty**: 1676  
**URL**: https://atcoder.jp/contests/abc130/tasks/abc130_e  
**VJudge Tag**: `[problem:AtCoder-abc130_e]`  
**Category File**: [`../categories/dp/common_subsequence_count_2d_dp.md`](../categories/dp/common_subsequence_count_2d_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `2D DP Counting Common Subsequences with 2D Prefix Sums`  

---

## 1. Problem Statement & Key Idea
Given two integer sequences S (length N) and T (length M). Find the number of pairs of subsequences of S and T that are identical, modulo 10^9 + 7.

**Key Insight**: 2D DP with 2D prefix sums. `dp[i][j]` = number of pairs of identical subsequences using prefixes S[1..i] and T[1..j].

## 2. Core Observation & Invariant
Inclusion-Exclusion recurrence on grid: dp[i][j] = (dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]) % MOD. If S[i] == T[j], matching this pair creates new common subsequences with all previously known ones plus the empty sequence: dp[i][j] = (dp[i][j] + dp[i-1][j-1] + 1) % MOD.

## 3. Step-by-Step Algorithm
1. Initialize dp[N + 1][M + 1] = 0.
2. For i from 1 to N:
3.   For j from 1 to M:
4.     dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + MOD) % MOD;
5.     if (S[i] == T[j]):
6.       dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] + 1) % MOD;
7. Print (dp[N][M] + 1) % MOD (including empty subsequence pair).

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N * M)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> s(n + 1), t(m + 1);
    for (int i = 1; i <= n; ++i) cin >> s[i];
    for (int j = 1; j <= m; ++j) cin >> t[j];

    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + MOD) % MOD;
            if (s[i] == t[j]) {
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] + 1) % MOD;
            }
        }
    }

    // Including the empty pair
    cout << (dp[n][m] + 1) % MOD << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Counting common subsequences via 2D prefix sum inclusion-exclusion.
- **Reusable Pattern**: `Common Subsequence Counter: dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + (S[i]==T[j] ? dp[i-1][j-1] + 1 : 0).`
