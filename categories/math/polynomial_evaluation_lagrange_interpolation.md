# Lagrange Interpolation

**Taxonomy Path**: `Math` > `Polynomial` > `Lagrange Interpolation`

## Description
This topic focuses on lagrange interpolation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The denominator $\prod_{j \ne i} (i - j) = i! \times (N - i)! \times (-1)^{N - i}$ decomposes into precomputed factorials. The numerator $\prod_{j \ne i} (T - j)$ is computed in $O(1)$ per term using prefix and suffix product arrays.
- Common Reductions: Given polynomial $P(x)$ of degree $N$ evaluated at points $x = 0, 1, \dots, N$, compute $P(T) \pmod{10^9+7}$. For consecutive integer sample points, Lagrange Interpolation simplifies to $O(N)$ using prefix and suffix products of $(T - j)$ and factorial inverses for the denominator $(i - j)!$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc033_4`](../../analysis/AtCoder-arc033_4.md) | D. 見たことのない多項式 | 2470 | Given polynomial $P(x)$ of degree $N$ evaluated at points $x = 0, 1, \dots, N$, compute $P(T) \pmod{10^9+7}$. For consec... |
