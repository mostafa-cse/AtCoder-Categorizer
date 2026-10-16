# Problem Analysis: AtCoder-abc141_e — Who Says a Pun?

**Problem ID**: `AtCoder-abc141_e`  
**Contest**: `abc141`  
**Rating / Difficulty**: 1459  
**URL**: https://atcoder.jp/contests/abc141/tasks/abc141_e  
**VJudge Tag**: `[problem:AtCoder-abc141_e]`  
**Category File**: [`../categories/dp/longest_nonoverlapping_common_substring_dp.md`](../categories/dp/longest_nonoverlapping_common_substring_dp.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Longest Common Non-Overlapping Substring DP`  

---

## 1. Problem Statement & Key Idea
Given a string S of length N (N <= 5000). Find the maximum length of a string that appears at least twice in S as non-overlapping substrings.

**Key Insight**: Use 2D Dynamic Programming to compute the Longest Common Prefix (LCP) between all pairs of suffixes. If the LCP between suffix i and suffix j is L, the non-overlapping constraint restricts the valid substring length to min(L, j - i).

## 2. Core Observation & Invariant
Let dp[i][j] be the length of the longest common prefix of suffixes S[i..] and S[j..]. If S[i] == S[j], dp[i][j] = dp[i+1][j+1] + 1; otherwise 0. For i < j, non-overlapping means length <= j - i. Maximize min(dp[i][j], j - i) over all 0 <= i < j < N.

## 3. Step-by-Step Algorithm
1. Initialize dp[N+1][N+1] = 0.
2. max_len = 0.
3. Iterate i from N - 1 down to 0:
4.   Iterate j from N - 1 down to i + 1:
5.     If S[i] == S[j]:
6.       dp[i][j] = dp[i+1][j+1] + 1.
7.       max_len = max(max_len, min(dp[i][j], j - i)).
8.     Else:
9.       dp[i][j] = 0.
10. Print max_len.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string s;
    if (!(cin >> n >> s)) return 0;

    // dp[i][j] = LCP of S[i..] and S[j..]
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    int max_len = 0;

    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j > i; --j) {
            if (s[i] == s[j]) {
                dp[i][j] = dp[i + 1][j + 1] + 1;
                max_len = max(max_len, min(dp[i][j], j - i));
            } else {
                dp[i][j] = 0;
            }
        }
    }

    cout << max_len << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Longest common prefix suffix table with non-overlapping index constraint bounding.
- **Reusable Pattern**: `Non-overlapping Duplicate Substring: dp[i][j] = dp[i+1][j+1] + 1 with min(dp[i][j], j - i).`
