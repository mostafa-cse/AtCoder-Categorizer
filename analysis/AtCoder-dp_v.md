# Problem Analysis: AtCoder-dp_v — Subtree

**Problem ID**: `AtCoder-dp_v`  
**Contest**: `dp`  
**Rating**: 2100  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_v  
**VJudge Tag**: `[problem:AtCoder-dp_v]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Dp on Different Structures`  
- **Topic (Skill)**: `Tree DP with Subtree Rerooting without Division`  

---

## 1. Problem Statement & Key Idea
For every node v in a tree, compute the number of black-connected components containing v modulo M (M may not be prime).

## 2. Core Observation & Invariant
Because M is not necessarily prime, division by (down[child] + 1) is invalid! Computing prefix and suffix products of children values allows excluding a child in O(1) without modular division.

## 3. Step-by-Step Algorithm
1. DFS1: compute subtree product down[u] = prod_{v in children} (down[v] + 1) mod M.
2. DFS2: compute parent contribution up[u] using prefix and suffix products of (down[sib] + 1).
3. Ans[u] = down[u] * (up[u] + 1) mod M.

## 4. Complexity Analysis
Time: O(N), Space: O(N).

## 5. Editorial Comparison & Alignment
All-roots tree DP rerooting under arbitrary modulus.

## 6. What This Problem Teaches
Tree rerooting without modular division via prefix/suffix product arrays.

## 7. Reusable Competitive Programming Pattern
`Division-free prefix/suffix rerooting on trees.`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)