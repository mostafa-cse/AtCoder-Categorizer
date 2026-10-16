# Problem Analysis: AtCoder-dp_s — Digit Sum

**Problem ID**: `AtCoder-dp_s`  
**Contest**: `dp`  
**Rating**: 1750  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_s  
**VJudge Tag**: `[problem:AtCoder-dp_s]`  
**Category File**: [`../categories/Dynamic_Programming.md`](../categories/Dynamic_Programming.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Digit DP`  
- **Topic (Skill)**: `Digit DP with Remainder State`  

---

## 1. Problem Statement & Key Idea
Count positive integers up to K (K <= 10^10000) whose sum of digits is a multiple of D.

## 2. Core Observation & Invariant
K has up to 10,000 digits! Process digits from most significant to least significant, maintaining the remainder of the digit sum mod D, and a boolean flag `tight` indicating whether the prefix matches K.

## 3. Step-by-Step Algorithm
1. dp[index][rem][tight]: number of valid suffixes.
2. For each digit d from 0 to (tight ? K[idx] : 9): next_tight = tight and (d == K[idx]); next_rem = (rem + d) % D; dp[idx+1][next_rem][next_tight] += dp[idx][rem][tight].
3. Answer: (dp[len][0][0] + dp[len][0][1] - 1 + MOD) % MOD (subtract 1 for 0).

## 4. Complexity Analysis
Time: O(|K| * D * 10), Space: O(|K| * D).

## 5. Editorial Comparison & Alignment
Textbook Digit DP with tight bound tracking.

## 6. What This Problem Teaches
Digit-by-digit construction, tight prefix bound handling, and large integer parsing.

## 7. Reusable Competitive Programming Pattern
`Standard Digit DP state tuple (index, remainder, is_tight).`

---
Back to [Category: Dynamic Programming (DP)](../categories/Dynamic_Programming.md) | [Categories Index](../categories/README.md)