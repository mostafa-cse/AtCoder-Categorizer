# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since any element moved to the left can be placed at the front, and any moved to the right at the back, all elements outside the chosen subsequence can be placed correctly. If value $i$ is unmoved, any preceding unmoved value $j < i$ must satisfy $pos[j] < pos[i]$. The transition $DP[i] = \min(\text{prefMinAB}[i-1], \min_{j < i, pos[j] < pos[i]} (DP[j] - \text{prefA}[j]) + \text{prefA}[i-1])$ allows point updates and range minimum queries over positions $pos$.
- Common Reductions: Find the minimum cost to sort a permutation $P$ of $1 \dots N$ by moving elements to the front (cost $B_i$ or $A_i$), back (cost $C_i$ or $A_i$), or arbitrary position (cost $A_i$). Elements that are never moved must form an increasing subsequence of values and indices $x_1 < x_2 < \dots < x_k$. Elements with values $< x_1$ can be moved to the front paying $\min(A_i, B_i)$, elements $> x_k$ can be moved to the back paying $\min(A_i, C_i)$, and interior elements not in the subsequence pay $A_i$. The optimal sequence of unmoved elements is found via DP accelerated with a Segment Tree in $O(N \log N)$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc201_f`](../../analysis/AtCoder-abc201_f.md) | F. Insertion Sort | 2484 | Find the minimum cost to sort a permutation $P$ of $1 \dots N$ by moving elements to the front (cost $B_i$ or $A_i$), ba... |
