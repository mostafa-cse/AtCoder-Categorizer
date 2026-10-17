# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Impartial game under normal play governed by the Sprague-Grundy theorem. Picking an interval [L_i, R_i) inside available subsegment [l, r) partitions the state into two independent subgames [l, L_i) and [R_i, r). The Grundy value of the transition is g(l, L_i) ^ g(R_i, r). State transitions can be precomputed using range DP over segment lengths in O(V^2 N) where V = 100.
- Common Reductions: Two players alternately pick non-overlapping intervals from N given intervals [L_i, R_i) on line [1, 100]. The last player to move wins. Determine who wins under optimal play.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc206_f`](../../analysis/AtCoder-abc206_f.md) | Interval Game 2 | 2221 | Two players alternately pick non-overlapping intervals from N given intervals [L_i, R_i) on line [1, 100]. The last play... |
