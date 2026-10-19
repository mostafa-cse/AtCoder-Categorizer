# Permutations and Permutation Cycles

**Taxonomy Path**: `Miscellaneous` > `Permutations` > `Permutations and Permutation Cycles`

## Description
This topic focuses on permutations and permutation cycles techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Append A_{N+1} = xor_sum(A) and B_{N+1} = xor_sum(B). Replacing A_i with the XOR sum is equivalent to swapping A_i and A_{N+1}! The multiset of values {A_1, ..., A_{N+1}} is completely invariant under operations. Transformation is possible iff multiset(A) == multiset(B). When possible, mismatched positions A_i != B_i define directed permutation cycles. Resolving C connected components requires (mismatched elements) + (C - 1) swaps if A_{N+1} is in a component, or + C if an extra swap is needed to bring A_{N+1} into the cycle.
- Common Reductions: Given array A of length N and target array B. In one operation, replace A_i with the XOR sum of all elements in A. Find the minimum operations to transform A into B, or -1 if impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc016_d`](../../analysis/AtCoder-agc016_d.md) | D. XOR Replace | 2910 | Given array A of length N and target array B. In one operation, replace A_i with the XOR sum of all elements in A. Find ... |
