# Difference Array

**Taxonomy Path**: `Basics` > `More Techniques` > `Difference Array`

## Description
This topic focuses on difference array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Applying the operation $(-1, 2, -1)$ at position $i$ corresponds to $A_{i-1} \leftarrow A_{i-1} - 1, A_i \leftarrow A_i + 2, A_{i+1} \leftarrow A_{i+1} - 1$. In terms of operation counts $x_i$, this gives $A_i = 2x_i - x_{i-1} - x_{i+1} = -(d_{i+1} - d_i)$ where $d_i = x_i - x_{i-1}$. A valid solution exists iff $\sum A_i = 0$ and the first prefix sum of $A$ sums to $0 \pmod N$.
- Common Reductions: Given a circular array $A_1, \dots, A_N$ of sum 0, determine the minimum number of operations $(-1, +2, -1)$ at positions $(i-1, i, i+1)$ needed to reduce all elements to 0, or report impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc129_d`](../../analysis/AtCoder-arc129_d.md) | D. -1 +2 -1 | 2300 | Given a circular array $A_1, \dots, A_N$ of sum 0, determine the minimum number of operations $(-1, +2, -1)$ at position... |
