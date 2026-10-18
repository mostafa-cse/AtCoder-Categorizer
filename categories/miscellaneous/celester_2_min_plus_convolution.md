# Min Plus Convolution (Convex and Convex)

**Taxonomy Path**: `Miscellaneous` > `Min Plus Convolution` > `Min Plus Convolution (Convex and Convex)`

## Description
This topic focuses on min plus convolution (convex and convex) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Pad string as S' = 'S' + S + 'R'. Then happiness is (b - 1) / 2, where b is the number of adjacent character differences in S'. Mapping differences to a 01-sequence, flipping a character toggles two adjacent bits. Increasing the number of 1s corresponds to pairing up 0s. The minimum cost to increase happiness by 1 (creating two new 1s) from an array D of distances between adjacent 0s corresponds to choosing non-adjacent elements from D with minimal sum. The cost function is convex, allowing a min-plus convolution / regret greedy algorithm with priority queue and doubly-linked list (Candies algorithm) in O(N log N).
- Common Reductions: Given a weather string S of length N ('S' or 'R'), we can flip at most k characters. Happiness is the number of "RS" substrings. For each k = 0, ..., N, find the maximum happiness achievable with at most k flips.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc464_g`](../../analysis/AtCoder-abc464_g.md) | G. Celester 2 | 2592 | Given a weather string S of length N ('S' or 'R'), we can flip at most k characters. Happiness is the number of "RS" sub... |
