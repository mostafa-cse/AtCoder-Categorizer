# Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)

**Taxonomy Path**: `Graph Theory` > `Matching` > `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`

## Description
This topic focuses on bipartite matching (hopcroft karp algorithm and kuhn's algorithm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Except for $1 + 1 = 2$, every prime sum must be odd, which requires pairing one odd integer and one even integer. The conflict graph between odd and even integers is bipartite. If $k$ pairs of $(1, 1)$ are reserved, $2k$ ones are removed, and the remaining ones participate in the bipartite matching with the even numbers. The total operations $f(k) + k$ is concave in $k$, allowing ternary search over $k \in [0, \lfloor B_1 / 2 \rfloor]$.
- Common Reductions: Given $N$ distinct values $A_i$ with frequencies $B_i$. In each operation, choose two numbers summing to a prime and erase them. Find the maximum number of operations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc263_g`](../../analysis/AtCoder-abc263_g.md) | G. Erasing Prime Pairs | 2261 | Given $N$ distinct values $A_i$ with frequencies $B_i$. In each operation, choose two numbers summing to a prime and era... |
