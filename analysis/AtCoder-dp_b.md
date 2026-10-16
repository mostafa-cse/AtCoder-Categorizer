# Problem Analysis: AtCoder-dp_b — Frog 2

**Problem ID**: `AtCoder-dp_b`  
**Contest**: `dp`  
**Rating**: 700  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_b  
**VJudge Tag**: `[problem:AtCoder-dp_b]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `1D DP with K-Step Transitions`  

---

## 1. Problem Statement & Key Idea
Generalize jumps from 2 stones to up to K stones with minimum total energy cost.

## 2. Core Observation & Invariant
Each state dp[i] is relaxed over a sliding window of the previous K states: dp[i] = min_{1 <= j <= K} (dp[i-j] + |h_i - h_{i-j}|).

## 3. Step-by-Step Algorithm
1. Initialize dp[1] = 0, others INF.
2. For i in 1..N-1: for step in 1..K (with i+step <= N): dp[i+step] = min(dp[i+step], dp[i] + |h_{i+step} - h_i|).
3. Return dp[N].

## 4. Complexity Analysis
Time: O(N * K), Space: O(N).

## 5. Editorial Comparison & Alignment
Standard push-based relaxation over parameterized lookahead.

## 6. What This Problem Teaches
Parameterized transition loops and boundary-bounded relaxation.

## 7. Reusable Competitive Programming Pattern
`Push DP over variable-sized transition intervals.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)