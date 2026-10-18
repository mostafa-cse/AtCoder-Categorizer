# Divide and Conquer Optimization

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `Divide and Conquer Optimization`

## Description
This topic focuses on divide and conquer optimization techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Snuke can escape Takahashi's blocks iff the number of 'S' (Snuke moves) between consecutive 'B' (block placements) is large enough. Specifically, when $j$ blocks remain to be placed, Snuke requires at least $2^{j-1}$ moves to evade being trapped. Thus, Snuke wins iff between the $j$-th from last block and the next block, there are $\ge 2^{j-1}$ 'S' moves. Takahashi wins iff Snuke does NOT win. Count Snuke winning strings via DP and subtract from $2^Q$. Since $2^j > N$ for $j > 20$, the DP only needs $\le 20$ active block indices.
- Common Reductions: Count strings of 'B', 'S', and '?' such that Takahashi wins the Block Game on an infinite 1D board.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc050_c`](../../analysis/AtCoder-agc050_c.md) | C - Block Game | 2528 | Count strings of 'B', 'S', and '?' such that Takahashi wins the Block Game on an infinite 1D board.... |
