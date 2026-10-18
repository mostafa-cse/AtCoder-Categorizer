# Floor Sum and Mod Sum of Arithmetic Progression

**Taxonomy Path**: `Number Theory` > `Floor Sum` > `Floor Sum and Mod Sum of Arithmetic Progression`

## Description
This topic focuses on floor sum and mod sum of arithmetic progression techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sorting the initial array $A$ non-decreasingly, every reachable state corresponds to choosing the number of operations of each type. Equivalently, the number of distinct terminal configurations reduces to summing the number of lattice points bounded by piecewise linear constraints, which evaluates to floor sums of arithmetic progressions $\sum \lfloor (a x + b) / c \rfloor$ across adjacent intervals.
- Common Reductions: Find the number of reachable multisets of pile sizes after repeatedly choosing $i$ non-empty piles and decrementing them while adding $i$ to a chosen pile.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc313_g`](../../analysis/AtCoder-abc313_g.md) | G - Redistribution of Piles | 2454 | Find the number of reachable multisets of pile sizes after repeatedly choosing $i$ non-empty piles and decrementing them... |
