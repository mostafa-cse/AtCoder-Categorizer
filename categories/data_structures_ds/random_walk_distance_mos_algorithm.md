# Mo's Algorithm

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Mo's Algorithm`

## Description
This topic focuses on mo's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If $|X| \ge N$, the sign of $x' - X$ is constant, giving answer $|X|$. For $|X| < N$, letting $M = \lceil (N + X) / 2 \rceil$, algebraic expansion yields $\mathbb{E}[|x' - X|] = -X + 2^{-(N-1)} ((N + X) f(N, M) - 2 g(N, M))$, where $f(N, M) = \sum_{i=0}^{M-1} \binom{N}{i}$ and $g(N, M) = \sum_{i=0}^{M-1} i \binom{N}{i}$. Both $f$ and $g$ admit $O(1)$ transitions under $N \to N \pm 1$ and $M \to M \pm 1$, enabling Mo's Algorithm over the 2D query points $(N, M)$ in $O(N \sqrt{T})$ time.
- Common Reductions: Compute the expected distance $\mathbb{E}[|x' - X|]$ after an $N$-step 1D random walk across $T$ offline queries modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc463_g`](../../analysis/AtCoder-abc463_g.md) | G - Random Walk Distance | 2452 | Compute the expected distance $\mathbb{E}[|x' - X|]$ after an $N$-step 1D random walk across $T$ offline queries modulo ... |
