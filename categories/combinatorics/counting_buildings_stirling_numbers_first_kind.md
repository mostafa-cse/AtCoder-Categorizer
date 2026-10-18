# Stirling Number of the First Kind for Fixed N

**Taxonomy Path**: `Combinatorics` > `Stirling Numbers` > `Stirling Number of the First Kind for Fixed N`

## Description
This topic focuses on stirling number of the first kind for fixed n techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The row of unsigned Stirling numbers of the first kind $\left[ \begin{matrix} N-1 \\ m \end{matrix} \right]$ is computed by expanding the polynomial $\prod_{i=0}^{N-2} (y + i)$ using divide-and-conquer NTT in $O(N \log^2 N)$. Then $(t + t^{-1})^m = \sum_{j=0}^m \binom{m}{j} t^{m - 2j}$. Extracting the coefficient of $t^K$ corresponds to summing $\left[ \begin{matrix} N-1 \\ m \end{matrix} \right] \binom{m}{(m + K)/2}$ over all $m \equiv K \pmod 2$.
- Common Reductions: Count permutations of $1 \dots N$ where the difference between visible buildings from the left and visible buildings from the right is $K$. When inserting element $x$ from 2 to $N$ into a permutation of $1 \dots x - 1$: placing at the left end increases $L - R$ by $+1$ (1 choice), placing at the right end decreases $L - R$ by $-1$ (1 choice), and placing in the interior leaves $L - R$ unchanged ($x - 2$ choices). The generating function is $\prod_{i=0}^{N-2} (t + t^{-1} + i)$, which expands to $\sum_{m} \left[ \begin{matrix} N-1 \\ m \end{matrix} \right] (t + t^{-1})^m$ via unsigned Stirling numbers of the first kind.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc385_g`](../../analysis/AtCoder-abc385_g.md) | G. Counting Buildings | 2492 | Count permutations of $1 \dots N$ where the difference between visible buildings from the left and visible buildings fro... |
