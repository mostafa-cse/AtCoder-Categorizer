# Divide and Conquer

**Taxonomy Path**: `Basics` > `Divide and Conquer` > `Divide and Conquer`

## Description
This topic focuses on divide and conquer techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Using median Divide and Conquer on $x$-coordinates: for a point set $S$, let $x_{mid}$ be the median $x$-coordinate. For every point $(x, y) \in S$, we add the projection $(x_{mid}, y)$. This connects all points in $S$ to the vertical line $x = x_{mid}$ via a single horizontal edge. Points on opposite sides of $x_{mid}$ can travel monotonically $(x, y) \to (x_{mid}, y) \to (x_{mid}, y') \to (x', y')$, with total length $|x - x'| + |y - y'|$. Recursively applying this to the left and right halves achieves pairwise Manhattan connectivity in depth $\lceil \log_2 N \rceil \le 10$, adding at most $N \log_2 N \le 10,000$ points.
- Common Reductions: Add at most $10000 - N$ bus stops at lattice intersections so that the shortest grid route between any two bus stops equals their Manhattan distance.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc024_4`](../../analysis/AtCoder-arc024_4.md) | D - バス停 | 2496 | Add at most $10000 - N$ bus stops at lattice intersections so that the shortest grid route between any two bus stops equ... |
