# Problem Analysis: AtCoder-dp_m — Candies

**Problem ID**: `AtCoder-dp_m`  
**Contest**: `dp`  
**Rating**: 1550  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_m  
**VJudge Tag**: `[problem:AtCoder-dp_m]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Prefix Sum Optimized DP`  

---

## 1. Problem Statement & Key Idea
Distribute K candies among N children such that child i receives at most a_i candies.

## 2. Core Observation & Invariant
Naively, dp[i][j] = sum_{k=0}^{a_i} dp[i-1][j-k] requires O(N * K^2). The inner sum is over a contiguous range [max(0, j - a_i), j] in the previous row, which prefix sums compute in O(1).

## 3. Step-by-Step Algorithm
1. dp[0] = 1, others 0.
2. For each child i: compute prefix sums pref of current dp.
3. dp[j] = (pref[j+1] - pref[max(0, j - a_i)]) mod MOD.
4. Return dp[K].

## 4. Complexity Analysis
Time: O(N * K), Space: O(K).

## 5. Editorial Comparison & Alignment
Prefix sum state acceleration.

## 6. What This Problem Teaches
Sliding window range sum optimization reducing quadratic transitions to linear.

## 7. Reusable Competitive Programming Pattern
`Prefix sum acceleration of contiguous state transitions.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)