# Problem Analysis: AtCoder-dp_g — Longest Path

**Problem ID**: `AtCoder-dp_g`  
**Contest**: `dp`  
**Rating**: 1350  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_g  
**VJudge Tag**: `[problem:AtCoder-dp_g]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `DP on Trees and DAGs`  

---

## 1. Problem Statement & Key Idea
Find the length of the longest directed path in a Directed Acyclic Graph (DAG).

## 2. Core Observation & Invariant
In a DAG, cycles are absent; topological ordering guarantees a well-founded recursion. The longest path starting at u is dp[u] = 1 + max_{(u, v) in E} dp[v].

## 3. Step-by-Step Algorithm
1. Memoized DFS: memo[u] = -1.
2. DFS(u): if memo[u] != -1 return memo[u]. ans = 0. For each out-neighbor v: ans = max(ans, 1 + DFS(v)). memo[u] = ans.
3. Global answer = max_{u in V} DFS(u).

## 4. Complexity Analysis
Time: O(V + E), Space: O(V + E).

## 5. Editorial Comparison & Alignment
Topological sort DP / memoized DFS on DAG.

## 6. What This Problem Teaches
Topological order as the universal prerequisite for acyclic graph dynamic programming.

## 7. Reusable Competitive Programming Pattern
`DAG memoized DFS transition.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)