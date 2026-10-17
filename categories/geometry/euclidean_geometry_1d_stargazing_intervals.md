# Euclidean Geometry

**Taxonomy Path**: `Geometry` > `Euclidean Geometry` > `Euclidean Geometry`

## Description
This topic focuses on euclidean geometry techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each person $i$'s claim implies that at least one star must be placed at $x_i - d_i$ or $x_i + d_i$, and NO star may be placed strictly inside the open interval $(x_i - d_i, x_i + d_i)$.
A coordinate $pos \in \{x_i - d_i, x_i + d_i\}$ is valid if it does not fall into any other person's forbidden interval. Crucially, by monotonicity of $x_i$, checking validity against the immediately adjacent neighbors $i-1$ and $i+1$ is both necessary and sufficient! Person $i$ is valid if at least one of $x_i - d_i$ or $x_i + d_i$ is not strictly inside $(x_{i-1} - d_{i-1}, x_{i-1} + d_{i-1})$ and not strictly inside $(x_{i+1} - d_{i+1}, x_{i+1} + d_{i+1})$. Maintaining the count of invalid people allows $O(1)$ updates per query affecting only $P-1, P, P+1$.
- Common Reductions: There are $N$ people on a 1D line at coordinates $x_1 < x_2 < \dots < x_N$. Each person claims the distance to their nearest star is $d_i$. Stars can be placed at any coordinates. We must determine if a valid star configuration exists, supported under $Q$ point updates on $d_i$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc231_c`](../../analysis/AtCoder-arc231_c.md) | C. One Sky, Many Stars | 2267 | There are $N$ people on a 1D line at coordinates $x_1 < x_2 < \dots < x_N$. Each person claims the distance to their nea... |
