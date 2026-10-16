# Problem Analysis: AtCoder-dp_q — Flowers

**Problem ID**: `AtCoder-dp_q`  
**Contest**: `dp`  
**Rating**: 1600  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_q  
**VJudge Tag**: `[problem:AtCoder-dp_q]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `DP Optimization using Data Structures [Some Practice Problems]`  

---

## 1. Problem Statement & Key Idea
Find an increasing subsequence of flower heights that maximizes total beauty.

## 2. Core Observation & Invariant
dp[h_i] = a_i + max_{0 <= h < h_i} dp[h]. Querying max in [0, h_i - 1] and updating point h_i is dynamically solved in O(log N) by a Fenwick or Segment Tree.

## 3. Step-by-Step Algorithm
1. Maintain Fenwick tree supporting point-update and prefix-max queries.
2. For each flower i: best = fenwick.query(h_i - 1); fenwick.update(h_i, best + a_i).
3. Return fenwick.query(N).

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Editorial Comparison & Alignment
Fenwick tree / Segment tree accelerated LIS.

## 6. What This Problem Teaches
Transforming quadratic inner-loop search into dynamic range queries via data structures.

## 7. Reusable Competitive Programming Pattern
`BIT/Segment Tree accelerated DP.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)