# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any tournament bracket on a circular arrangement corresponds to contiguous subsegments. A person i can win interval [i, j] iff there exists an internal split point k such that i wins [i, k], someone p wins [k+1, j], and i beats p. Using interval DP with bitsets, dpl[i][j] is true iff person i can win [i, j] and dpr[j][i] iff person j can win [i, j]. Bitset AND operations accelerate transitions to O(N^3 / 64).
- Common Reductions: In a knockout tournament of N players arranged in a circle where adjacent survivors battle, determine how many players have a positive probability of winning the entire tournament.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-m_solutions2019_f`](../../analysis/AtCoder-m_solutions2019_f.md) | F - Random Tournament | 2986 | In a knockout tournament of N players arranged in a circle where adjacent survivors battle, determine how many players h... |
