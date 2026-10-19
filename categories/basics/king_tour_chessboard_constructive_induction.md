# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A King can move to any of the 8 adjacent squares. By induction on grid dimensions, we can peel off perimeter rows or columns. For example, if the target (A, B) does not lie in the first column, we can traverse column 1 completely from (1, 1) down to (H, 1), step into (H, 2), and recursively solve on the remaining H x (W - 1) grid. By symmetry (transposing when H > W or reflecting boundaries), we reduce the problem to base cases where H = 2 or H = 3, which admit direct serpentine constructions.
- Common Reductions: Construct a King's tour on an H x W chessboard that starts at (1, 1), ends at a given target square (A, B), and visits every single square exactly once.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc232_h`](../../analysis/AtCoder-abc232_h.md) | H - King's Tour | 2780 | Construct a King's tour on an H x W chessboard that starts at (1, 1), ends at a given target square (A, B), and visits e... |
