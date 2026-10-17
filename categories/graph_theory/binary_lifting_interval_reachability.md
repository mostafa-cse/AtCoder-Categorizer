# Binary Lifting and LCA

**Taxonomy Path**: `Graph Theory` > `Lowest Common Ancestor (LCA)` > `Binary Lifting and LCA`

## Description
This topic focuses on binary lifting and lca techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because staying at a hotel further along the line strictly dominates staying closer, the optimal next hotel from hotel i is the maximum j such that x[j] - x[i] <= L (when moving right) or minimum j such that x[i] - x[j] <= L (when moving left). Binary lifting precomputes the hotel reached after 2^k daily maximal jumps.
- Common Reductions: Given N sorted hotels on a line and maximum daily travel distance L, answer Q queries finding the minimum number of days to travel between hotel a and hotel b. Monotonicity implies each step greedily jumps to the farthest reachable hotel, modeled as binary lifting on functional graphs.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-arc060_c]` | Tak and Hotels | 2154 | Given N sorted hotels on a line and maximum daily travel distance L, answer Q queries finding the minimum number of days... |
