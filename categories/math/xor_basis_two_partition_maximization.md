# Vector Space and XOR Basis

**Taxonomy Path**: `Math` > `Linear Algebra` > `Vector Space and XOR Basis`

## Description
This topic focuses on vector space and xor basis techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let $S = \bigoplus A_i$ be the total XOR sum. In any partition $(X, Y)$, $X \oplus Y = S$. For bits where $S$ has 1, exactly one of $X$ and $Y$ has 1, contributing $2^b$ to $X + Y$ regardless of partition. For bits where $S$ has 0, $X$ and $Y$ have the same bit value; if that bit is 1 in $X$, both contribute $2^b$, adding $2^{b+1}$ to $X + Y$. Thus, maximizing $X + Y$ is equivalent to maximizing the subset XOR sum on masked elements $A_i \ \& \ (\sim S)$.
- Common Reductions: Maximize the sum of two disjoint subset XOR sums. Bits with odd total counts contribute $2^b$ regardless; bits with even total counts can both be made 1 by finding the maximum subset XOR sum on masked elements via Gaussian elimination in $O(N \log (\max A))$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc141_f`](../../analysis/AtCoder-abc141_f.md) | F. Xor Sum 3 | 2342 | Maximize the sum of two disjoint subset XOR sums. Bits with odd total counts contribute $2^b$ regardless; bits with even... |
