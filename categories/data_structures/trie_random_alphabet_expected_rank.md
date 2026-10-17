# Trie on Strings and Bits

**Taxonomy Path**: `Data Structures (DS)` > `Trie` > `Trie on Strings and Bits`

## Description
This topic focuses on trie on strings and bits techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Under a uniformly random alphabet permutation, any string $S_j$ that is a proper prefix of $S_i$ precedes $S_i$ with probability 1, any string of which $S_i$ is a proper prefix precedes $S_i$ with probability 0, and any string branching at a distinct character precedes $S_i$ with probability 1/2 by character symmetry.
- Common Reductions: Given $N$ strings $S_1, \dots, S_N$, a random permutation of the 26 lowercase English letters is chosen uniformly. For each string $S_i$, find the expected value of its 1-based index when all $N$ strings are sorted lexicographically, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc268_g`](../../analysis/AtCoder-abc268_g.md) | G. Random Student ID | 2311 | Given $N$ strings $S_1, \dots, S_N$, a random permutation of the 26 lowercase English letters is chosen uniformly. For e... |
