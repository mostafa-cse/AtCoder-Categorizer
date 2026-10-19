# Floor Sum and Mod Sum of Arithmetic Progression

**Taxonomy Path**: `Number Theory` > `Floor Sum` > `Floor Sum and Mod Sum of Arithmetic Progression`

## Description
This topic focuses on floor sum and mod sum of arithmetic progression techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Substituting X = A * k + B, the sum over k=1..R becomes sum_{k=1}^R floor((A*k + B + 2^b) / 2^{b+1}) - sum_{k=1}^R floor((A*k + B) / 2^{b+1}). Each sum is an evaluation of ACL floor_sum. With 30 bits, each query runs in O(30 log(mod)) time.
- Common Reductions: Compute sum_{k=1}^R popcount(A * k + B) efficiently for A, B, R <= 10^9. Because popcount(X) = sum_{b=0}^{60} ((X >> b) & 1), we can decompose the sum bit-by-bit: the b-th bit of X is 1 iff floor((X + 2^b) / 2^{b+1}) - floor(X / 2^{b+1}) = 1. Summing over k reduces each bit to standard AtCoder floor_sum, solvable in O(log(A + 2^b)) per bit.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc283_h`](../../analysis/AtCoder-abc283_h.md) | Popcount Sum | 2682 | Compute sum_{k=1}^R popcount(A * k + B) efficiently for A, B, R <= 10^9. Because popcount(X) = sum_{b=0}^{60} ((X >> b) ... |
