# DP Optimization using Data Structures [Some Practice Problems]

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `DP Optimization using Data Structures [Some Practice Problems]`

## Description
This topic focuses on dp optimization using data structures [some practice problems] techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: At the end of each round, exactly 2 cards (x, y) are retained in hand. Maintain dp[x][y] = maximum score with hand {x, y}. Each round draws 3 cards {a, b, c}. If a == b == c, all dp values increase by 1. Otherwise, we can pair cards from {a, b, c} with cards in hand. The transitions correspond to: global addition, updating rows/columns for values in {a, b, c}, and updating point pairs {u, v} in {a, b, c}. Maintaining row maximums and a global maximum allows all DP transitions in O(1) amortized time per round.
- Common Reductions: Given 3N cards with values in [1, N], initially hold 5 cards. In each of N-1 rounds, draw 3 cards and optionally discard 3 matching cards for 1 point, retaining 2 cards in hand. Maximize the total points.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc176_f`](../../analysis/AtCoder-abc176_f.md) | F. Brave CHAIN | 2912 | Given 3N cards with values in [1, N], initially hold 5 cards. In each of N-1 rounds, draw 3 cards and optionally discard... |
