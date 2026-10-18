# Lucas Theorem

**Taxonomy Path**: `Combinatorics` > `Factorials and Binomial Coefficients (nCr)` > `Lucas Theorem`

## Description
This topic focuses on lucas theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Lucas' Theorem / Freshman's Dream in $\mathbb{F}_2[x]$, the multinomial coefficient $\binom{K}{c_1, \dots, c_N}$ is odd iff the base-2 expansions of $c_i$ partition the bits of $K$. Thus, the XOR sum reduces to $\bigoplus_{(i_b)} \sum_{b \in \text{bits}(K)} 2^b A_{i_b}$. Each bit of the sum is determined by the carry, where carry never exceeds $\max(A) \le 1000$.
- Common Reductions: Find the bitwise XOR sum of all $\sum_{i=1}^K A_{X_i}$ over all $N^K$ index sequences $X$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc156_d`](../../analysis/AtCoder-arc156_d.md) | D. Xor Sum 5 | 2568 | Find the bitwise XOR sum of all $\sum_{i=1}^K A_{X_i}$ over all $N^K$ index sequences $X$.... |
