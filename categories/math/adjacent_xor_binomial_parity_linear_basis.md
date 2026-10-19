# Vector Space and XOR Basis

**Taxonomy Path**: `Math` > `Linear Algebra` > `Vector Space and XOR Basis`

## Description
This topic focuses on vector space and xor basis techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: After 1 step, all popcounts become even. For N = 2 or N not equiv 2 mod 4, ANY non-empty even subset of A can be achieved as the final element, which is the vector space spanned by {A_1 ^ A_i}_{i=2}^N. When N > 2 and N equiv 2 mod 4, all even subsets EXCEPT the full set of all N elements are achievable. In that case, we can omit each element A_j one by one and take the maximum over the basis of the remaining N-1 elements.
- Common Reductions: Given array A of N integers (N <= 100, A_i < 2^60), repeatedly rearrange A and replace with adjacent XORs until length 1. Find the maximum possible value of the final element.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc173_e`](../../analysis/AtCoder-arc173_e.md) | E - Rearrange and Adjacent XOR | 2869 | Given array A of N integers (N <= 100, A_i < 2^60), repeatedly rearrange A and replace with adjacent XORs until length 1... |
