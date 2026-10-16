# Problem Analysis: AtCoder-typical90_f — Smallest Subsequence

**Problem ID**: `AtCoder-typical90_f`  
**Contest**: `typical90`  
**Rating**: 1500  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_f  
**VJudge Tag**: `[problem:AtCoder-typical90_f]`  
**Category File**: [`../categories/Strings.md`](../categories/Strings.md)  

- **Tag (Domain)**: `Strings`  
- **Subtopic**: `Greedy on Strings`  
- **Topic (Skill)**: `Next-Occurrence Array / Lexicographically Smallest Subsequence`  

---

## 1. Problem Statement & Key Idea
Find the lexicographically smallest subsequence of length K from string S of length N.

## 2. Core Observation & Invariant
To minimize lexicographically, greedily choose the smallest possible character for each of the K positions from left to right. A character choice at position p is valid if and only if the remaining suffix has length >= remaining positions needed.

## 3. Step-by-Step Algorithm
1. Precompute next_pos[i][c]: the earliest index >= i where character c occurs.
2. Current index cur = 0.
3. For step from 1 to K: remaining_needed = K - step.
   For char c from 'a' to 'z': let pos = next_pos[cur][c]. If N - pos >= remaining_needed: append c, cur = pos + 1, break.
4. Output string.

## 4. Complexity Analysis
Time: O(26 * N + 26 * K), Space: O(26 * N).

## 5. Editorial Comparison & Alignment
Next-character transition table with greedy lookahead.

## 6. What This Problem Teaches
Precomputing next-occurrence transition tables on strings and greedy lexicographical construction.

## 7. Reusable Competitive Programming Pattern
`Next-occurrence array for subsequence queries.`

---
Back to [Category: Strings](../categories/Strings.md) | [Categories Index](../categories/README.md)