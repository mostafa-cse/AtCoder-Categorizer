# Vector Space and XOR Basis

**Taxonomy Path**: `Math` > `Linear Algebra` > `Vector Space and XOR Basis`

## Description
This topic focuses on vector space and xor basis techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: On the Boolean hypercube, modular lattice functions $f(x) + f(y) = f(x \land y) + f(x \lor y)$ are exactly linear combinations of the coordinate bits plus a constant. The extreme values of $f$ over all $2^N$ vertices are $a - \sum_{c_i < 0} |c_i|$ and $a + \sum_{c_i > 0} c_i$, making the valid interval for $a$ depend solely on $\sum |c_i|$.
- Common Reductions: Count integer functions $f: \{0, 1\}^N \to [0, K]$ satisfying $f(x) + f(y) = f(x \land y) + f(x \lor y)$. The functional equation forces $f$ to be affine: $f(x) = a + \sum_{i=0}^{N-1} c_i x_i$. Boundedness $0 \le f(x) \le K$ implies $\sum |c_i| \le K$, with $K - \sum |c_i| + 1$ choices for $a$. Grouping by the number of non-zero $c_i$ simplifies via the double hockey stick identity to $\sum_{m=0}^{\min(N, K)} \binom{N}{m} 2^m \binom{K+1}{m+1}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc144_d`](../../analysis/AtCoder-arc144_d.md) | D. AND OR Equation | 2468 | Count integer functions $f: \{0, 1\}^N \to [0, K]$ satisfying $f(x) + f(y) = f(x \land y) + f(x \lor y)$. The functional... |
