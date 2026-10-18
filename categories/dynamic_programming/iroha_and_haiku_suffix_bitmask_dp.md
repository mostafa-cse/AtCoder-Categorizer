# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because $X + Y + Z \le 17$, the entire state of recent suffix sums fits into a 17-bit integer ($2^{17} = 131,072$). Suffix bitmask transitions are pure bitwise shifts, allowing $O(10 \cdot 2^{X+Y+Z})$ operations per sequence position.
- Common Reductions: Count length-$N$ sequences with elements in $[1, 10]$ containing an $X, Y, Z$-Haiku subsegment. Complement counting: total sequences $10^N$ minus sequences that never form an $X, Y, Z$-Haiku. Maintain a bitmask of reachable suffix sums up to $S = X + Y + Z \le 17$. Appending digit $d$ shifts the bitmask by $d$ and sets bit $d - 1$. Forbid transitions to any mask containing bits $Z - 1, Y + Z - 1, S - 1$ simultaneously.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc058_c`](../../analysis/AtCoder-arc058_c.md) | E. Iroha and Haiku | 2473 | Count length-$N$ sequences with elements in $[1, 10]$ containing an $X, Y, Z$-Haiku subsegment. Complement counting: tot... |
