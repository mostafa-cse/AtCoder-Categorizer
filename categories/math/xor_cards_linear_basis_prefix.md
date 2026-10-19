# Vector Space and XOR Basis

**Taxonomy Path**: `Math` > `Linear Algebra` > `Vector Space and XOR Basis`

## Description
This topic focuses on vector space and xor basis techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Represent each card as a 60-bit vector (A_i << 30) | B_i and perform Gaussian elimination over GF(2) to obtain a row echelon basis of at most 60 cards. The cards partition into those with A_i != 0 (at most 30 cards, with strictly decreasing MSBs) and those with A_i == 0. When considering whether to pick card i with MSB 2^k, the remaining cards can only affect bits < k. If (A' | (2^k - 1)) <= K, any choice of remaining cards is guaranteed to keep the front XOR <= K, allowing us to freely maximize B using the remaining cards as a linear basis. Otherwise, we uniquely follow the branch that matches bit k of K.
- Common Reductions: Given N cards with A_i on the front and B_i on the back, choose one or more cards such that XOR(A_i) <= K, maximizing XOR(B_i).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc249_g`](../../analysis/AtCoder-abc249_g.md) | G - Xor Cards | 2757 | Given N cards with A_i on the front and B_i on the back, choose one or more cards such that XOR(A_i) <= K, maximizing XO... |
