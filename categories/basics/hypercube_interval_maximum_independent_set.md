# Bitwise Operations and Bitmasks

**Taxonomy Path**: `Basics` > `Bitwise Thinking` > `Bitwise Operations and Bitmasks`

## Description
This topic focuses on bitwise operations and bitmasks techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The hypercube graph is bipartite partitioned by popcount parity. In an interval $[L, R]$, pairs $\{2j, 2j+1\}$ form a matching of size $(len - 2)/2$. When $L$ is odd, $R$ is even, $P(L) \neq P(R)$, and $R < L + 2^k$ (where $k = \text{MSB}(L \oplus R)$), both endpoints can be included simultaneously because no two elements differ by $2^k$.
- Common Reductions: Given $L$ and $R$, find the maximum size of an independent set in the induced subgraph of the hypercube graph formed by vertices $x \in [L, R]$, where edges connect integers differing by exactly one bit.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc213_b`](../../analysis/AtCoder-arc213_b.md) | B. Hamming Distance is not 1 | 2313 | Given $L$ and $R$, find the maximum size of an independent set in the induced subgraph of the hypercube graph formed by ... |
