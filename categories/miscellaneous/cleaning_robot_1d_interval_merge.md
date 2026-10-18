# Coordinate Compression

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Coordinate Compression`

## Description
This topic focuses on coordinate compression techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Trace 1 cycle to find visited set $P$ and net vector $(\Delta x, \Delta y)$. If $(\Delta x, \Delta y) = (0, 0)$, answer is $|P|$. Otherwise, the trajectory decomposes into parallel 1D lines parameterized by canonical remainder $(r, base_y)$ with $x = q \Delta x + r$. Each point $(x, y) \in P$ generates an interval $[q, q + K - 1]$ along its line. Merging 1D intervals per line computes the exact union.
- Common Reductions: Count distinct grid squares visited by a robot executing move sequence $S$ of length $N$ repeated $K$ times.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc219_f`](../../analysis/AtCoder-abc219_f.md) | F. Cleaning Robot | 2542 | Count distinct grid squares visited by a robot executing move sequence $S$ of length $N$ repeated $K$ times.... |
