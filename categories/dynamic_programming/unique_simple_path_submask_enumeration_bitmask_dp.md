# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Minimizing destroyed edges is equivalent to maximizing the sum of costs of kept edges. The condition of a unique simple path between 1 and N implies that the kept subgraph consists of a simple path v_1, v_2, ..., v_k (v_1=1, v_k=N), where each vertex v_i is attached to a connected component C_i of vertices disjoint from all other components, and NO edges exist between C_i and C_j (i != j) except the path edges (v_i, v_{i+1}). Within each component C_i, ALL internal edges may be kept.
- Common Reductions: In a connected undirected weighted graph with N <= 15 vertices, find the minimum total cost of edges to destroy such that there exists exactly one simple path between vertex 1 and vertex N.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc078_d`](../../analysis/AtCoder-arc078_d.md) | F - Mole and Abandoned Mine | 2956 | In a connected undirected weighted graph with N <= 15 vertices, find the minimum total cost of edges to destroy such tha... |
