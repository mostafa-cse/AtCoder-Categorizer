# Tournament Graph

**Taxonomy Path**: `Graph Theory` > `Special Graphs` > `Tournament Graph`

## Description
This topic focuses on tournament graph techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any tournament, the condensation is a linear order $C_1 \to \dots \to C_k$. The number of SCCs is $1 + \sum_{A \subset V, A \ne \emptyset, A \ne V} [\text{all edges } A \to V \setminus A]$. The cross-edge forward count is the number of inversions $\text{inv}(A, V \setminus A)$, while internal edges can be chosen freely.
- Common Reductions: Find the total number of SCCs across all tournaments on $N$ vertices with exactly $M$ forward edges.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc163_d`](../../analysis/AtCoder-arc163_d.md) | D. Sum of SCC | 2581 | Find the total number of SCCs across all tournaments on $N$ vertices with exactly $M$ forward edges.... |
