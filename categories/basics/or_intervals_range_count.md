# Bitwise Operations and Bitmasks

**Taxonomy Path**: `Basics` > `Bitwise Thinking` > `Bitwise Operations and Bitmasks`

## Description
This topic focuses on bitwise operations and bitmasks techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let k be the highest bit where A and B differ. Strip common prefix bits. Then A's remainder is in [0, 2^k - 1] and B's remainder is in [2^k, 2^k + B_rem]. All subsets without bit k produce values in [A_rem, 2^k - 1]. Subsets containing at least one element with bit k produce values in [2^k, 2^k + 2^(m+1) - 1] union [2^k + A_rem, 2^(k+1) - 1], where m is the second highest bit of B. Merging these disjoint or overlapping intervals yields the exact count in O(1).
- Common Reductions: Counting the number of distinct values achievable by bitwise OR of non-empty subsets of [A, B] reduces to analyzing bit intervals relative to the most significant differing bit.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc015_d`](../../analysis/AtCoder-agc015_d.md) | A or...or B Problem | 2655 | Counting the number of distinct values achievable by bitwise OR of non-empty subsets of [A, B] reduces to analyzing bit ... |
