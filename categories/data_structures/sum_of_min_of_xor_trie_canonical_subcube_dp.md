# Trie on Strings and Bits

**Taxonomy Path**: `Data Structures (DS)` > `Trie` > `Trie on Strings and Bits`

## Description
This topic focuses on trie on strings and bits techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any subtree u at bit level b, the sum of min_{y in u} (z ^ y) as z ranges freely over all 2^b values is purely a structural property of subtree u: F(u, b) = F(L, b-1) + F(R, b-1) if both exist, or 2*F(child, b-1) + 2^(2b-2) if only one child exists.
- Common Reductions: Binary Trie DP precalculating subtree minimum XOR sums over complete subcubes combined with canonical prefix decomposition of [0, M-1].

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc425_g`](../../analysis/AtCoder-abc425_g.md) | Sum of Min of XOR | 2205 | Binary Trie DP precalculating subtree minimum XOR sums over complete subcubes combined with canonical prefix decompositi... |
| [`AtCoder-arc127_d`](../../analysis/AtCoder-arc127_d.md) | D. Sum of Min of Xor | 2593 | Compute $\sum_{1 \le i < j \le N} \min(A_i \oplus A_j, B_i \oplus B_j)$ for sequences $A$ and $B$ with values $< 2^{18}$... |
