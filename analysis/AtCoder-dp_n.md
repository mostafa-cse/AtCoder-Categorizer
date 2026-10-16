# Problem Analysis: AtCoder-dp_n — Slimes

**Problem ID**: `AtCoder-dp_n`  
**Contest**: `dp`  
**Rating**: 1600  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_n  
**VJudge Tag**: `[problem:AtCoder-dp_n]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Merge N slimes adjacent in a line into a single slime minimizing the sum of merging costs.

## 2. Core Observation & Invariant
The final merge combines two adjacent contiguous blocks [l, k] and [k+1, r]. The merge cost is always sum(a[l..r]). Therefore: dp[l][r] = sum(a[l..r]) + min_{l <= k < r} (dp[l][k] + dp[k+1][r]).

## 3. Step-by-Step Algorithm
1. Precompute prefix sums of array a.
2. For len = 2..N: for l = 1..N-len+1: r = l+len-1: dp[l][r] = min_{k=l}^{r-1}(dp[l][k] + dp[k+1][r]) + (pref[r] - pref[l-1]).
3. Return dp[1][N].

## 4. Complexity Analysis
Time: O(N^3) standard, O(N^2) via Knuth's optimization.

## 5. Editorial Comparison & Alignment
Optimal binary search tree / matrix chain multiplication DP.

## 6. What This Problem Teaches
Interval DP with split-point minimization and cost of merging subproblems.

## 7. Reusable Competitive Programming Pattern
`Split-point interval DP.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)