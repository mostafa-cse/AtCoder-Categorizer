# Problem Analysis: AtCoder-dp_i — Coins

**Problem ID**: `AtCoder-dp_i`  
**Contest**: `dp`  
**Rating**: 1150  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_i  
**VJudge Tag**: `[problem:AtCoder-dp_i]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Probability and Expected Value DP`  

---

## 1. Problem Statement & Key Idea
Calculate the exact probability that more heads than tails appear when tossing N independent biased coins.

## 2. Core Observation & Invariant
Let dp[i][j] be the probability of obtaining exactly j heads after i coin tosses. The outcome of coin i partitions probability mass into two independent events: heads (prob p_i) or tails (prob 1 - p_i).

## 3. Step-by-Step Algorithm
1. dp[0][0] = 1.0; others 0.0.
2. For i in 1..N: for j in 0..i: dp[i][j] = (j > 0 ? dp[i-1][j-1] * p_i : 0) + dp[i-1][j] * (1 - p_i).
3. Sum dp[N][j] for j > N/2.

## 4. Complexity Analysis
Time: O(N^2), Space: O(N).

## 5. Editorial Comparison & Alignment
Poisson binomial distribution dynamic programming.

## 6. What This Problem Teaches
Probability mass conservation and floating-point accumulation in discrete trial DP.

## 7. Reusable Competitive Programming Pattern
`Probability convolution DP over independent Bernoulli trials.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)