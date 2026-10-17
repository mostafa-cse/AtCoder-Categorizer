# Trie on Strings and Bits

**Taxonomy Path**: `Data Structures (DS)` > `Trie` > `Trie on Strings and Bits`

## Description
This topic focuses on trie on strings and bits techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Bitwise divide-and-conquer from MSB: if both subsets $S_0, S_1$ have even cardinality, Alice and Bob can pair elements internally without crossing bit $b$, decoupling the subproblems into $\max(\text{solve}(S_0), \text{solve}(S_1))$. If odd, Alice forces a cross, and the minimum possible outcome is $2^b + \min_{x \in S_0, y \in S_1}(x \oplus y)$.
- Common Reductions: In a game where Alice and Bob pair up $2N$ integers to minimize/maximize the maximum pair XOR, bitwise divide-and-conquer partitions elements by MSB. If both subsets are even, they decouple; if odd, a crossover pair is forced and found via binary Trie in $O(N \log (\max A))$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc122_d`](../../analysis/AtCoder-arc122_d.md) | D. XOR Game | 2331 | In a game where Alice and Bob pair up $2N$ integers to minimize/maximize the maximum pair XOR, bitwise divide-and-conque... |
