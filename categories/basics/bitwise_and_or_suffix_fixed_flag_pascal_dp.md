# Bitwise Operations and Bitmasks

**Taxonomy Path**: `Basics` > `Bitwise Thinking` > `Bitwise Operations and Bitmasks`

## Description
This topic focuses on bitwise operations and bitmasks techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The maximum value M is achieved by placing all K OR operations at the end: M = OR_{i=N-K}^{N-1} A_i. Working backwards from the last operation, bits that must match M become permanently fixed, bounding the number of active branch states to at most 2.
- Common Reductions: Choose AND or OR for each element of A with at most K OR operations to achieve the maximum possible final value M. Count the number of valid operation sequences by working backwards with a fixed-bit state and Pascal triangle prefix sums.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc224_f`](../../analysis/AtCoder-arc224_f.md) | F. AND/OR | 2407 | Choose AND or OR for each element of A with at most K OR operations to achieve the maximum possible final value M. Count... |
