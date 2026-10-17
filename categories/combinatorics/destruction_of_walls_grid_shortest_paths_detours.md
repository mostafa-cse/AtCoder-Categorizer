# Large Factorials and Binomial Coefficients

**Taxonomy Path**: `Combinatorics` > `Factorials and Binomial Coefficients (nCr)` > `Large Factorials and Binomial Coefficients`

## Description
This topic focuses on large factorials and binomial coefficients techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any path from (1, 1) to (H, W) requires at least L = H + W - 2 walls. For K < L: 0 ways. For K = L: exactly C(L, H - 1) shortest paths. For K = L + 1: one shortest path plus 1 extra unused wall, C(L, H - 1) * (E - L). For K = L + 2 = H + W: paths have length L (with 2 extra walls, minus double-counted pairs forming a 1x1 square) plus simple detour paths of length H + W (moving once away from (H, W)).
- Common Reductions: Count the number of ways to demolish K walls in an H x W grid such that the top-left room can reach the bottom-right room, given K <= H + W.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc203_c`](../../analysis/AtCoder-arc203_c.md) | Destruction of Walls | 2248 | Count the number of ways to demolish K walls in an H x W grid such that the top-left room can reach the bottom-right roo... |
