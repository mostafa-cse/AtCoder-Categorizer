# Suffix Array

**Taxonomy Path**: `Strings` > `Suffix Structures` > `Suffix Array`

## Description
This topic focuses on suffix array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Every cyclic shift of S is a length-N prefix of a suffix of S + S starting at index i in [0, N-1], and similarly for T. Construct concatenated string X = S + S + 0^N + T + T + 200^N + sentinel where delimiters guarantee that identical length-N prefixes are broken with S strictly before T. In the suffix array of X, shift i of S is <= shift j of T iff suffix i precedes suffix (3N + j) in the suffix array. A single linear sweep over the suffix array counts valid pairs.
- Common Reductions: Count pairs (i, j) of cyclic shifts of strings S and T of length N <= 2 * 10^5 such that shift i of S is lexicographically <= shift j of T.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc272_f`](../../analysis/AtCoder-abc272_f.md) | Two Strings | 2238 | Count pairs (i, j) of cyclic shifts of strings S and T of length N <= 2 * 10^5 such that shift i of S is lexicographical... |
