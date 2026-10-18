# Stern-Brocot Tree and Rational Approximation

**Taxonomy Path**: `Miscellaneous` > `General` > `Stern-Brocot Tree and Rational Approximation`

## Description
This topic focuses on stern-brocot tree and rational approximation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The best rational approximations of a real number are found via continued fractions or descending the Stern-Brocot Tree. The Stern-Brocot Tree maintains a bracket $(\frac{p_1}{q_1}, \frac{p_2}{q_2})$ containing $r$, starting with $\frac{0}{1}$ and $\frac{1}{1}$. The mediant $\frac{p_1 + p_2}{q_1 + q_2}$ is compared against $r$. To handle $N \le 10^{18}$ in logarithmic time, accelerated leaps (Euclidean division on continued fraction quotients) jump multiple mediants at once.
- Common Reductions: Given a real number $r \in [0, 1]$ with up to 18 decimal places and an integer $N \le 10^{18}$, find a reduced fraction $p / q$ with $0 \le p \le q \le N$ and $\gcd(p, q) = 1$ that minimizes $|r - p / q|$. In case of a tie, choose the smaller fraction.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc333_g`](../../analysis/AtCoder-abc333_g.md) | G. Nearest Fraction | 2536 | Given a real number $r \in [0, 1]$ with up to 18 decimal places and an integer $N \le 10^{18}$, find a reduced fraction ... |
