# Problem Analysis: AtCoder-dp_f — LCS

**Problem ID**: `AtCoder-dp_f`  
**Contest**: `dp`  
**Rating**: 1250  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_f  
**VJudge Tag**: `[problem:AtCoder-dp_f]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Longest Common Subsequence & Backtracking`  

---

## 1. Problem Statement & Key Idea
Reconstruct and print the actual string corresponding to the Longest Common Subsequence of strings s and t.

## 2. Core Observation & Invariant
Standard 2D table computes optimal lengths. The sequence itself is uniquely extracted by tracing back from (len(s), len(t)) following optimal transition choices.

## 3. Step-by-Step Algorithm
1. Compute dp[i][j]: if s[i-1] == t[j-1] -> dp[i-1][j-1]+1; else max(dp[i-1][j], dp[i][j-1]).
2. Traceback: if s[i-1] == t[j-1]: append s[i-1], i--, j--; else if dp[i-1][j] >= dp[i][j-1]: i--; else j--.
3. Reverse characters.

## 4. Complexity Analysis
Time: O(|s| * |t|), Space: O(|s| * |t|).

## 5. Editorial Comparison & Alignment
Full 2D DP matrix traceback.

## 6. What This Problem Teaches
State path reconstruction and multi-dimensional backtracking.

## 7. Reusable Competitive Programming Pattern
`Optimal decision matrix traceback.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)