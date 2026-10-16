# Problem Analysis: AtCoder-abc186_e — Throne

**Problem ID**: `AtCoder-abc186_e`  
**Contest**: `abc186`  
**Rating**: 1250  
**URL**: https://atcoder.jp/contests/abc186/tasks/abc186_e  
**VJudge Tag**: `[problem:AtCoder-abc186_e]`  
**Category File**: [`../categories/Number_Theory.md`](../categories/Number_Theory.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Modular Arithmetic`  
- **Topic (Skill)**: `Modular Linear Congruence / Extended Euclidean Algorithm`  

---

## 1. Problem Statement & Key Idea
A piece moves K steps clockwise on a circle of size N, starting at position S. Find minimum steps to reach position 0.

## 2. Core Observation & Invariant
The condition is S + x * K = 0 (mod N), which rearranges to K * x = -S (mod N). This is a linear congruence ax = b (mod m). Solutions exist if and only if gcd(K, N) divides S.

## 3. Step-by-Step Algorithm
1. Let g = gcd(K, N). If S % g != 0: return -1.
2. Divide through by g: K' = K/g, S' = S/g, N' = N/g.
3. Now gcd(K', N') = 1. Find modular inverse inv = mod_inv(K', N') via Extended GCD.
4. x = (-S' * inv) mod N'. Output x.

## 4. Complexity Analysis
Time: O(log(min(K, N))) per testcase, Space: O(1).

## 5. Editorial Comparison & Alignment
Extended Euclidean Algorithm for modular inverse.

## 6. What This Problem Teaches
Modular linear congruences, solvability condition via GCD divisibility, and Extended Euclidean Algorithm.

## 7. Reusable Competitive Programming Pattern
`Extended Euclidean linear congruence solver.`

---
Back to [Category: Number Theory](../categories/Number_Theory.md) | [Categories Index](../categories/README.md)