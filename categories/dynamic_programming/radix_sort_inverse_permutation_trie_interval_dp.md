# Substring DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `Substring DP`

## Description
This topic focuses on substring dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In reverse, each operation takes a subset of elements to the end maintaining relative order—identical to stable sort by a binary digit. A valid sequence of K stable sorts places element i into final order if its assigned K-bit integer X_i satisfies X_i < X_{i+1} whenever Q_i > Q_{i+1}.
- Common Reductions: Find the minimum cost to transform permutation A into P using K suffix-split-and-insert operations. Reversing the process maps directly to base-2 radix sort on the inverse permutation Q, solved via Trie-based interval DP.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc062_b`](../../analysis/AtCoder-agc062_b.md) | B. Split and Insert | 2407 | Find the minimum cost to transform permutation A into P using K suffix-split-and-insert operations. Reversing the proces... |
