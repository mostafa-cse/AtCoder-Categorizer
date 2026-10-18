# Maximum Flow / Minimum Cut

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Flow / Minimum Cut`

## Description
This topic focuses on maximum flow / minimum cut techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For player k to be the unique winner, they must attain strictly more wins than any other player. To maximize k's win count, k must win every unplayed game involving k. Each other player i can then win at most (W_k - 1) - current_wins[i] matches, which maps directly to capacity constraints in a bipartite flow network.
- Common Reductions: Determine which players can win a round-robin tournament by greedily assigning all remaining matches involving candidate player k to k, and modeling the remaining non-k matches as a Maximum Flow network with upper bounds on opponents' total wins.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc241_g`](../../analysis/AtCoder-abc241_g.md) | Round Robin | 2422 | Determine which players can win a round-robin tournament by greedily assigning all remaining matches involving candidate... |
