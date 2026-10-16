# Problem Analysis: AtCoder-abc284_d — Happy New Year 2023

**Problem ID**: `AtCoder-abc284_d`  
**Contest**: `abc284`  
**Rating**: 1050  
**URL**: https://atcoder.jp/contests/abc284/tasks/abc284_d  
**VJudge Tag**: `[problem:AtCoder-abc284_d]`  
**Category File**: [`../categories/Number_Theory.md`](../categories/Number_Theory.md)  

- **Tag (Domain)**: `Number Theory`  
- **Subtopic**: `Prime Numbers`  
- **Topic (Skill)**: `Cubic-Root Prime Factorization (N = p^2 * q)`  

---

## 1. Problem Statement & Key Idea
Given N = p^2 * q where p and q are prime and N <= 9 * 10^18, find primes p and q.

## 2. Core Observation & Invariant
Because N = p^2 * q, at least one of p or q must be <= N^(1/3) <= 2.15 * 10^6! Testing trial divisors up to N^(1/3) will instantly find one prime factor.

## 3. Step-by-Step Algorithm
1. Loop d from 2 up to 3 * 10^6:
   If N % d == 0: if N % (d * d) == 0 -> p = d, q = N / (d * d); else p = isqrt(N / d), q = d; break.
2. Output p and q.

## 4. Complexity Analysis
Time: O(N^(1/3)) per testcase, Space: O(1).

## 5. Editorial Comparison & Alignment
Cubic root trial division for asymmetric prime powers.

## 6. What This Problem Teaches
Exploiting asymmetric algebraic power structures to bound search space to N^(1/3) rather than sqrt(N).

## 7. Reusable Competitive Programming Pattern
`N^(1/3) trial division for p^2 * q factorization.`

---
Back to [Category: Number Theory](../categories/Number_Theory.md) | [Categories Index](../categories/README.md)