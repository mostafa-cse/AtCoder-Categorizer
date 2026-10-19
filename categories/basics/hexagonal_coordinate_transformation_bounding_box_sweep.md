# Two Pointers

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Two Pointers`

## Description
This topic focuses on two pointers techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Mapping (X, Y) -> (X, Y, X - Y) embeds the hexagonal metric into 3D Chebyshev space. By Helly's property for L_infinity balls, all pairwise distances are <= D iff all points fit in a bounding box [X, X+D] x [Y, Y+D] x [Z, Z+D]. Subsets are uniquely counted by their coordinate minima (X, Y, Z). For fixed X and Y, maintaining points in the Z-window [Z, Z+D] with two pointers allows evaluating PIE over the 8 boundary conditions in O(1) per step, yielding an O(N^3) total algorithm.
- Common Reductions: On a hexagonal grid, distance is d((i1, j1), (i2, j2)) = max(|i1 - i2|, |j1 - j2|, |(i1 - j1) - (i2 - j2)|). Given N points, count non-empty subsets where all pairwise distances are <= D modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc280_g`](../../analysis/AtCoder-abc280_g.md) | G - Do Use Hexagon Grid 2 | 2842 | On a hexagonal grid, distance is d((i1, j1), (i2, j2)) = max(|i1 - i2|, |j1 - j2|, |(i1 - j1) - (i2 - j2)|). Given N poi... |
