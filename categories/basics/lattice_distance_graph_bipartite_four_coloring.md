# Pigeonhole Principle

**Taxonomy Path**: `Basics` > `Basic Counting` > `Pigeonhole Principle`

## Description
This topic focuses on pigeonhole principle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any distance sqrt(D) graph on the integer lattice Z^2 is bipartite! Factoring D = 4^k D' where D' not equiv 0 mod 4: if D' equiv 1, 3 mod 4, a 2-coloring is ((x >> k) + (y >> k)) mod 2; if D' equiv 2 mod 4, a 2-coloring is (x >> k) mod 2. Combining the 2-colorings for D_1 and D_2 produces a 4-coloring of the 4N^2 points. By the Pigeonhole Principle, at least one color class contains >= N^2 points, and every color class is an independent set in both graphs.
- Common Reductions: Given N and constants D_1, D_2, choose N^2 points from the 2N x 2N grid of lattice points [0, 2N-1]^2 such that no two chosen points have Euclidean distance sqrt(D_1) or sqrt(D_2).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc025_d`](../../analysis/AtCoder-agc025_d.md) | D - Choosing Points | 2868 | Given N and constants D_1, D_2, choose N^2 points from the 2N x 2N grid of lattice points [0, 2N-1]^2 such that no two c... |
