# Problem Analysis: AtCoder-dp_p — Independent Set

**Problem ID**: `AtCoder-dp_p`  
**Contest**: `dp`  
**Rating**: 1500  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_p  
**VJudge Tag**: `[problem:AtCoder-dp_p]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Count ways to paint vertices of a tree black or white such that no two adjacent vertices are both black.

## 2. Core Observation & Invariant
Root tree arbitrarily. If node u is Black, all children must be White. If u is White, each child can be independently either Black or White.

## 3. Step-by-Step Algorithm
1. Post-order DFS(u, parent).
2. dp[u][Black] = prod_{v in children} dp[v][White].
3. dp[u][White] = prod_{v in children} (dp[v][Black] + dp[v][White]).
4. Return (dp[root][Black] + dp[root][White]) mod MOD.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Editorial Comparison & Alignment
Tree independent set combinatorial DP.

## 6. What This Problem Teaches
Subtree DP, child product combinations, and color state branching on trees.

## 7. Reusable Competitive Programming Pattern
`Two-state subtree product DP on trees.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)