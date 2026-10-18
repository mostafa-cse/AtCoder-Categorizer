# Binary Search

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Binary Search`

## Description
This topic focuses on binary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When evaluating whether a monster of health H can be defeated in T turns, casting spell i when k turns remain contributes min(t_i, k) * d_i damage. Since each turn's contribution is independent, the optimal strategy greedily maximizes F(k) = max(max_{t_i <= k}(t_i d_i), k * max_{t_i > k} d_i) at each remaining turn k.
- Common Reductions: Find the earliest turn T to defeat a monster of health H given N spells dealing d_i damage for t_i turns. Binary searching on T allows greedy damage evaluation at each remaining turn k as max(max_{t_i <= k}(t_i d_i), k * max_{t_i > k} d_i); summing over piecewise linear segments in O(N) per test evaluates in O(N log(H)) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc303_f`](../../analysis/AtCoder-abc303_f.md) | F. Damage over Time | 2381 | Find the earliest turn T to defeat a monster of health H given N spells dealing d_i damage for t_i turns. Binary searchi... |
