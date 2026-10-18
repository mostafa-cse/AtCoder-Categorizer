# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The number of internally connected configurations $c(S)$ is computed via standard subset DP: $c(S) = g(S) - \sum_{T \subset S, v \in T} c(T) g(S \setminus T)$, where $g(S) = (cntR(S))!$ if $cntR(S) == cntB(S)$, else 0.
- Common Reductions: Find the expected number of connected components when $M$ cables randomly connect $M$ red terminals and $M$ blue terminals attached to $N \le 16$ circuit parts. By linearity of expectation, total components is $\sum_{S \subseteq V} [S \text{ is a connected component}]$. A subset $S$ forms an isolated connected component iff it has equal red and blue terminals ($cntR(S) = cntB(S) = k$), and its internal subgraph is connected ($c(S)$ ways).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc321_g`](../../analysis/AtCoder-abc321_g.md) | G. Electric Circuit | 2439 | Find the expected number of connected components when $M$ cables randomly connect $M$ red terminals and $M$ blue termina... |
