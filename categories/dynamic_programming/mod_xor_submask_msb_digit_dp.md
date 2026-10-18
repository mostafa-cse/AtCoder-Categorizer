# Digit DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Digit DP` > `Digit DP`

## Description
This topic focuses on digit dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If MSB(x) < MSB(y), y XOR x >= 2^m > y/2 > y mod x. When MSB(x) == MSB(y), floor(y / x) = 1, so y mod x = y - x. Then y - x = y XOR x holds if and only if x is a bitwise submask of y.
- Common Reductions: Solve y mod x = y XOR x over [L, R] by proving the condition is equivalent to MSB(x) == MSB(y) and (x & y) == x, then counting valid pairs via Digit DP from bit 60 down to 0 in O(log R).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc138_f`](../../analysis/AtCoder-abc138_f.md) | Coincidence | 2431 | Solve y mod x = y XOR x over [L, R] by proving the condition is equivalent to MSB(x) == MSB(y) and (x & y) == x, then co... |
