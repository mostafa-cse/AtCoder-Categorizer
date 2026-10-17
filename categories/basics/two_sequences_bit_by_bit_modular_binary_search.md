# Binary Search

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Binary Search`

## Description
This topic focuses on binary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Bit k of a_i + b_j is completely determined by (a_i mod 2^(k+1)) + (b_j mod 2^(k+1)). Setting T = 2^k, bit k is 1 iff the sum lies in [T, 2T - 1] or [3T, 4T - 2].
- Common Reductions: Bit-by-bit contribution method with modular reduction mod 2^(k+1) and range counting via binary search.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc092_b`](../../analysis/AtCoder-arc092_b.md) | Two Sequences | 2207 | Bit-by-bit contribution method with modular reduction mod 2^(k+1) and range counting via binary search.... |
