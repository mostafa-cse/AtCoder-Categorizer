# Permutations and Permutation Cycles

**Taxonomy Path**: `Miscellaneous` > `Permutations` > `Permutations and Permutation Cycles`

## Description
This topic focuses on permutations and permutation cycles techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Expanding the sequence terms shows a_1 = p, a_2 = q, a_3 = q p^{-1}, a_4 = q p^{-1} q^{-1}, a_5 = q p^{-1} q^{-1} p q^{-1}, a_6 = q p^{-1} q^{-1} p q p^{-1} q^{-1}. Then a_7 = (q p^{-1} q^{-1} p) p (q p^{-1} q^{-1} p)^{-1}. Letting C = q p^{-1} q^{-1} p be the group commutator, we have a_{n+6} = C a_n C^{-1} for all n >= 1. By induction, a_{6m + r} = C^m a_r C^{-m}. Because permutation conjugation preserves cycle structure, C^m is computed in O(N) via cycle decomposition.
- Common Reductions: Compute the K-th permutation in the sequence defined by a_1 = p, a_2 = q, and a_{n+1} = a_n a_{n-1}^{-1} for n >= 2, where K <= 10^18 and N <= 10^5.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc031_d`](../../analysis/AtCoder-agc031_d.md) | D - A Sequence of Permutations | 2953 | Compute the K-th permutation in the sequence defined by a_1 = p, a_2 = q, and a_{n+1} = a_n a_{n-1}^{-1} for n >= 2, whe... |
