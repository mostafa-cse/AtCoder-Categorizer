# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Euler characteristic and region weighting: assign weight 1/2 to chord endpoints along circular arcs and weight 1 to the unique deepest vertex of interior black regions. In a random chord subset, endpoints receive expected weight 1/4 (total 3N/8), and chord intersections receive expected weight 1/8 if another chord separates them from the center. The total expected weight simplifies to (3N + I + V) / 8, where I is intersecting chord pairs and V counts A_i + K <= A_{i+1}.
- Common Reductions: Given circle circumference L, chord length K (2K < L), and N chords starting at coordinates A_i, find the total number of black regions across all 2^N chord subsets colored in chessboard fashion starting with center region white.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc073_a`](../../analysis/AtCoder-agc073_a.md) | Chords and Checkered | 2219 | Given circle circumference L, chord length K (2K < L), and N chords starting at coordinates A_i, find the total number o... |
