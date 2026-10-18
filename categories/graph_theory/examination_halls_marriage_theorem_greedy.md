# Halls Theorem

**Taxonomy Path**: `Graph Theory` > `Matching` > `Halls Theorem`

## Description
This topic focuses on halls theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sweep values from largest to smallest. Maintain suffix balance of scores. Helper students $j$ with $A_j \ge B_j$ become available when the sweep passes $A_j$; push their $B_j$ into a min-priority queue. Whenever the suffix balance falls below 0, pop the smallest $B_j$ from the queue to fix the deficit as far into the future as possible. If the queue is empty while balance $< 0$, no solution exists (output -1).
- Common Reductions: Students have score $A_i$ and need $B_i$. Swapping scores between students can make everyone graduate ($A'_i \ge B_i$) iff for all $x$, $\text{count}(A \ge x) \ge \text{count}(B \ge x)$ by Hall's Marriage Theorem. Students with $A_i < B_i$ are mandatory swaps. For students with $A_i \ge B_i$, we want to keep as many unchanged as possible. Each helper student $j$ added to the swap pool covers the deficit on interval $[B_j, A_j - 1]$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc147_e`](../../analysis/AtCoder-arc147_e.md) | E. Examination | 2553 | Students have score $A_i$ and need $B_i$. Swapping scores between students can make everyone graduate ($A'_i \ge B_i$) i... |
