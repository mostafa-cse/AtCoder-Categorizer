# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Under A_i <- A_i - i, the target sequence B must be non-decreasing. An operation at i increases the index-weighted sum sum_{j=0}^{N-1} j * A_j by exactly 1 while keeping sum A_j invariant. Within each leveled block of size len and sum s, elements are B_j = floor((s + j) / len). Monotonically merge adjacent blocks whenever left_max > right_min.
- Common Reductions: Minimum operations (A_i - 1, A_{i+1} + 1) to make A strictly increasing. Transformed to non-decreasing via A_i <- A_i - i. Solved via monotonic block merging in O(N).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc459_f]` | -1, +1 | 2163 | Minimum operations (A_i - 1, A_{i+1} + 1) to make A strictly increasing. Transformed to non-decreasing via A_i <- A_i - ... |
