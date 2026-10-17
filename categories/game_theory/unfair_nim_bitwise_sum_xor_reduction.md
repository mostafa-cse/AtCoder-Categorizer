# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let u = A_1 - d, v = A_2 + d. We need u ^ v = XOR(A_3..A_N) = X and u + v = A_1 + A_2 = S. Since (u + v) - (u ^ v) = 2(u & v), we obtain u & v = D = (S - X) / 2. This requires S >= X, (S - X) even, and (D & X) == 0. To minimize d = A_1 - u, we greedily set bits of X in u from most significant to least while keeping u <= A_1.
- Common Reductions: Transfer minimum d stones (0 <= d < A_1) from pile 1 to pile 2 so that Takahashi wins Nim (overall XOR sum of all N piles becomes 0).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc172_f`](../../analysis/AtCoder-abc172_f.md) | Unfair Nim | 2216 | Transfer minimum d stones (0 <= d < A_1) from pile 1 to pile 2 so that Takahashi wins Nim (overall XOR sum of all N pile... |
