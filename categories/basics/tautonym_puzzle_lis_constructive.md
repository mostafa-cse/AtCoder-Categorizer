# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Construct s as P + Q, where P = (1, 2, ..., k) and Q is a permutation of (1, 2, ..., k). Because each character in 1..k appears exactly once in P and once in Q, any good subsequence y + y must have its first copy in P and second copy in Q. Since P is sorted 1..k, y must be an INCREASING subsequence of Q! Thus, the number of good subsequences of s is precisely the number of non-empty increasing subsequences of Q. Appending an element to the right of Q doubles the count of increasing subsequences (including empty), while prepending an element to the left increments the count by 1. Using Horner's rule on the binary representation of N + 1, we construct Q with k <= 55 elements.
- Common Reductions: Find a string s of integers from 1..100 with |s| <= 200 such that exactly N subsequences of s are 'good' (of the form y + y for |y| >= 1), where 1 <= N <= 10^{12}.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc012_c`](../../analysis/AtCoder-agc012_c.md) | C - Tautonym Puzzle | 2731 | Find a string s of integers from 1..100 with |s| <= 200 such that exactly N subsequences of s are 'good' (of the form y ... |
