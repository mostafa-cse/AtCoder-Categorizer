# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By symmetry, assume X, Y >= 0. In n steps of Manhattan length K, the total sum of step lengths is nK. The overshoot 2D = nK - (X + Y) must be non-negative and even. This overshoot 2D is compensated by making moves in the negative direction totaling D. For valid n, we allocate X and Y displacements into n vectors of Manhattan norm K.
- Common Reductions: Reach target coordinate (X, Y) in the minimum number of steps from (0, 0), where each step has Manhattan distance exactly K. The minimum number of steps n satisfies n * K >= |X| + |Y| and n * K = |X| + |Y| (mod 2). If K is even and |X| + |Y| is odd, it is impossible (-1). Otherwise, n steps are constructible by greedily aligning steps along the dominant axis and adjusting the overshoot via triangular adjustments.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc135_e`](../../analysis/AtCoder-abc135_e.md) | Golf | 2665 | Reach target coordinate (X, Y) in the minimum number of steps from (0, 0), where each step has Manhattan distance exactl... |
