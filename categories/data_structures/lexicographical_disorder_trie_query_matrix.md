# Trie on Strings and Bits

**Taxonomy Path**: `Data Structures (DS)` > `Trie` > `Trie on Strings and Bits`

## Description
This topic focuses on trie on strings and bits techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the Trie of all strings, any string $S_j$ smaller than $S_k$ either ends at an ancestor of $S_k$ (constant prefix contribution), or branches off at a node $u$ with character $c'$ where $S_k$ has $c$ and $\text{rank}(c') < \text{rank}(c)$. Summing sibling branch sizes across $S_k$'s path produces a $26 \times 26$ divergence matrix $W_k$.
- Common Reductions: Answer $Q$ queries finding the 1-based lexicographical rank of string $S_k$ under custom alphabet permutations $p$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-codefestival_2016_qualB_e`](../../analysis/AtCoder-codefestival_2016_qualB_e.md) | E. Lexicographical disorder | 2576 | Answer $Q$ queries finding the 1-based lexicographical rank of string $S_k$ under custom alphabet permutations $p$.... |
