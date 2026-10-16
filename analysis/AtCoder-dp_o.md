# Problem Analysis: AtCoder-dp_o — Matching

**Problem ID**: `AtCoder-dp_o`  
**Contest**: `dp`  
**Rating**: 1650  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_o  
**VJudge Tag**: `[problem:AtCoder-dp_o]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Bit Related DP`  
- **Topic (Skill)**: `Bitmask DP`  

---

## 1. Problem Statement & Key Idea
Count perfect matchings in a bipartite graph with N men and N women (N <= 21).

## 2. Core Observation & Invariant
When matching men 0, 1, ..., i-1, exactly i women must be matched. Thus, i = popcount(mask). The index of the active man is completely implicit in the bitmask!

## 3. Step-by-Step Algorithm
1. dp[0] = 1, others 0.
2. For mask from 0 to 2^N - 1: let i = popcount(mask). If i == N continue.
3. For each woman j in 0..N-1: if compatible(i, j) and not (mask & (1 << j)): dp[mask | (1 << j)] = (dp[mask | (1 << j)] + dp[mask]) mod MOD.
4. Return dp[(1<<N) - 1].

## 4. Complexity Analysis
Time: O(N * 2^N), Space: O(2^N).

## 5. Editorial Comparison & Alignment
Popcount dimension-reduced bitmask DP.

## 6. What This Problem Teaches
Eliminating a state dimension using subset cardinality invariants in bitmask DP.

## 7. Reusable Competitive Programming Pattern
`Popcount implicit state matching: i = popcount(mask).`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)