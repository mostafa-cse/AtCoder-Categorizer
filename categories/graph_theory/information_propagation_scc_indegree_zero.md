# Strongly Connected Components (SCC)

**Taxonomy Path**: `Graph Theory` > `Graph Connectivity` > `Strongly Connected Components (SCC)`

## Description
This topic focuses on strongly connected components (scc) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Ally $u$ can transmit a message to ally $v$ safely if and only if $\text{dist}^2(u, v) < R_u^2$, where $R_u^2 = \min_{k} \text{dist}^2(u, \text{spy}_k)$ is the squared distance from $u$ to the nearest spy. This defines a directed transmission graph. Within any strongly connected component (SCC), informing any one node informs all nodes in the component. Contracting the graph into its DAG of SCCs, the minimum number of nodes to inform equals the number of SCCs with in-degree zero.
- Common Reductions: Find the minimum number of ally nodes to directly inform such that all $N$ allies receive the message without being intercepted by any of the $M$ spies.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc010_4`](../../analysis/AtCoder-arc010_4.md) | D - 情報伝播 | 2481 | Find the minimum number of ally nodes to directly inform such that all $N$ allies receive the message without being inte... |
