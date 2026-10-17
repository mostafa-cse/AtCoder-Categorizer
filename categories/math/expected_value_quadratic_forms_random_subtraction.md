# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The final element x is a linear combination x = sum c_i A_i with signs c_i in {-1, +1}. Expanding the square gives x^2 = sum A_i^2 + 2 sum_{i < j} c_i c_j A_i A_j. By symmetry, E[c_i c_j] = rho_N is identical for all pairs i != j. A martingale / tree recurrence shows sum_{i < j} E[c_i c_j] = -N / 3 for N >= 3, giving rho_N = -2 / (3 * (N - 1)). Thus, E[x^2] = sum A_i^2 + rho_N * ((sum A_i)^2 - sum A_i^2).
- Common Reductions: Find the expected value of x^2 modulo 998244353 where x is the remaining element after repeatedly picking two random elements a, b and replacing them with a - b.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc450_g`](../../analysis/AtCoder-abc450_g.md) | Random Subtraction | 2227 | Find the expected value of x^2 modulo 998244353 where x is the remaining element after repeatedly picking two random ele... |
