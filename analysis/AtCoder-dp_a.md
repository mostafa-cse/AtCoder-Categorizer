# Problem Analysis: AtCoder-dp_a — Frog 1

**Problem ID**: `AtCoder-dp_a`  
**Contest**: `dp`  
**Rating**: 600  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_a  
**VJudge Tag**: `[problem:AtCoder-dp_a]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `1D State Recurrence / Bounded Lookahead`  

---

## 1. Problem Statement & Key Idea
Determine the minimum jump cost to reach stone N where each jump can span 1 or 2 stones.

## 2. Core Observation & Invariant
At stone i, arrival is possible exclusively from i-1 or i-2. The state depends only on local height differences |h_i - h_{i-k}| and optimal prefix solutions.

## 3. Step-by-Step Algorithm
1. Base cases: dp[1] = 0, dp[2] = |h_2 - h_1|.
2. For i from 3 to N: dp[i] = min(dp[i-1] + |h_i - h_{i-1}|, dp[i-2] + |h_i - h_{i-2}|).
3. Result: dp[N].

## 4. Complexity Analysis
Time: O(N), Space: O(1) rolling state.

## 5. Editorial Comparison & Alignment
Standard 1D forward relaxation recurrence.

## 6. What This Problem Teaches
Optimal substructure, state initialization, and memory-compressed transitions.

## 7. Reusable Competitive Programming Pattern
`Linear 1D DP with constant lookback window.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)