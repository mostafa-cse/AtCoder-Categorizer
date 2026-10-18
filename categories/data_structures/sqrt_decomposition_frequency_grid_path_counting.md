# Basic SQRT Decomposition

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Basic SQRT Decomposition`

## Description
This topic focuses on basic sqrt decomposition techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If a color appears <= B times, pairwise binomial calculation takes O(B^2) time. If a color appears > B times, there are at most N^2 / B such heavy colors, and for each we can run a single O(N^2) grid DP.
- Common Reductions: Count pairs of grid cells (r1, c1) and (r2, c2) with r1 <= r2, c1 <= c2 having the same color, weighted by the number of monotonic paths binom((r2-r1)+(c2-c1), r2-r1). Balance workload using Square Root Decomposition on color frequencies.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc259_h`](../../analysis/AtCoder-abc259_h.md) | Ex. Yet Another Path Counting | 2406 | Count pairs of grid cells (r1, c1) and (r2, c2) with r1 <= r2, c1 <= c2 having the same color, weighted by the number of... |
