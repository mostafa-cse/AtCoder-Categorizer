# Problem Analysis: AtCoder-abc250_c — Adjacent Swaps

**Problem ID**: `AtCoder-abc250_c`  
**Contest**: `abc250`  
**Rating**: 800  
**URL**: https://atcoder.jp/contests/abc250/tasks/abc250_c  
**VJudge Tag**: `[problem:AtCoder-abc250_c]`  
**Category File**: [`../categories/Basics.md`](../categories/Basics.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Implementation / Simulation`  
- **Topic (Skill)**: `Dual Index Mapping (Value-to-Position & Position-to-Value)`  

---

## 1. Problem Statement & Key Idea
Perform Q swaps where each query swaps the ball with integer x and its right neighbor (or left neighbor if at boundary).

## 2. Core Observation & Invariant
Finding ball x in an array of size N naively takes O(N) per query. Maintaining two arrays: `val_at[pos]` and `pos_of[val]` allows locating and swapping in O(1).

## 3. Step-by-Step Algorithm
1. Maintain pos[x] = position of ball x, and val[p] = ball at position p.
2. For each query x: find p = pos[x]. Determine target position p2 = (p < N ? p + 1 : p - 1). Let y = val[p2].
3. Swap in val: val[p] = y, val[p2] = x. Update positions: pos[x] = p2, pos[y] = p.

## 4. Complexity Analysis
Time: O(Q), Space: O(N).

## 5. Editorial Comparison & Alignment
Dual array bijection maintenance.

## 6. What This Problem Teaches
O(1) bidirectional lookup mapping and maintaining invertible permutations under swap operations.

## 7. Reusable Competitive Programming Pattern
`Dual index mapping (Position <-> Value).`

---
Back to [Category: Basics](../categories/Basics.md) | [Categories Index](../categories/README.md)