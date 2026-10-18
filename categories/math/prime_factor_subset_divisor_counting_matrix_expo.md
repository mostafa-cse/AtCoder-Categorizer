# Matrix Exponentiation

**Taxonomy Path**: `Math` > `Matrices` > `Matrix Exponentiation`

## Description
This topic focuses on matrix exponentiation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The number of divisors is prod_{j=1}^6 (e_j + 1) = sum_{S subset {1..6}} prod_{j in S} e_j. Each element A_t contributes v_{p_j}(A_t) to a subset of required primes. This defines a 64-state submask transition matrix, extended to 65x65 to compute prefix sums over all lengths 1 to N.
- Common Reductions: Sum the number of positive divisors of the product across all sequences of length 1 to N with elements in [1, M] (M <= 16). Because only 6 primes exist <= 16, expand the divisor count over prime subsets and evaluate via 65x65 Matrix Exponentiation.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc182_c`](../../analysis/AtCoder-arc182_c.md) | C. Sum of Number of Divisors of Product | 2408 | Sum the number of positive divisors of the product across all sequences of length 1 to N with elements in [1, M] (M <= 1... |
