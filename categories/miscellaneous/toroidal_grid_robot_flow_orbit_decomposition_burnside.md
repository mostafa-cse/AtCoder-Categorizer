# Burnside's Lemma / Polya Enumeration Theorem

**Taxonomy Path**: `Miscellaneous` > `General` > `Burnside's Lemma / Polya Enumeration Theorem`

## Description
This topic focuses on burnside's lemma / polya enumeration theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For T = 1, diagonal zones (x - y mod gcd(H, W)) cannot contain both right and down robots. Furthermore, coexistence of stationary robots restricts the grid to pure horizontal or vertical flows. This yields 2^H + 2^W + 2^{\gcd(H, W)} - 3 valid configurations. For general T, the torus decomposes into G_H x G_W independent subgrids where G_H = \gcd(H, T) and G_W = \gcd(W, T), each of size R_X = H / G_H and R_Y = W / G_W.
- Common Reductions: On an H x W toroidal grid, place stationary, right-moving, or down-moving robots such that at times 0, T, 2T, ... every cell has exactly one robot. Count valid configurations modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-ddcc2020_qual_f`](../../analysis/AtCoder-ddcc2020_qual_f.md) | F - DISCOSMOS | 2992 | On an H x W toroidal grid, place stationary, right-moving, or down-moving robots such that at times 0, T, 2T, ... every ... |
