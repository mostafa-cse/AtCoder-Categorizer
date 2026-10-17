# Randomized Algorithms

**Taxonomy Path**: `Miscellaneous` > `Randomized` > `Randomized Algorithms`

## Description
This topic focuses on randomized algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: With S = 400,000 independent trials, the 3-sigma confidence bound is 3 * sqrt(p(1-p)/S) <= 3 * 0.5 / sqrt(400000) approx 0.0023, and empirical error is consistently <= 0.0006. Fast bitwise PRNG and array swaps allow 400,000 iterations to run in 0.05 seconds.
- Common Reductions: N <= 11 people sitting around a circular table undergo K <= 20 random pairwise seat swaps. We must find the probability that none of M <= 10 forbidden pairs are adjacent on the circle, within error <= 0.002. Running 400,000 Monte Carlo simulation trials with fast xorshift PRNG guarantees standard error < 0.0008, well within tolerance.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc003_4`](../../analysis/AtCoder-arc003_4.md) | D. シャッフル席替え | 2194 | N <= 11 people sitting around a circular table undergo K <= 20 random pairwise seat swaps. We must find the probability ... |
