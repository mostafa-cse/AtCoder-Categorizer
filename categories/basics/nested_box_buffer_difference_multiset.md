# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Using all active boxes to package K donuts partitions the boxes into K nesting chains, where buffer material is sum (C_{outer} - C_{inner}). This is mathematically equivalent to partitioning the sorted active boxes into K intervals, minimizing span minus the sum of the K-1 largest adjacent differences.
- Common Reductions: Pack K donuts into N nested boxes, minimizing total buffer material C_i - C_j across Q box crush events. Nesting into K chains equates to partitioning sorted active boxes into K intervals, minimizing span minus the sum of the K-1 largest adjacent differences. Maintaining differences with two multisets answers each query in O(log N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-donuts_2015_4`](../../analysis/AtCoder-donuts_2015_4.md) | D. ドーナツの箱詰め | 2383 | Pack K donuts into N nested boxes, minimizing total buffer material C_i - C_j across Q box crush events. Nesting into K ... |
