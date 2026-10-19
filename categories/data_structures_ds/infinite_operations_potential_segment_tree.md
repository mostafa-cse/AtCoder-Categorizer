# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let F(A) = sum_{i < j} |A_i - A_j|. Any valid operation gaining x points reduces F(A) by at least 2x, and a 'good' operation on adjacent elements in sorted order reduces F(A) by exactly 2x. Thus, the infinite limit is exactly F(A) / 2! When an element A_pos changes from old_val to new_val, the change in F(A) depends on sum_{a in A \ {old_val}} (|new_val - a| - |old_val - a|). This can be dynamically maintained using coordinate compression and a Fenwick tree (or Segment Tree) storing counts and prefix sums in O(log(N + Q)) per query.
- Common Reductions: Given sequence A of length N and Q point-update queries. For each query, let f(n) be the maximum points gained by choosing A_i <= A_j and moving them x closer while gaining x points. Find lim_{n -> inf} f(n) modulo 998244353 after each update.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc126_e`](../../analysis/AtCoder-arc126_e.md) | E - Infinite Operations | 2766 | Given sequence A of length N and Q point-update queries. For each query, let f(n) be the maximum points gained by choosi... |
