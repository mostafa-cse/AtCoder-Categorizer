# Problem Analysis: AtCoder-dp_h — Grid 1

**Problem ID**: `AtCoder-dp_h`  
**Contest**: `dp`  
**Rating**: 1050  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_h  
**VJudge Tag**: `[problem:AtCoder-dp_h]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Grid DP / Path Counting with Obstacles`  

---

## 1. Problem Statement & Key Idea
Count paths from top-left (1,1) to bottom-right (H,W) moving only right and down, avoiding obstacle walls.

## 2. Core Observation & Invariant
Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.

## 3. Step-by-Step Algorithm
1. dp[1][1] = 1.
2. For r in 1..H, c in 1..W: if grid[r][c] == '#': dp[r][c] = 0; else dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % MOD.
3. Return dp[H][W].

## 4. Complexity Analysis
Time: O(H * W), Space: O(W).

## 5. Editorial Comparison & Alignment
Grid combinatorial dynamic programming.

## 6. What This Problem Teaches
Grid boundary enforcement, obstacle nullification, and modulo arithmetic accumulation.

## 7. Reusable Competitive Programming Pattern
`2D additive grid DP.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)