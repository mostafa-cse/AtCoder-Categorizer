# Basic SQRT Decomposition

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Basic SQRT Decomposition`

## Description
This topic focuses on basic sqrt decomposition techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because $h_i \le 10$, each stone $x$ can only be reached from stones in $[x - 10, x - 1]$. The transitions form a linear recurrence of order 10 represented by a $10 \times 10$ transition matrix. With $N \le 300,000$, we partition stones into blocks of size $B = 500$. For each block, we precompute the cumulative $10 \times 10$ transition matrix in $O(100 B)$ time. For each query $(s, t)$, multiplying a $1 \times 10$ state vector across full blocks takes only $10 \times 10 = 100$ operations per block, and partial boundaries take scalar DP, answering each query in $O(B + (N/B) \times 100)$ time.
- Common Reductions: Count the number of jump paths from stone $s$ to $t$ modulo 1000000007 across $D \le 5000$ queries on stones with jump limit $h_i \le 10$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc027_4`](../../analysis/AtCoder-arc027_4.md) | D - ぴょんぴょんトレーニング | 2474 | Count the number of jump paths from stone $s$ to $t$ modulo 1000000007 across $D \le 5000$ queries on stones with jump l... |
