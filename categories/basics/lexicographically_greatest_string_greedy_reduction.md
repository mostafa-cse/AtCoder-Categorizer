# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The operations allow cancelling pairs of 'a's and shifting 'b's forward. The optimal string consists of a maximal prefix of 'b's followed by minimal 'a's, or leading 'b's with specific trailing patterns. The exact trailing sequence depends on the total count of 'a's, whether the last character of S is 'a', and whether pairs of 'a's can be cancelled without destroying 'b' runs. By decomposing S into runs of 'a' and 'b', we can evaluate a small number of candidate optimal reductions and take the lexicographically maximum.
- Common Reductions: Given a string S consisting of 'a' and 'b', you can repeatedly delete adjacent identical characters or invert/reverse substrings. Find the lexicographically largest string that can be formed.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc113_e`](../../analysis/AtCoder-arc113_e.md) | E - Rvom and Rsrev | 2789 | Given a string S consisting of 'a' and 'b', you can repeatedly delete adjacent identical characters or invert/reverse su... |
