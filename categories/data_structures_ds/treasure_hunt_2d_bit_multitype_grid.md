# 2D BIT

**Taxonomy Path**: `Data Structures (DS)` > `Binary Indexed Tree (BIT)` > `2D BIT`

## Description
This topic focuses on 2d bit techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: With $K \le 100$ and $N, M \le 500$, we maintain a separate 2D Binary Indexed Tree (Fenwick Tree) for each of the $K$ types. Total memory is $100 \times 500 \times 500 \times 4 \text{ bytes} \approx 100 \text{ MB}$, well within limits. Type 1 swaps two cells, updating 4 points across the 2D BITs in $O(\log N \log M)$ time. Type 2 queries a sub-rectangle $[r_1, r_2] \times [c_1, c_2]$: querying each of the $K$ 2D BITs takes $O(K \log N \log M)$ time to find the maximum frequency and tiebreak by largest type.
- Common Reductions: Process cell swaps and sub-rectangle majority type queries on an $N \times M$ grid with cell types $1 \dots K$ ($N, M \le 500, K \le 100$).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-code_festival_morning_hard_c`](../../analysis/AtCoder-code_festival_morning_hard_c.md) | C - 宝探し 2 | 2521 | Process cell swaps and sub-rectangle majority type queries on an $N \times M$ grid with cell types $1 \dots K$ ($N, M \l... |
