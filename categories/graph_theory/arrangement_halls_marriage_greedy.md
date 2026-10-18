# Halls Theorem

**Taxonomy Path**: `Graph Theory` > `Matching` > `Halls Theorem`

## Description
This topic focuses on halls theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Consider the directed complement graph where forbidden transitions $u \to a_u$ are deleted. We need a Hamiltonian path in this graph. By Hall's Marriage Theorem / Tutte's criterion, a valid continuation exists from current vertex $u$ iff no unvisited vertex $v$ has in-degree $|V_{\text{remaining}}| - 1$ in the forbidden graph (i.e. is forbidden from all remaining vertices). Thus, we can greedily select the smallest available candidate that preserves Hall's condition.
- Common Reductions: Find the lexicographically smallest permutation $P$ of $(1, 2, \dots, N)$ such that $P_{i+1} \ne a_{P_i}$ for all $1 \le i \le N-1$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-dwacon6th_prelims_d`](../../analysis/AtCoder-dwacon6th_prelims_d.md) | D - Arrangement | 2589 | Find the lexicographically smallest permutation $P$ of $(1, 2, \dots, N)$ such that $P_{i+1} \ne a_{P_i}$ for all $1 \le... |
