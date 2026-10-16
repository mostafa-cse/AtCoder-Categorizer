# Problem Analysis: AtCoder-dp_u — Grouping

**Problem ID**: `AtCoder-dp_u`  
**Contest**: `dp`  
**Rating**: 1850  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_u  
**VJudge Tag**: `[problem:AtCoder-dp_u]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP / O(3^N) Submask Enumeration`  

---

## 1. Problem Statement & Key Idea
Partition N rabbits into arbitrary disjoint groups maximizing total compatibility score (N <= 16).

## 2. Core Observation & Invariant
Precompute standalone group scores in O(N^2 * 2^N). Then dp[mask] = max_{sub is submask of mask} (cost[sub] + dp[mask ^ sub]). The submask loop `sub = (sub - 1) & mask` iterates all submasks in sum_{k=0}^N binom(N, k) 2^k = 3^N total operations.

## 3. Step-by-Step Algorithm
1. Precompute score[mask] for all 2^N subsets.
2. Loop mask from 1 to 2^N - 1:
   sub = mask; while sub > 0: dp[mask] = max(dp[mask], score[sub] + dp[mask ^ sub]); sub = (sub - 1) & mask.
3. Return dp[(1<<N) - 1].

## 4. Complexity Analysis
Time: O(3^N + N^2 * 2^N), Space: O(2^N).

## 5. Editorial Comparison & Alignment
Textbook submask enumeration.

## 6. What This Problem Teaches
The (sub - 1) & mask bitwise trick and set partition dynamic programming.

## 7. Reusable Competitive Programming Pattern
`O(3^N) submask iteration: sub = (sub - 1) & mask.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)