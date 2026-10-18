# Divide and Conquer

**Taxonomy Path**: `Basics` > `Divide and Conquer` > `Divide and Conquer`

## Description
This topic focuses on divide and conquer techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: This can be solved by divide-and-conquer on 3 stacks in O(N log N) moves. To sort a range of disks [L, R] currently on peg src onto peg dest (with largest at bottom): partition the disks around midpoint mid = (L + R) / 2 by popping them from src and routing disks <= mid to aux_small and disks > mid to aux_large. Then recursively sort the larger disks [mid + 1, R] from aux_large onto dest (they land at the bottom of dest). Finally, recursively sort the smaller disks [L, mid] from aux_small onto dest (they land on top of the larger disks). The total moves satisfy T(N) = 2 T(N/2) + N, which for N = 10,000 requires only ~139,000 moves, well below the 225,000 limit.
- Common Reductions: Given 3 pegs and N disks (N <= 10,000) stacked on peg 1 in arbitrary order, move disks one at a time between pegs (any disk can be placed on top of any other) to sort all disks on any peg with largest at the bottom and smallest at the top, using at most 225,000 moves.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-code_formula_2014_final_g`](../../analysis/AtCoder-code_formula_2014_final_g.md) | G. ノイハの塔 (Tower of Neuha) | 2588 | Given 3 pegs and N disks (N <= 10,000) stacked on peg 1 in arbitrary order, move disks one at a time between pegs (any d... |
