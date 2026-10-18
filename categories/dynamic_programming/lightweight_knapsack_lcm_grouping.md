# Knapsack and Subset Sum Optimizations

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Subset Sum Optimizations`

## Description
This topic focuses on knapsack and subset sum optimizations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Items of each weight $w \in \{1, 2, 3\}$ are always selected in descending order of value. Because $\text{lcm}(1, 2, 3) = 6$, all remaining items of weight $w$ can be grouped into super-items of weight 6, leaving remainders $R_w = F_w \bmod (6/w)$ which take only $6 \times 3 \times 2 = 36$ total states.
- Common Reductions: Bounded knapsack with small weights $W_i \in \{1, 2, 3\}$ and capacity $C \le 2 \times 10^9$. Since $\text{lcm}(1, 2, 3) = 6$, all items are grouped into weight-6 super-items, leaving only 36 remainder combinations solved greedily in $O(N \log N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc442_g`](../../analysis/AtCoder-abc442_g.md) | G. Lightweight Knapsack | 2347 | Bounded knapsack with small weights $W_i \in \{1, 2, 3\}$ and capacity $C \le 2 \times 10^9$. Since $\text{lcm}(1, 2, 3)... |
