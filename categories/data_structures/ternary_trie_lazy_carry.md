# Trie on Strings and Bits

**Taxonomy Path**: `Data Structures (DS)` > `Trie` > `Trie on Strings and Bits`

## Description
This topic focuses on trie on strings and bits techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Represent the 3^N positions in a ternary trie of depth N. Operation 'R' swaps children 1 and 2 at every trie node, maintained by a lazy flip tag in O(1). Operation 'S' adds 1 in ternary: child 0 becomes 1, child 1 becomes 2, child 2 becomes 0 with carry propagating down child 2 in amortized O(N) time. After processing all operations, push down tags via DFS to recover each person's final position.
- Common Reductions: 3^N people arranged in a circle labeled 0 to 3^N - 1 in base 3 dance according to operations 'S' (shift x -> x + 1 mod 3^N) and 'R' (reverse positions). Find final positions of all people.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc044_c`](../../analysis/AtCoder-agc044_c.md) | C. Strange Dance | 2889 | 3^N people arranged in a circle labeled 0 to 3^N - 1 in base 3 dance according to operations 'S' (shift x -> x + 1 mod 3... |
