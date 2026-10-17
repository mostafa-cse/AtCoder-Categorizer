# Maximum Flow / Minimum Cut

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Flow / Minimum Cut`

## Description
This topic focuses on maximum flow / minimum cut techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A simple path connecting $A$ and $C$ via $B$ exists if and only if there exist two vertex-disjoint paths from $B$ to $A$ and from $B$ to $C$ (sharing no vertices other than $B$). We split every vertex $u \ne B$ into $u_{in} \to u_{out}$ with capacity 1 (and $B_{in} \to B_{out}$ with capacity 2). Source $S$ connects to $B_{in}$ with capacity 2; $A_{out}$ and $C_{out}$ connect to Sink $T$ with capacity 1. A valid path exists if and only if the maximum flow is 2.
- Common Reductions: Given a connected undirected graph $G$ and distinct vertices $A, B, C$. Determine if there exists a simple path from $A$ to $C$ passing through $B$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc318_g`](../../analysis/AtCoder-abc318_g.md) | G. Typical Path Problem | 2260 | Given a connected undirected graph $G$ and distinct vertices $A, B, C$. Determine if there exists a simple path from $A$... |
