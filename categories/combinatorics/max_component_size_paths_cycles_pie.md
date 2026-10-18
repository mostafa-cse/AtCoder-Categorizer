# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Degree <= 2 implies every connected component is either an isolated vertex, a simple path, or a cycle (including double edges). By pinning the lowest-indexed remaining vertex to form a component of size s, we avoid overcounting and compute graphs with component size <= K in O(N^2 M) DP.
- Common Reductions: Count graphs on N labeled vertices and M unlabeled edges where every vertex has degree <= 2 and maximum connected component size is exactly L by subtracting the count for max component size <= L - 1 from the count for max component size <= L.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc180_f`](../../analysis/AtCoder-abc180_f.md) | Unbranched | 2419 | Count graphs on N labeled vertices and M unlabeled edges where every vertex has degree <= 2 and maximum connected compon... |
