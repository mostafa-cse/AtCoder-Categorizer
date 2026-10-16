# Problem Analysis: AtCoder-dp_j — Sushi

**Problem ID**: `AtCoder-dp_j`  
**Contest**: `dp`  
**Rating**: 1650  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_j  
**VJudge Tag**: `[problem:AtCoder-dp_j]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Expected Value DP with Multi-Frequency States`  

---

## 1. Problem Statement & Key Idea
N plates have 1, 2, or 3 sushi. Repeatedly pick a random plate until all sushi are eaten. Find expected number of operations.

## 2. Core Observation & Invariant
The plate identity does not matter! Only the count of plates having 1 sushi (c1), 2 sushi (c2), and 3 sushi (c3) determines the system state. Picking an empty plate loops back to the same state (self-loop), which can be eliminated algebraically.

## 3. Step-by-Step Algorithm
1. State: dp[c1][c2][c3] = expected operations.
2. E = 1 + (c1/N)*dp[c1-1][c2][c3] + (c2/N)*dp[c1+1][c2-1][c3] + (c3/N)*dp[c1][c2+1][c3-1] + (c0/N)*E.
3. Solve for E: E * (1 - c0/N) = 1 + sum(...) => E = (N + c1*dp1 + c2*dp2 + c3*dp3) / (c1 + c2 + c3).
4. Memoized DFS / 3D loop.

## 4. Complexity Analysis
Time: O(N^3), Space: O(N^3).

## 5. Editorial Comparison & Alignment
Expected value recurrence with algebraic self-loop resolution.

## 6. What This Problem Teaches
State compression by value multiplicity and algebraic self-loop elimination in expected value DP.

## 7. Reusable Competitive Programming Pattern
`Self-loop elimination: E = (1 + \sum P_i E_i) / (1 - P_{self}).`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)