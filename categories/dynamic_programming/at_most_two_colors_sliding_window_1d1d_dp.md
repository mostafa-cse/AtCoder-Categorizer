# 1D1D DP Optimization

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `1D1D DP Optimization`

## Description
This topic focuses on 1d1d dp optimization techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any valid window of size K, one color always occupies the final square. The state collapses to dp[i-1], the rightmost occurrence of the other color within the window, plus a variable sing tracking monochrome K-windows.
- Common Reductions: Count colorings where every K-window has at most 2 colors by tracking the rightmost position of the second-to-last color in a 1D DP and optimizing transitions with sliding window prefix sums in O(N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc279_g`](../../analysis/AtCoder-abc279_g.md) | At Most 2 Colors | 2431 | Count colorings where every K-window has at most 2 colors by tracking the rightmost position of the second-to-last color... |
