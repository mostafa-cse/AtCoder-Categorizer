# Splitting Objects into Light and Heavy / Case Processing

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Splitting Objects into Light and Heavy / Case Processing`

## Description
This topic focuses on splitting objects into light and heavy / case processing techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any interval of length $\ge d$ is guaranteed to contain at least one multiple of $d$. Intervals of length $< d$ contain at most one multiple of $d$ and can be queried via point evaluations.
- Common Reductions: Given $N$ souvenir intervals $[l_i, r_i] \subseteq [1, M]$, for each train interval $d = 1, \dots, M$, find the number of souvenir intervals containing at least one multiple of $d$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc068_c`](../../analysis/AtCoder-arc068_c.md) | E. Snuke Line | 2307 | Given $N$ souvenir intervals $[l_i, r_i] \subseteq [1, M]$, for each train interval $d = 1, \dots, M$, find the number o... |
