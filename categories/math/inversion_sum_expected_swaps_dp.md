# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In operation (X, Y): P(A_X > A_Y) and P(A_Y > A_X) become (P(A_X > A_Y) + P(A_Y > A_X)) / 2. For any third index k != X, Y: P(A_k > A_X) and P(A_k > A_Y) both become (P(A_k > A_X) + P(A_k > A_Y)) / 2, and symmetrically for P(A_X > A_k) and P(A_Y > A_k). All other pairs are untouched.
- Common Reductions: Finding sum of inversions over 2^Q operation outcomes where each operation swaps A_X and A_Y with probability 1/2. By linearity of expectation, total inversions = 2^Q * sum_{i < j} P(A_i > A_j). Each swap operation (X, Y) only affects pairs involving X or Y, allowing an O(N) update per operation.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc030_d`](../../analysis/AtCoder-agc030_d.md) | Inversion Sum | 2712 | Finding sum of inversions over 2^Q operation outcomes where each operation swaps A_X and A_Y with probability 1/2. By li... |
