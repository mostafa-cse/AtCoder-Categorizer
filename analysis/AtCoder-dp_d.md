# Problem Analysis: AtCoder-dp_d — Knapsack 1

**Problem ID**: `AtCoder-dp_d`  
**Contest**: `dp`  
**Rating**: 1150  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_d  
**VJudge Tag**: `[problem:AtCoder-dp_d]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Maximize total value of items within knapsack capacity W <= 10^5 where each item can be selected at most once.

## 2. Core Observation & Invariant
Capacity is moderate (W <= 10^5). By iterating weight downwards from W to w_i, 1D array space is sufficient without using an item multiple times.

## 3. Step-by-Step Algorithm
1. Initialize dp[0..W] = 0.
2. For each item (w_i, v_i): for cap from W down to w_i: dp[cap] = max(dp[cap], dp[cap - w_i] + v_i).
3. Result is max(dp).

## 4. Complexity Analysis
Time: O(N * W), Space: O(W).

## 5. Editorial Comparison & Alignment
Textbook 0/1 Knapsack with 1D memory compression.

## 6. What This Problem Teaches
Reverse-order state traversal to prevent unbounded repetition in subset selection.

## 7. Reusable Competitive Programming Pattern
`1D space-optimized 0/1 knapsack.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)