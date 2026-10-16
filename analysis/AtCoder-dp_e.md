# Problem Analysis: AtCoder-dp_e — Knapsack 2

**Problem ID**: `AtCoder-dp_e`  
**Contest**: `dp`  
**Rating**: 1450  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_e  
**VJudge Tag**: `[problem:AtCoder-dp_e]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack Dual State / Value as State`  

---

## 1. Problem Statement & Key Idea
Solve 0/1 Knapsack when capacity W <= 10^9 is enormous, but item values v_i <= 1000 and N <= 100.

## 2. Core Observation & Invariant
Max total value V_max <= 100 * 1000 = 10^5. Invert the DP formulation: define dp[v] as the minimum weight required to achieve exact total value v.

## 3. Step-by-Step Algorithm
1. Let V_sum = sum(v_i). dp[0] = 0, dp[1..V_sum] = INF.
2. For each item (w_i, v_i): for v from V_sum down to v_i: dp[v] = min(dp[v], dp[v - v_i] + w_i).
3. Return max v such that dp[v] <= W.

## 4. Complexity Analysis
Time: O(N * sum(V)), Space: O(sum(V)).

## 5. Editorial Comparison & Alignment
State-inversion / dual-space dynamic programming.

## 6. What This Problem Teaches
Swapping objective function and state dimension when constraints are large but values are compact.

## 7. Reusable Competitive Programming Pattern
`Dual DP parameter inversion.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)