# Bitwise Operations and Bitmasks

**Taxonomy Path**: `Basics` > `Bitwise Thinking` > `Bitwise Operations and Bitmasks`

## Description
This topic focuses on bitwise operations and bitmasks techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Assigning potential $P_v = x \oplus dist^1_\oplus(1, v)$ preserves edge weights under vertex potential swaps. The multiset of potentials must match $\{y \oplus dist^2_\oplus(1, v)\}$. Summing potentials under XOR when $N$ is odd reveals $z = x \oplus y = (\bigoplus dist^1_v) \oplus (\bigoplus dist^2_v)$, eliminating all degrees of freedom.
- Common Reductions: Determine whether initial edge weights $w^1_i$ on a tree with $N$ vertices ($N$ odd) can be transformed to target weights $w^2_i$ by XORing incident edges of an edge $(u, v)$ with its weight $w$. Represent edge weights as differences of vertex potentials $w(u, v) = P_u \oplus P_v$. An operation on edge $(u, v)$ is identical to swapping potentials $P_u$ and $P_v$. Because the tree is connected, potentials can be permuted arbitrarily. Since $N$ is odd, the root potential shift $z$ is uniquely determined.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc052_b`](../../analysis/AtCoder-agc052_b.md) | B. Tree Edges XOR | 2473 | Determine whether initial edge weights $w^1_i$ on a tree with $N$ vertices ($N$ odd) can be transformed to target weight... |
