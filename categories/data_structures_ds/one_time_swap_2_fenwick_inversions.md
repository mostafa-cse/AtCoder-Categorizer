# BIT / Fenwick Tree

**Taxonomy Path**: `Data Structures (DS)` > `Binary Indexed Tree (BIT)` > `BIT / Fenwick Tree`

## Description
This topic focuses on bit / fenwick tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Comparing $f(l, r)$ to $A$: $f(l, r) < A$ if $A_l > A_r$, $f(l, r) = A$ if $A_l = A_r$, and $f(l, r) > A$ if $A_l < A_r$. For pairs with $A_l > A_r$, the lexicographical order corresponds to sorting by $(l, A_r, -r)$. By sorting queries offline, we iterate $l$ from $0$ to $N-1$ and maintain elements in a Fenwick Tree with binary lifting to identify $(A_r, r)$ in $O(\log N)$ per query. A symmetric pass handles $f(l, r) > A$.
- Common Reductions: Find the pair $(l, r)$ whose one-time swap produces the $k$-th lexicographically smallest permutation in the multiset of all $\binom{N}{2}$ swapped arrays.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc431_g`](../../analysis/AtCoder-abc431_g.md) | G - One Time Swap 2 | 2490 | Find the pair $(l, r)$ whose one-time swap produces the $k$-th lexicographically smallest permutation in the multiset of... |
