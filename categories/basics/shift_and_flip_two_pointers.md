# Two Pointers

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Two Pointers`

## Description
This topic focuses on two pointers techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Fix the net shift s in [-(N-1), N-1]. The shift path starting at 0 and ending at s visiting an interval [-L, R] takes minimum distance 2L + 2R - |s|. Each mismatch bit i must visit some 1 in B, requiring L >= l_i or R >= r_i where l_i, r_i are the distances to the nearest 1 of B. For a fixed s, grouping these constraints and taking suffix maximums of r_i allows computing the optimal R for each L in O(N) time.
- Common Reductions: Given two binary strings A and B of length N, we can shift A circularly left or right, and flip any bit of A if the aligned bit of B is 1. Find the minimum total number of shifts and flips to make A equal to B.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc019_d`](../../analysis/AtCoder-agc019_d.md) | D. Shift and Flip | 2601 | Given two binary strings A and B of length N, we can shift A circularly left or right, and flip any bit of A if the alig... |
