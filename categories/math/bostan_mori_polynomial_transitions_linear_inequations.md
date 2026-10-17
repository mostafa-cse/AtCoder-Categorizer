# Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Generating Functions`

## Description
This topic focuses on generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Decomposing x_i = 2 Q_i + R_i with R_i in {0, 1} yields 2 sum A_i Q_i + sum A_i R_i <= M. Let S(x) = prod_{i=1}^N (1 + x^{A_i}). Tracking polynomial coefficients coef where sum coef[M-i] f(A, i) is invariant, each step convolves S with coef and downsamples degrees by factor 2 (M <- M / 2).
- Common Reductions: Count non-negative integer solutions to sum_{i=1}^N A_i x_i <= M modulo 998244353 for M <= 10^18. Solved using binary digit decomposition Bostan-Mori polynomial transitions.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc436_g]` | Linear Inequation | 2164 | Count non-negative integer solutions to sum_{i=1}^N A_i x_i <= M modulo 998244353 for M <= 10^18. Solved using binary di... |
