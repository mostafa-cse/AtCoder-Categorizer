# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A palindrome is possible iff at most one character has an odd frequency. In an optimal swap sequence, identical characters never cross each other. Processing characters greedily from left to right, we match each character with its rightmost available twin, assigning them symmetric target positions at the current outer boundaries. The minimum swaps to achieve this target configuration equals the inversion count of the target permutation, solvable in O(N log N) via Fenwick tree.
- Common Reductions: Find the minimum number of adjacent swaps to transform a string of length N <= 2 * 10^5 into a palindrome, or report -1 if impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc088_c`](../../analysis/AtCoder-arc088_c.md) | Papple Sort | 2231 | Find the minimum number of adjacent swaps to transform a string of length N <= 2 * 10^5 into a palindrome, or report -1 ... |
