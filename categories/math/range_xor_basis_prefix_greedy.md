# Vector Space and XOR Basis

**Taxonomy Path**: `Math` > `Linear Algebra` > `Vector Space and XOR Basis`

## Description
This topic focuses on vector space and xor basis techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A linear basis over GF(2) with greedy index tracking can answer range subset XOR queries without segment trees. In the prefix XOR basis for prefix R, each basis vector basis[b] retains the latest position pos[b] among the elements that contributed to that basis vector. When inserting (A[i], i), if bit b is set and basis[b] already exists, we greedily keep the element with the larger index as basis[b] and continue inserting the swapped out element. To query (L, R, X), we only reduce X with basis vectors in prefix R whose pos[b] >= L. If X reduces to 0, it lies in the span of A[L..R].
- Common Reductions: Given an array A of N positive integers and Q queries (L, R, X), determine whether X can be formed as the XOR sum of some subsequence of A[L..R].

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc223_h`](../../analysis/AtCoder-abc223_h.md) | H - Xor Query | 2771 | Given an array A of N positive integers and Q queries (L, R, X), determine whether X can be formed as the XOR sum of som... |
