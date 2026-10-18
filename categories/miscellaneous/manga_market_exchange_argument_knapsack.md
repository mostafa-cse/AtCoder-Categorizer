# Exchange Arguments

**Taxonomy Path**: `Miscellaneous` > `Greedy Algorithms` > `Exchange Arguments`

## Description
This topic focuses on exchange arguments techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Stores with $a_i = 0$ add a constant cost $b_i + 1$ independent of arrival time. They should be visited greedily in increasing order of $b_i + 1$. For stores with $a_i \ge 1$, sort by $(b_i + 1) / a_i$ and run Knapsack DP: $DP[k]$ is the minimum time to visit $k$ stores ($0 \le k \le 30$). The remaining time $T - DP[k]$ greedily accommodates $a_i = 0$ stores via binary search.
- Common Reductions: There are $N$ stores. Visiting store $i$ with arrival time $t$ has departure time $(a_i + 1)t + (b_i + 1)$. For stores with $a_i \ge 1$, visiting store $i$ then $j$ is better than $j$ then $i$ when $(b_i + 1) a_j < (b_j + 1) a_i$ by exchange argument. Furthermore, because $(a_i + 1) \ge 2$, time doubles at each step, so at most $\log_2(T) \le 30$ stores with $a_i \ge 1$ can be visited before time $T$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-hitachi2020_d`](../../analysis/AtCoder-hitachi2020_d.md) | D. Manga Market | 2547 | There are $N$ stores. Visiting store $i$ with arrival time $t$ has departure time $(a_i + 1)t + (b_i + 1)$. For stores w... |
