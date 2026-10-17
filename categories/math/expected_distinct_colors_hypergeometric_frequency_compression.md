# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By linearity of expectation, the expected number of distinct colors in a sample of size $K$ equals the sum of probabilities that each color is present: $E[C] = \sum_{c} (1 - \binom{N - cnt_c}{K} / \binom{N}{K})$. Grouping colors by frequency compresses the evaluation to at most $\sqrt{2N}$ unique sizes.
- Common Reductions: Given $N$ colored candies with color frequencies $c_1, \dots, c_m$, for each $k = 1, \dots, N$, compute the expected number of distinct colors when choosing $k$ candies uniformly at random modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc215_g`](../../analysis/AtCoder-abc215_g.md) | G. Colorful Candies 2 | 2276 | Given $N$ colored candies with color frequencies $c_1, \dots, c_m$, for each $k = 1, \dots, N$, compute the expected num... |
