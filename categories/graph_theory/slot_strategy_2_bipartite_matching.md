# Halls Theorem

**Taxonomy Path**: `Graph Theory` > `Matching` > `Halls Theorem`

## Description
This topic focuses on halls theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since there are only $N \le 100$ reels, each reel needs to consider at most its first $N$ occurrences of digit $d$ in the periodic reel. Across all reels, at most $N^2 \le 10000$ candidate times exist. Bipartite matching with binary search on candidate times $T$ verifies solvability.
- Common Reductions: Find the minimum time $T$ to stop $N$ slot reels at identical digits, where at most one reel can be stopped at any time $t$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc320_g`](../../analysis/AtCoder-abc320_g.md) | G. Slot Strategy 2 (Hard) | 2575 | Find the minimum time $T$ to stop $N$ slot reels at identical digits, where at most one reel can be stopped at any time ... |
