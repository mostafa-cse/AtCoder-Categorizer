# Splitting Objects into Light and Heavy / Case Processing

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Splitting Objects into Light and Heavy / Case Processing`

## Description
This topic focuses on splitting objects into light and heavy / case processing techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A vertex is heavy if $\deg(u) \ge B = \Theta(\sqrt{M})$ and light otherwise. Each heavy vertex has at most $O(\sqrt{M})$ heavy neighbors. Updates propagate lazily: a vertex's true current value is the latest update among its direct update and updates stored on its heavy neighbors.
- Common Reductions: In a graph of $N$ vertices and $M$ edges where each vertex initially has value $x$, process $Q$ operations where choosing vertex $x$ sets the values of $x$ and all its neighbors to $x$'s current value.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc219_g`](../../analysis/AtCoder-abc219_g.md) | G. Propagation | 2287 | In a graph of $N$ vertices and $M$ edges where each vertex initially has value $x$, process $Q$ operations where choosin... |
