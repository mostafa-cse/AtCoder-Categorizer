# Suffix Automaton

**Taxonomy Path**: `Strings` > `Suffix Structures` > `Suffix Automaton`

## Description
This topic focuses on suffix automaton techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each operation either increments or decrements the length of X by 1. If X and Y share a common contiguous substring S, we can shrink X to S and expand S to Y in |P| + |Q| - 2|S| operations. To minimize this, we seek the Longest Common Substring (LCS) of X and Y, which can be found in O(P + Q) using a Suffix Automaton built on X. If X and Y have no common substring (LCS = 0), X must shrink to a single element u, transition along adjacent elements in A to an element v in Y via a shortest path of distance d in the value adjacency graph of A (costing 2d operations), and expand to Y. The total operations in this case is |P| + |Q| - 2 + 2d, computed via multi-source BFS.
- Common Reductions: Given an integer sequence A of length N, and two contiguous subsequences X of length P and Y of length Q, we can add/delete elements from the front or back of X such that X remains a non-empty contiguous subsequence of A at all times. We want to find the minimum number of operations to transform X into Y.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc151_e`](../../analysis/AtCoder-arc151_e.md) | E - Keep Being Substring | 2713 | Given an integer sequence A of length N, and two contiguous subsequences X of length P and Y of length Q, we can add/del... |
