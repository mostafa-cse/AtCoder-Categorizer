# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each bean in bowl i moves independently according to the rules of an impartial game, so the game is equivalent to Nim by Sprague-Grundy theorem. The Grundy value g(i) of a bean at bowl i is the mex of Grundy values of bowls reachable in one step: g(i) = mex { g(i - j) | 1 <= j <= C_i }. A bean at bowl i contributes g(i) to the XOR sum if moved an odd number of times; specifically, since beans move independently, bowl i contributes (B_i mod 2) * g(i) to the global Nim sum. To compute g(i) in O(log N) time, maintain the latest occurrence index of each Grundy value in a segment tree, and find the minimum value whose last occurrence is < i - C_i.
- Common Reductions: We are given N bowls containing beans. A bean at bowl i can be moved to bowl i - j (1 <= j <= C_i) with at most A_i beans moved in total from bowl i. Determine if the first player has a winning strategy in this impartial game.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc038_c`](../../analysis/AtCoder-arc038_c.md) | C. 茶碗と豆 (Bowls and Beans) | 2531 | We are given N bowls containing beans. A bean at bowl i can be moved to bowl i - j (1 <= j <= C_i) with at most A_i bean... |
