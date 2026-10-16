# Problem Analysis: AtCoder-dp_r — Walk

**Problem ID**: `AtCoder-dp_r`  
**Contest**: `dp`  
**Rating**: 1700  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_r  
**VJudge Tag**: `[problem:AtCoder-dp_r]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Matrix Exponentiation DP`  

---

## 1. Problem Statement & Key Idea
Count paths of exact length K (K <= 10^18) in a directed graph of N vertices (N <= 50).

## 2. Core Observation & Invariant
The number of paths of length K between all pairs of vertices is given by A^K, where A is the adjacency matrix of the graph. Matrix multiplication computes transitions; binary exponentiation solves K <= 10^18 in O(log K) steps.

## 3. Step-by-Step Algorithm
1. Construct adjacency matrix A where A[u][v] = 1 if edge exists, else 0.
2. Compute M = A^K mod (10^9+7) using binary matrix exponentiation.
3. Total paths = sum_{i, j} M[i][j] mod MOD.

## 4. Complexity Analysis
Time: O(N^3 log K), Space: O(N^2).

## 5. Editorial Comparison & Alignment
Matrix exponentiation for path counting on graphs.

## 6. What This Problem Teaches
Formulating linear state recurrences as matrix products and exponentiating large step counts.

## 7. Reusable Competitive Programming Pattern
`Matrix exponentiation DP for enormous transition steps.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)