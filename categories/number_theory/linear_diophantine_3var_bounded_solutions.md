# Extended Euclid

**Taxonomy Path**: `Number Theory` > `Euclidean Algorithm` > `Extended Euclid`

## Description
This topic focuses on extended euclid techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each fixed $i \in [1, N]$, the equation $B j + C k = X - A i$ is a 2-variable linear Diophantine equation whose solutions form an arithmetic progression $j = j_0 + t \cdot (C / g)$.
- Common Reductions: Given $N, A, B, C, X$, count the number of triples $(i, j, k)$ with $1 \le i, j, k \le N$ satisfying $A i + B j + C k = X$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc315_g`](../../analysis/AtCoder-abc315_g.md) | G. Ai + Bj + Ck = X (1 <= i, j, k <= N) | 2315 | Given $N, A, B, C, X$, count the number of triples $(i, j, k)$ with $1 \le i, j, k \le N$ satisfying $A i + B j + C k = ... |
