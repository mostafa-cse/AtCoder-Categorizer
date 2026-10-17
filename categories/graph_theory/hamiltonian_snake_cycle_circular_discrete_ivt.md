# Hamiltonian Path and Cycle

**Taxonomy Path**: `Graph Theory` > `Hamiltonian Path` > `Hamiltonian Path and Cycle`

## Description
This topic focuses on hamiltonian path and cycle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A standard snake Hamiltonian cycle visits columns in alternating up/down directions on rows 1..2H-1, then returns along row 0. On this cycle of length 4HW, let f(i) be the number of strawberries in the arc of length 2HW starting at cell i. Since f(i + 2HW) = 2HW - f(i) and f changes by at most 1 between adjacent starting points, by the discrete IVT there must be an index where f(i) = HW.
- Common Reductions: Partition a 2H x 2W grid containing 2HW strawberries into two connected regions A and B of size 2HW each containing exactly HW strawberries. Construct a Hamiltonian cycle on the 2H x 2W grid; any contiguous subsegment of length 2HW forms a connected path whose complement is also connected. By the discrete intermediate value theorem, a circular arc of length 2HW with exactly HW strawberries always exists.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc219_e`](../../analysis/AtCoder-arc219_e.md) | E. Equal Distribution | 2164 | Partition a 2H x 2W grid containing 2HW strawberries into two connected regions A and B of size 2HW each containing exac... |
