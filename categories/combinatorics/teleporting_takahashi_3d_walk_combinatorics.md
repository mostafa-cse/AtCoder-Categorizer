# Large Factorials and Binomial Coefficients

**Taxonomy Path**: `Combinatorics` > `Factorials and Binomial Coefficients (nCr)` > `Large Factorials and Binomial Coefficients`

## Description
This topic focuses on large factorials and binomial coefficients techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In 3D, choosing which $C$ of the $N$ steps move in $Z$ leaves $M = N - C$ steps for the $XY$-plane. In each of the $M$ steps, exactly one of $X$ or $Y$ moves by $\pm 1$. Rotating coordinates via $U = X + Y$ and $V = X - Y$ means in every step $(U, V)$ changes by $(\pm 1, \pm 1)$ independently, decoupling $U$ and $V$ into independent binomial distributions.
- Common Reductions: Count $N$-step 3D lattice walks from $(0, 0, 0)$ to $(X, Y, Z)$ where each step changes one coordinate by $\pm 1$. Iterate over the number of steps $C$ allocated to the $Z$-axis. The remaining $M = N - C$ steps in 2D rotate by 45 degrees: $(x, y) \to (x+y, x-y)$, decomposing the 2D walk into two independent 1D walks of length $M$ with steps in $\{+1, -1\}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc240_g`](../../analysis/AtCoder-abc240_g.md) | G. Teleporting Takahashi | 2462 | Count $N$-step 3D lattice walks from $(0, 0, 0)$ to $(X, Y, Z)$ where each step changes one coordinate by $\pm 1$. Itera... |
