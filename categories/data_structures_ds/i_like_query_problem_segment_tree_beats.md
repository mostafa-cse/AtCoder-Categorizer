# Segment Tree Beats

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree Beats`

## Description
This topic focuses on segment tree beats techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Floor division is not a linear operation, but when $\lfloor \max / x \rfloor == \lfloor \min / x \rfloor$, the entire range $[L, R]$ collapses to a single value, transforming the operation into a simple range assignment! Segment Tree Beats tracks range minimum, range maximum, and range sum. When $\lfloor \max / x \rfloor == \lfloor \min / x \rfloor$, we apply range assignment tag $\lfloor \max / x \rfloor$. Otherwise, we recurse into children. Since each division by $x \ge 2$ strictly reduces the bit-length of $\max - \min$, the amortized complexity is $O((N + Q) \log N \log(\max A))$.
- Common Reductions: Maintain an array $A$ of size $N$ supporting three operations:
1. Range floor division: $A_i \leftarrow \lfloor A_i / x \rfloor$ for $i \in [L, R]$.
2. Range assignment: $A_i \leftarrow y$ for $i \in [L, R]$.
3. Range sum query: $\sum_{i=L}^R A_i$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc256_h`](../../analysis/AtCoder-abc256_h.md) | Ex. I like Query Problem | 2531 | Maintain an array $A$ of size $N$ supporting three operations:
1. Range floor division: $A_i \leftarrow \lfloor A_i / x ... |
