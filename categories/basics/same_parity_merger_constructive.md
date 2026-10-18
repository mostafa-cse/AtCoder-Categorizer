# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Choosing an internal element replaces it with the sum of its neighbors and deletes both neighbors, preserving the index parity of all remaining elements. Thus, any final single element is a sum of a non-empty subset of elements with identical original index parity (all odd or all even). The maximum sum is achieved by taking all positive elements of the superior parity (or the single maximum element if all are negative).
- Common Reductions: Array merging via neighbor replacement preserves relative index parity. Any achievable value is a non-empty sum of same-parity elements; greedy parity selection and $O(N)$ constructive trimming and collapsing deterministically yields the maximum sum.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc092_c`](../../analysis/AtCoder-arc092_c.md) | E. Both Sides Merger | 2361 | Array merging via neighbor replacement preserves relative index parity. Any achievable value is a non-empty sum of same-... |
