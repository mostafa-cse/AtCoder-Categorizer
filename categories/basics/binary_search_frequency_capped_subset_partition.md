# Binary Search

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Binary Search`

## Description
This topic focuses on binary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: $X$ operations choosing $K$ distinct elements are feasible if and only if the total capped count $\sum_i \min(c_i, X) \ge K \cdot X$. Inverting this relationship allows determining the maximum $X$ for each $K$ via binary search or suffix-maximum sweep over $K \le \lfloor S(X) / X \rfloor$.
- Common Reductions: Given $N$ integers, for each $K = 1, \dots, N$, find the maximum number of operations possible where each operation chooses $K$ pairwise distinct integers and removes them.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc143_f`](../../analysis/AtCoder-abc143_f.md) | F. Distinct Numbers | 2277 | Given $N$ integers, for each $K = 1, \dots, N$, find the maximum number of operations possible where each operation choo... |
