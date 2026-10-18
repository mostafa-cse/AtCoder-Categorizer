# Difference Array

**Taxonomy Path**: `Basics` > `More Techniques` > `Difference Array`

## Description
This topic focuses on difference array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A syllable starts at index 0 if $(A_0 + k) \bmod K$ is a vowel, or at index $i \ge 1$ if $(A_{i-1} + k) \bmod K$ is a non-vowel and $(A_i + k) \bmod K$ is a vowel. The transition frequencies between $(K - A_i) \bmod K$ and $(K - A_{i-1}) \bmod K$ can be viewed as coefficients of a 2D bivariate polynomial $A(x, y)$, and the required counts correspond to the cyclic convolution of $A$ with non-vowel indicator $S(x)$ and vowel indicator $T(y)$. Decomposing into independent 1D circular convolutions via NTT solves all $K$ shifts efficiently.
- Common Reductions: Count the number of vowel syllables for each cyclic shift $k \in [0, K-1]$ of an array $A$ generated via a linear congruential PRNG.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc471_g`](../../analysis/AtCoder-abc471_g.md) | G - Caeser Syllables | 2464 | Count the number of vowel syllables for each cyclic shift $k \in [0, K-1]$ of an array $A$ generated via a linear congru... |
