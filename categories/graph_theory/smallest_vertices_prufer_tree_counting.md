# Prufer Code

**Taxonomy Path**: `Graph Theory` > `Graph Counting` > `Prufer Code`

## Description
This topic focuses on prufer code techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Vertex $v$ satisfies $f(v) = v$ iff all vertices in its subtree belong to $\{v, v+1, \dots, N\}$. By Cayley's multinomial formula via Prüfer sequences, the number of trees where $\{v\} \cup S$ forms $v$'s subtree depends only on $|S| = m$ and $\sum_{u \in S} d_u = m - d_v$, with contribution $\frac{(m - 1)! (N - m - 2)!}{(d_1 - 1)! \prod_{i=2}^N d_i!} d_v$.
- Common Reductions: Count the total number of good vertices ($f(v) = v$) across all directed rooted trees with vertex 1 as root and specified out-degrees $(d_1, \dots, d_N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc162_d`](../../analysis/AtCoder-arc162_d.md) | D. Smallest Vertices | 2568 | Count the total number of good vertices ($f(v) = v$) across all directed rooted trees with vertex 1 as root and specifie... |
