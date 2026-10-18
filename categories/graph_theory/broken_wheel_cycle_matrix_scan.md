# Cycle Detection

**Taxonomy Path**: `Graph Theory` > `Cycles` > `Cycle Detection`

## Description
This topic focuses on cycle detection techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A wheel graph consists of a center hub connected to an $N$-cycle. Directing the hub edges determines the in-degree contribution to each rim vertex from the center. The remaining rim edges form a cycle of dependencies where each edge can be oriented clockwise, counterclockwise, or be absent. This defines a transfer matrix scan along the cycle of length $N$, solved via matrix multiplication or dynamic programming in $O(N)$ time.
- Common Reductions: Count the number of valid orientations of a wheel graph with missing rim edges such that all vertex in-degrees match given constraints.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc193_b`](../../analysis/AtCoder-arc193_b.md) | B - Broken Wheel | 2420 | Count the number of valid orientations of a wheel graph with missing rim edges such that all vertex in-degrees match giv... |
