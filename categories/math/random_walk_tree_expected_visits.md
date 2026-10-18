# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each branch behaves as a 1D random walk with reflecting/absorbing boundaries. The central hub is visited between branch explorations. By analyzing the expected time to explore a new branch conditioned on having already visited k distinct branches, the total expected time decomposes into branch traversal times and the coupon collector waiting time (harmonic numbers H_N = sum_{i=1}^N 1/i). The overall expected number of steps until every vertex is visited evaluates cleanly to M^2 * (2N * H_N - 1).
- Common Reductions: The expected cover time for a random walk on a symmetric star graph with N branches of length M reduces via Markov chain linearity, gambler's ruin, and coupon collector's harmonic numbers to the exact closed form: M^2 * (2N * H_N - 1) modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc185_d`](../../analysis/AtCoder-arc185_d.md) | Random Walk on Tree | 2649 | The expected cover time for a random walk on a symmetric star graph with N branches of length M reduces via Markov chain... |
