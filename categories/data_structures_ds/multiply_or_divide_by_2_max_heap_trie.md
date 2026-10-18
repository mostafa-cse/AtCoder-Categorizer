# Trie on Strings and Bits

**Taxonomy Path**: `Data Structures (DS)` > `Trie` > `Trie on Strings and Bits`

## Description
This topic focuses on trie on strings and bits techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Viewing numbers as binary strings in a bitwise Trie, dividing by 2 pops the lowest bit, while multiplying by 2 appends a 0. The longest binary string can only match by reducing its length. Greedily reducing the maximum element is optimal and prevents branching.
- Common Reductions: Find minimum operations to transform multiset $A$ into $B$ using $x \leftarrow \lfloor x / 2 \rfloor$ and $x \leftarrow 2x$. Invert operations on $B$: multiplying an element in $A$ by 2 is equivalent to dividing an even element in $B$ by 2. Inspecting the strictly largest element $M \in A \cup B$: if $M \in A$ and $M > \max(B)$, $M$ cannot be matched without division, so $M \leftarrow \lfloor M / 2 \rfloor$. If $M \in B$ and $M > \max(A)$, $M$ must be formed by doubling, which requires $M$ to be even (if odd, impossible: output -1) and replaces $M$ with $M / 2$. A max-heap simulates this top-down reduction in $O((N + M) \log(\max A))$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc254_h`](../../analysis/AtCoder-abc254_h.md) | Ex. Multiply or Divide by 2 | 2499 | Find minimum operations to transform multiset $A$ into $B$ using $x \leftarrow \lfloor x / 2 \rfloor$ and $x \leftarrow ... |
