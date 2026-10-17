# Topological Sorting

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Topological Sorting`

## Description
This topic focuses on topological sorting techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Pairwise analysis shows that for disjoint intervals, cost is 0; for overlapping non-contained intervals, cost is 1 in both orders. Only when [L_j, R_j] is strictly contained in [L_i, R_i] does order matter: P_j < P_i incurs cost 0, whereas P_i < P_j incurs cost 2. Containment defines a DAG poset where j -> i whenever interval j is contained in interval i. To find the lexicographically smallest permutation P, assign the largest seat numbers N, N-1, ..., 1 backwards to the unassigned node with the largest index having no containing unassigned ancestor.
- Common Reductions: Find the lexicographically smallest seat permutation P minimizing the total dissatisfaction when people with staying intervals [L_i, R_i] cross seats to enter and exit.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc200_c`](../../analysis/AtCoder-arc200_c.md) | Movie Theater | 2237 | Find the lexicographically smallest seat permutation P minimizing the total dissatisfaction when people with staying int... |
