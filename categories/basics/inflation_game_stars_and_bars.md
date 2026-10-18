# Stars and Bars

**Taxonomy Path**: `Basics` > `Basic Counting` > `Stars and Bars`

## Description
This topic focuses on stars and bars techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since multiplication cards multiply all previous additions, all addition cards played before a multiplication card benefit from that factor. By Stars and Bars and linearity of expectation, the expected coefficient of each addition card depends symmetrically on the number of multiplication cards drawn after it. The distribution of multiplication cards among addition cards follows a negative hypergeometric / elementary symmetric polynomial distribution that can be computed via DP.
- Common Reductions: We are given A addition cards and B multiplication cards. In each round, we choose a card to play. Addition cards add values to the total score, while multiplication cards multiply the score by factors. Find the expected maximum final score over all possible card draws.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc034_4`](../../analysis/AtCoder-arc034_4.md) | D. インフレゲーム (Inflation Game) | 2570 | We are given A addition cards and B multiplication cards. In each round, we choose a card to play. Addition cards add va... |
