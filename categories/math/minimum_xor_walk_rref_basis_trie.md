# [Technique] XOR Basis ft Reduced Row Echelon Form

**Taxonomy Path**: `Math` > `Linear Algebra` > `[Technique] XOR Basis ft Reduced Row Echelon Form`

## Description
This topic focuses on [technique] xor basis ft reduced row echelon form techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any walk XOR between x and y equals (D[x] ^ D[y]) ^ c where D[v] is spanning tree path XOR and c is in the linear span of fundamental cycles. Putting the cycle XOR basis into Reduced Row Echelon Form (RREF) allows projecting each D[v] into a canonical representative D~[v] where all pivot bits are cleared. The minimum walk XOR between x and y is identically D~[x] ^ D~[y], allowing pair counting via a 0-1 Trie.
- Common Reductions: Given connected undirected graph with edge weights W_i < 2^30, count pairs of vertices (x, y) (x < y) whose minimum XOR walk weight is <= K.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc451_g`](../../analysis/AtCoder-abc451_g.md) | Minimum XOR Walk | 2221 | Given connected undirected graph with edge weights W_i < 2^30, count pairs of vertices (x, y) (x < y) whose minimum XOR ... |
