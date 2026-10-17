# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Decomposing poles into independent contiguous blocks where adjacent gaps are <= H simplifies the state: within each block, pole i is the last to fall iff all poles to its left fall left and all poles to its right fall right. The number of preceding events equals the monotonic stack sizes for running minima to the left and right. Aggregating block completion distributions using a segment tree computes the exact probability that all N poles have fallen by earthquake t in O(N log N) time.
- Common Reductions: Given $N$ poles of height $H$ at coordinates $X_i$, each falling left or right with probability $1/2$ during sequential earthquakes, compute the probability that all poles have fallen by exactly the $t$-th earthquake multiplied by $2^N$ for all $t = 1, \dots, N$ modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc177_d`](../../analysis/AtCoder-arc177_d.md) | D. Earthquakes | 2299 | Given $N$ poles of height $H$ at coordinates $X_i$, each falling left or right with probability $1/2$ during sequential ... |
