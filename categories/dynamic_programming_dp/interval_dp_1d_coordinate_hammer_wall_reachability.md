# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: On a 1D line starting at 0, the set of visited coordinates always forms a contiguous interval $[l, r]$ containing 0, with the player situated at either $l$ or $r$. Expanding to $l - 1$ or $r + 1$ is valid if and only if any wall encountered has its associated hammer located within $[l, r]$.
- Common Reductions: Given a coordinate line with start at 0, target at $X$, $N$ walls, and $N$ hammers required to break corresponding walls, find the minimum total travel distance to reach $X$, or -1 if unreachable.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc273_f`](../../analysis/AtCoder-abc273_f.md) | F. Hammer 2 | 2277 | Given a coordinate line with start at 0, target at $X$, $N$ walls, and $N$ hammers required to break corresponding walls... |
