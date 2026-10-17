# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each occurrence generates an independent rectangle of valid (L, R) coordinates. The union of these rectangles covers all valid pairs. Sweeping L from 1 to N, we activate and deactivate intervals [R1, R2] on a segment tree tracking min coverage and zero-count. The number of covered R values at each step L is N - (zero_count if min == 0 else 0).
- Common Reductions: Find the number of pairs (L, R) such that at least one value appears uniquely in A[L..R]. For each occurrence p_k of value x, it is unique in A[L..R] iff p_{k-1} < L <= p_k and p_k <= R < p_{k+1}. The problem reduces to finding the area of the union of axis-aligned rectangles [p_{k-1}+1, p_k] x [p_k, p_{k+1}-1] via sweep-line and segment tree.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc346_g`](../../analysis/AtCoder-abc346_g.md) | G. Alone | 2166 | Find the number of pairs (L, R) such that at least one value appears uniquely in A[L..R]. For each occurrence p_k of val... |
