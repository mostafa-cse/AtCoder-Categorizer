# Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Generating Functions`

## Description
This topic focuses on generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By the tail sum formula for expectation, E[X] equals sum_{k=0}^N P(X > k). Drawing k socks of distinct colors is equivalent to selecting k distinct colors and 1 sock from each, whose combinatorial count is precisely the coefficient of x^k in the generating function prod_{i=1}^N (1 + A_i x).
- Common Reductions: Compute the expected number of draws to obtain a matching pair by linearity of expectation E[X] = sum P(X > k), where P(X > k) is the probability that the first k drawn socks are all of distinct colors, expressed as [x^k] prod(1 + A_i x) / C(S, k) via Divide and Conquer NTT.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc352_g`](../../analysis/AtCoder-abc352_g.md) | Socks 3 | 2413 | Compute the expected number of draws to obtain a matching pair by linearity of expectation E[X] = sum P(X > k), where P(... |
