# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By linearity of expectation, the total score is the sum over rounds of the probability that player A's card exceeds player B's card. Through prefix-suffix rank symmetry and telescoping sums, the combinatorial probability reduces to an exact closed form involving factorials and harmonic numbers, computable in linear time O(N).
- Common Reductions: 2N cards labeled 1 to 2N are randomly partitioned into two decks of size N. Players reveal top cards simultaneously; the larger card scores 1 point. Find expected score of player A modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc053_c`](../../analysis/AtCoder-agc053_c.md) | C. Random Card Game | 2878 | 2N cards labeled 1 to 2N are randomly partitioned into two decks of size N. Players reveal top cards simultaneously; the... |
