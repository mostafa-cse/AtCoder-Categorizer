# Maximum Closure Problem

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Closure Problem`

## Description
This topic focuses on maximum closure problem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In an $S-T$ cut where $u \in S$ means square $u$ is chosen: if $u$ is not chosen ($u \in T$), we lose $A_{i, j}$ (edge $S \to u$ with capacity $A_{i, j}$). If $u$ is chosen and its diagonal predecessor $v$ is not chosen, directed edge $u \to v$ is cut with cost $C$. If no predecessor exists, edge $u \to T$ has capacity $C$. Max score = $\sum A_{i, j} - \text{MinCut}$.
- Common Reductions: Given an $H \times W$ grid with values $A_{i, j}$, choose squares to draw X's on to maximize $\sum A_{i, j} - C \times (\text{number of segments})$. A main diagonal segment starts at $(i, j)$ if $(i, j)$ is chosen and $(i-1, j-1)$ is NOT chosen. An anti diagonal segment starts at $(i, j)$ if $(i, j)$ is chosen and $(i-1, j+1)$ is NOT chosen. Model as Min-Cut on a flow network.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc225_g`](../../analysis/AtCoder-abc225_g.md) | G. X | 2566 | Given an $H \times W$ grid with values $A_{i, j}$, choose squares to draw X's on to maximize $\sum A_{i, j} - C \times (... |
