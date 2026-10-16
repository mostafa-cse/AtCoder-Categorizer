# Problem Analysis: AtCoder-dp_f — LCS

**Problem ID**: `AtCoder-dp_f`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1250  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_f  
**VJudge Tag**: `[problem:AtCoder-dp_f]`  
**Category File**: [`../categories/dp/interval_dp.md`](../categories/dp/interval_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Longest Common Subsequence & Backtracking`  

---

## 1. Problem Statement & Key Idea
Given two strings s and t, find and print the actual string corresponding to their Longest Common Subsequence.

**Core Idea**: Reconstruct and print the actual string corresponding to the Longest Common Subsequence of strings s and t.

## 2. Core Observation & Invariant
Standard 2D table computes optimal lengths. The sequence itself is uniquely extracted by tracing back from (len(s), len(t)) following optimal transition choices.

## 3. Step-by-Step Algorithm
1. Compute dp[i][j]: if s[i-1] == t[j-1] -> dp[i-1][j-1]+1; else max(dp[i-1][j], dp[i][j-1]).
2. Traceback: if s[i-1] == t[j-1]: append s[i-1], i--, j--; else if dp[i-1][j] >= dp[i][j-1]: i--; else j--.
3. Reverse characters.

## 4. Complexity Analysis
Time: O(|s| * |t|), Space: O(|s| * |t|).

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

    string s, t;
    if (!(cin >> s >> t)) return 0;

    int n = s.size();
    int m = t.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    string lcs = "";
    int i = n, j = m;
    while (i > 0 && j > 0) {
        if (s[i - 1] == t[j - 1]) {
            lcs += s[i - 1];
            --i;
            --j;
        } else if (dp[i - 1][j] >= dp[i][j - 1]) {
            --i;
        } else {
            --j;
        }
    }

    reverse(lcs.begin(), lcs.end());
    cout << lcs << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Full 2D DP matrix traceback.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: State path reconstruction and multi-dimensional backtracking.
- **Reusable Pattern**: `Optimal decision matrix traceback.`

---
Back to [Longest Common Subsequence & Backtracking](../categories/dp/interval_dp.md) | [Categories Directory](../categories/README.md)