# Matrix Exponentiation

**Taxonomy Path**: `Math` > `Matrices` > `Matrix Exponentiation`

## Description
This topic focuses on matrix exponentiation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For repunits $R_k = (10^k - 1)/9$, $\gcd(R_A, R_B) = R_{\gcd(A, B)}$. Consequently, $\text{lcm}(R_A, R_B) = R_A \cdot \frac{R_B}{R_{\gcd(A, B)}} = R_A \sum_{j=0}^{B/\gcd(A, B) - 1} (10^{\gcd(A, B)})^j$. Both factors are geometric sums $\sum_{i=0}^{L-1} r^i$ evaluated modulo $M$ via $2 \times 2$ matrix exponentiation.
- Common Reductions: Compute $\text{lcm}(R_A, R_B) \pmod M$ for repunits. Using $\gcd(R_A, R_B) = R_{\gcd(A, B)}$, the LCM factors into two geometric series $R_A$ and $\sum (10^{\gcd(A, B)})^j$, each evaluated via $2 \times 2$ matrix exponentiation in $O(\log A + \log B)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc050_c`](../../analysis/AtCoder-arc050_c.md) | C. LCM 111 | 2372 | Compute $\text{lcm}(R_A, R_B) \pmod M$ for repunits. Using $\gcd(R_A, R_B) = R_{\gcd(A, B)}$, the LCM factors into two g... |
