# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The Grundy function for a pile of X stones with divisor K satisfies G(X, K) = X / K when X % K == 0, and G(X, K) = G(X - (floor(X/K) + 1), K) otherwise. Because d = floor(X/K) remains constant across contiguous ranges of length d+1, division jumps of size (X % K) // (d + 1) compress long subtraction chains into O(sqrt(A/K)) steps.
- Common Reductions: The Sprague-Grundy theorem reduces the game to Nim with Grundy values G(X, K) = X/K (if K | X) and G(X - floor(X/K) - 1, K) otherwise. Division jumps accelerate the recursion to O(sqrt(A/K)) per pile, total O(N sqrt(max A)) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc091_d`](../../analysis/AtCoder-arc091_d.md) | F. Strange Nim | 2395 | The Sprague-Grundy theorem reduces the game to Nim with Grundy values G(X, K) = X/K (if K | X) and G(X - floor(X/K) - 1,... |
