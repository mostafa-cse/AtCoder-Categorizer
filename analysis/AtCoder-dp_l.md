# Problem Analysis: AtCoder-dp_l — Deque

**Problem ID**: `AtCoder-dp_l`  
**Contest**: `dp`  
**Rating**: 1400  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_l  
**VJudge Tag**: `[problem:AtCoder-dp_l]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
Two players take turns removing numbers from either end of an array. Player 1 maximizes X - Y, Player 2 minimizes it.

## 2. Core Observation & Invariant
For any remaining subsegment [l, r], the active player chooses either a_l or a_r to maximize their gain minus the opponent's outcome from the remaining interval: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).

## 3. Step-by-Step Algorithm
1. Base: dp[i][i] = a_i.
2. Loop length from 2 to N: loop l from 1 to N-len+1: r = l+len-1: dp[l][r] = max(a_l - dp[l+1][r], a_r - dp[l][r-1]).
3. Return dp[1][N].

## 4. Complexity Analysis
Time: O(N^2), Space: O(N^2).

## 5. Editorial Comparison & Alignment
Zero-sum game minimax interval dynamic programming.

## 6. What This Problem Teaches
Interval dynamic programming (order of evaluation by length) and zero-sum minimax negation.

## 7. Reusable Competitive Programming Pattern
`Minimax interval DP: dp[l][r] = max(opt_left - dp[l+1][r], opt_right - dp[l][r-1]).`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)