# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Adding a permutation adds $N(N+1)/2$ to the total sum. A uniform state is achievable if and only if $\sum A_i \equiv 0 \pmod N$ for odd $N$, or $\sum A_i \in \{0, N/2\} \pmod N$ for even $N$.
- Common Reductions: Given array $A$ of length $N \le 50$, repeatedly add permutations of $(1, \dots, N)$ in at most $10^4$ operations to equalize all elements, or determine impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc159_c`](../../analysis/AtCoder-arc159_c.md) | C. Permutation Addition | 2304 | Given array $A$ of length $N \le 50$, repeatedly add permutations of $(1, \dots, N)$ in at most $10^4$ operations to equ... |
