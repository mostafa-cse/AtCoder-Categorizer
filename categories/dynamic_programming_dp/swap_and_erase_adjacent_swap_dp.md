# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Erasing prefix runs of identical elements can be deferred until after all swaps are complete. In any optimal solution, each element is swapped at most once, meaning all swap indices satisfy $|p_i - p_j| \ge 2$. Thus, the array $0 \dots N-1$ is partitioned into disjoint singles (unswapped elements $A_i$) and pairs (swapped elements $(A_{i+1}, A_i)$). The total cost is $1 + (\text{number of swaps}) + (\text{number of adjacent mismatches } B_i \ne B_{i+1})$, which can be minimized via linear DP.
- Common Reductions: Find the minimum number of adjacent swap operations and prefix run-erase operations to make an array $A$ empty.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc195_d`](../../analysis/AtCoder-arc195_d.md) | D - Swap and Erase | 2470 | Find the minimum number of adjacent swap operations and prefix run-erase operations to make an array $A$ empty.... |
