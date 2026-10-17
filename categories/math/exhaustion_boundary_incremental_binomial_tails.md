# Gambler's Ruin

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Gambler's Ruin`

## Description
This topic focuses on gambler's ruin techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Before either color is exhausted, each chocolate chosen is Black with probability $1/2$. Once White is exhausted, all remaining chocolates are Black with probability 1; once Black is exhausted, Black has probability 0.
- Common Reductions: Given $B$ black and $W$ white chocolates, repeatedly choose Black or White with equal probability and eat one if available. Find the probability that the $i$-th chocolate eaten is Black for all $i = 1, \dots, B+W$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-exawizards2019_e`](../../analysis/AtCoder-exawizards2019_e.md) | E. Black or White | 2309 | Given $B$ black and $W$ white chocolates, repeatedly choose Black or White with equal probability and eat one if availab... |
