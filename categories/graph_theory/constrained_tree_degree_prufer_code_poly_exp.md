# Prufer Code

**Taxonomy Path**: `Graph Theory` > `Graph Counting` > `Prufer Code`

## Description
This topic focuses on prufer code techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If $1 \notin S$, no tree can exist and the answer is 0. If $1 \in S$, $F(0) = 1 \ne 0$, so $F(x)^N = \exp(N \ln F(x))$. Polynomial inversion, differentiation, integration, and Newton's method for $\exp$ compute the required coefficient in $O(N \log N)$.
- Common Reductions: Count labeled trees on $N$ vertices where every vertex degree belongs to subset $S$. By Cayley's tree formula and Prüfer sequences, the degrees satisfy $\sum_{i=1}^N (d_i - 1) = N - 2$, and the number of trees with a fixed degree sequence is $(N - 2)! / \prod (d_i - 1)!$. Setting $k_i = d_i - 1$, this equals $(N - 2)! [x^{N-2}] F(x)^N$ where $F(x) = \sum_{d \in S} \frac{x^{d-1}}{(d-1)!}$. Since every tree with $N \ge 2$ has leaves ($1 \in S$), $F(0) = 1$. The power $F(x)^N$ is computed using polynomial $\ln$ and $\exp$ via NTT in $O(N \log N)$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc303_h`](../../analysis/AtCoder-abc303_h.md) | Ex. Constrained Tree Degree | 2501 | Count labeled trees on $N$ vertices where every vertex degree belongs to subset $S$. By Cayley's tree formula and Prüfer... |
