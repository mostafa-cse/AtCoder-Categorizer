# Matrix Exponentiation

**Taxonomy Path**: `Math` > `Matrices` > `Matrix Exponentiation`

## Description
This topic focuses on matrix exponentiation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The sequence of accesses forms a time-homogeneous Markov chain on the 24 hours of the day, where transition probability $M_{u, v}$ accounts for the geometric probability of failing all 24 hours $0, 1, 2, \dots$ times before hitting hour $v$.
- Common Reductions: A process transitions along a circular 24-hour clock. At hour $h$, with probability $p_h$ an access occurs. If so, with probability $A_i$ user $i$ accesses it. Find the probability that the $N$-th access is made by each user, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc271_g`](../../analysis/AtCoder-abc271_g.md) | G. Access Counter | 2323 | A process transitions along a circular 24-hour clock. At hour $h$, with probability $p_h$ an access occurs. If so, with ... |
