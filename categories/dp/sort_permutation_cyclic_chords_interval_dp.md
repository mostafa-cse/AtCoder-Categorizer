# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sorting a permutation in minimum swaps requires every swap to split a cycle into two. Swaps between positions with i == j mod N give 1 point and correspond to chords connecting equal residue classes on the cycle. Two chords can both be executed iff they do not cross. The problem decouples independently over each cycle of P.
- Common Reductions: Permutation cycle decomposition reduced to maximum non-crossing chords connecting equal residues on a circle via interval DP.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc204_b`](../../analysis/AtCoder-arc204_b.md) | Sort Permutation | 2210 | Permutation cycle decomposition reduced to maximum non-crossing chords connecting equal residues on a circle via interva... |
