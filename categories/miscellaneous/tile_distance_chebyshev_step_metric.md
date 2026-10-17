# Manhattan <> Chebyshev

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Manhattan <> Chebyshev`

## Description
This topic focuses on manhattan <> chebyshev techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A grid point (x, y) belongs to a KxK block ((x/K), (y/K)). Blocks with odd coordinate sum are large tiles, and those with even coordinate sum are sets of K^2 1x1 tiles. Inside large tiles, motion is free along any direction. When stepping between adjacent large tiles (which meet at small tile borders), diagonal steps cost 2 and axis-aligned steps of 2 blocks cost min(4, K+1).
- Common Reductions: Multi-scale grid distance reduction between 1x1 small tiles and KxK large tiles via Chebyshev diagonal metric with axis-aligned step cost.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc353_f`](../../analysis/AtCoder-abc353_f.md) | Tile Distance | 2201 | Multi-scale grid distance reduction between 1x1 small tiles and KxK large tiles via Chebyshev diagonal metric with axis-... |
