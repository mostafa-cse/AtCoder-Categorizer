# Slope Trick

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Slope Trick`

## Description
This topic focuses on slope trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Classic Slope Trick / Buy Low Sell High with priority queue replacement. When price P_i exceeds the minimum available price in the min-heap, we greedily pair it with the lowest price, adding P_i - top to profit. We push P_i twice: once representing an option to upgrade the selling price to a future higher price, and once as a buy option.
- Common Reductions: Given daily stock prices P_1, ..., P_N, maximize total profit by choosing to buy 1 share, sell 1 share, or do nothing each day with unlimited holding capacity.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc250_g`](../../analysis/AtCoder-abc250_g.md) | Stonks | 2219 | Given daily stock prices P_1, ..., P_N, maximize total profit by choosing to buy 1 share, sell 1 share, or do nothing ea... |
