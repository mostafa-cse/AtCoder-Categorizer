# Difference Array

**Taxonomy Path**: `Basics` > `More Techniques` > `Difference Array`

## Description
This topic focuses on difference array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Cross-center range operations decompose into symmetric left/right operations without penalty. On difference sequence C (where sum(C) is a multiple of M), each operation increments one element and decrements another modulo M. Choosing a subset of elements X to only decrease and the rest to only increase yields minimum operations sum of the k smallest elements of C, where k = |C| - sum(C)/M.
- Common Reductions: Minimum range increment/decrement operations modulo M to make sequence A palindromic. Folding differences B_i = (A_i - A_{N+1-i}) mod M reduces the problem to zeroing B. Transforming to difference array C_i = (B_i - B_{i-1}) mod M turns range operations into pairs of increment/decrement on single elements, solvable greedily by sorting.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc454_f`](../../analysis/AtCoder-abc454_f.md) | I. Make it Palindrome 2 | 2169 | Minimum range increment/decrement operations modulo M to make sequence A palindromic. Folding differences B_i = (A_i - A... |
