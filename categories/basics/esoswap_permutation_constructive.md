# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When P has a contiguous block 1, 2, ..., k, applying the swap operation sequentially to the positions of 1, 2, ..., k shifts the entire block one position to the right and brings the element immediately following k to the left of the block: [1..k, X] becomes [X, 1..k]. By repeating this shifting procedure, we can rotate the block through the permutation until the element immediately following k becomes k+1, absorbing it into the block to form 1, 2, ..., k+1. Growing the block from size 1 to N-1 takes sum_{k=1}^{N-2} k(N - 1 - k) = N(N-1)(N-2)/6 <= 161,700 operations. Finally, shifting the sorted block 1..N-1 until 0 is at index 0 takes at most (N-1)*N <= 10,000 operations, well within 2 * 10^5.
- Common Reductions: Given a permutation P of 0..N-1 (N <= 100), an operation chooses index i and swaps P[i] with P[(i + P[i]) mod N]. We want to sort P in ascending order in at most 2 * 10^5 operations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc110_f`](../../analysis/AtCoder-arc110_f.md) | F - Esoswap | 2719 | Given a permutation P of 0..N-1 (N <= 100), an operation chooses index i and swaps P[i] with P[(i + P[i]) mod N]. We wan... |
