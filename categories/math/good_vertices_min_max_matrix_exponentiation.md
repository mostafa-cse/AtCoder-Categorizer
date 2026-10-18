# Matrix Exponentiation

**Taxonomy Path**: `Math` > `Matrices` > `Matrix Exponentiation`

## Description
This topic focuses on matrix exponentiation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The min-max algebra satisfies associativity and distributivity. Matrix binary exponentiation of the adjacency matrix $M^L$ in the $(\min, \max)$ semiring computes all pair bottleneck walks of length $L$ in $O(N^3 \log L)$ time.
- Common Reductions: In a directed graph with $N \le 100$, edges are added at times $1 \dots T$. We want to find the earliest time a walk of length exactly $L$ ($L \le 10^9$) from vertex 1 to vertex $i$ exists. This is a bottleneck shortest walk problem on the $(\min, \max)$ semiring, where matrix multiplication $(A \circ B)_{i,j} = \min_k \max(A_{i,k}, B_{k,j})$ computes the minimal edge threshold over path lengths.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc236_g`](../../analysis/AtCoder-abc236_g.md) | G. Good Vertices | 2438 | In a directed graph with $N \le 100$, edges are added at times $1 \dots T$. We want to find the earliest time a walk of ... |
