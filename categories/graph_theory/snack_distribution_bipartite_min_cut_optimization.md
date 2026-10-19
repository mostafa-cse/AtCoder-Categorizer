# Maximum Flow / Minimum Cut

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Flow / Minimum Cut`

## Description
This topic focuses on maximum flow / minimum cut techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By max-flow min-cut duality, the min-cut capacity when selecting the k largest snack capacities in S is sum_{i=1}^{N-k} A_{(i)} + sum_{j=1}^M min(C_j, k B_j). For each child j, the threshold where k B_j exceeds C_j is t_j = floor(C_j / B_j). Sorting snacks A and grouping children by threshold t_j allows evaluating all cuts k in [0, N] via a single linear sweep in O(N log N + M log M) time.
- Common Reductions: Distribute N kinds of snacks (kind i has A_i pieces) to M children, where child j can receive at most B_j pieces of any single snack and at most C_j pieces in total. Find the maximum total pieces distributed.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc125_e`](../../analysis/AtCoder-arc125_e.md) | E - Snack | 2874 | Distribute N kinds of snacks (kind i has A_i pieces) to M children, where child j can receive at most B_j pieces of any ... |
