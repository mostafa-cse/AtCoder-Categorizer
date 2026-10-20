# Stack

**Taxonomy Path**: `Basics` > `Standard Template Library (STL)` > `Stack`

## Description
This topic focuses on stack techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: We simulate the median replacement greedily using a stack reduction. When scanning from left to right, two adjacent '1's can absorb any '0'. The stack can be canonicalized into a finite automaton of only 9 states! Transitions on '0' and '1' form a 9-state DFA, where accepting states correspond to stacks with majority '1's.
- Common Reductions: Given a string S of odd length N <= 3 * 10^5 consisting of '0', '1', and '?', count the number of binary strings obtainable by replacing '?' such that repeatedly replacing 3 consecutive characters with their median reduces the string to '1', modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc022_e`](../../analysis/AtCoder-agc022_e.md) | E - Median Replace | 2963 | Given a string S of odd length N <= 3 * 10^5 consisting of '0', '1', and '?', count the number of binary strings obtaina... |
