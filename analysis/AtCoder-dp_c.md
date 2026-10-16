# Problem Analysis: AtCoder-dp_c — Vacation

**Problem ID**: `AtCoder-dp_c`  
**Contest**: `dp`  
**Rating**: 900  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_c  
**VJudge Tag**: `[problem:AtCoder-dp_c]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Multi-State DP / Consecutive Constraints`  

---

## 1. Problem Statement & Key Idea
Maximize vacation happiness over N days choosing between three activities (A, B, C) without doing the same activity two days in a row.

## 2. Core Observation & Invariant
Enforcing the constraint 'no two consecutive identical choices' requires augmenting the state with the identity of the last chosen activity.

## 3. Step-by-Step Algorithm
1. State: dp[day][act] = max happiness up to day ending in act in {0, 1, 2}.
2. dp[i][0] = a_i + max(dp[i-1][1], dp[i-1][2]), and symmetrically for 1 and 2.
3. Return max_{act} dp[N][act].

## 4. Complexity Analysis
Time: O(N), Space: O(1) rolling state.

## 5. Editorial Comparison & Alignment
Classic 3-state Markov transition graph.

## 6. What This Problem Teaches
State augmentation for path-dependent constraints and state-machine DP.

## 7. Reusable Competitive Programming Pattern
`Categorical state-machine DP with mutually exclusive transitions.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)