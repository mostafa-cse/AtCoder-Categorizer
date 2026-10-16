# Problem Analysis: AtCoder-typical90_a — Yokan Party

**Problem ID**: `AtCoder-typical90_a`  
**Contest**: `typical90`  
**Rating**: 1200  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_a  
**VJudge Tag**: `[problem:AtCoder-typical90_a]`  
**Category File**: [`../categories/Basics.md`](../categories/Basics.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Binary Search`  
- **Topic (Skill)**: `Binary Search on Answer / Greedy Feasibility`  

---

## 1. Problem Statement & Key Idea
Cut a stick of length L at K positions to maximize the length of the shortest piece.

## 2. Core Observation & Invariant
'Maximize the minimum' is the definitive indicator for Binary Search on Answer. The predicate 'Can we obtain at least K+1 pieces each of length >= M?' is strictly monotonic with respect to M.

## 3. Step-by-Step Algorithm
1. Binary search M in [1, L].
2. Predicate check(M): Greedily cut whenever the current piece reaches length >= M. If total pieces cut is >= K and remaining piece is >= M, return True; else False.
3. Upper boundary of search range is the optimal answer.

## 4. Complexity Analysis
Time: O(N log L), Space: O(1).

## 5. Editorial Comparison & Alignment
Textbook binary search on answer.

## 6. What This Problem Teaches
Formulating feasibility predicates, establishing monotonicity, and greedy cut verification.

## 7. Reusable Competitive Programming Pattern
`Binary search on answer + greedy feasibility check.`

---
Back to [Category: Basics](../categories/Basics.md) | [Categories Index](../categories/README.md)