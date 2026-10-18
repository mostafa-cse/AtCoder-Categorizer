# Exchange Arguments

**Taxonomy Path**: `Miscellaneous` > `Greedy Algorithms` > `Exchange Arguments`

## Description
This topic focuses on exchange arguments techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By exchange arguments, if the robot makes K trips to the dump, it should pick up approximately ceil(N/K) pieces per trip. In each trip, pieces are collected on the way back. The furthest piece and 2nd furthest piece have energy multiplier 5; the b-th furthest piece (b >= 3) has multiplier 2b + 1. Sorting pieces and partitioning them into blocks of size K allows evaluating the cost of any K in O(N / K) time using prefix sums.
- Common Reductions: A robot collects N pieces of garbage at positions x_1 < x_2 < ... < x_N. Carrying k pieces consumes (k+1)^2 energy per unit distance, plus cost X per pickup/dropoff. Find the minimum total energy.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc027_b`](../../analysis/AtCoder-agc027_b.md) | B - Garbage Collector | 2631 | A robot collects N pieces of garbage at positions x_1 < x_2 < ... < x_N. Carrying k pieces consumes (k+1)^2 energy per u... |
