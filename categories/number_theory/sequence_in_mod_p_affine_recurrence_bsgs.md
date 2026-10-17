# Discrete Log / Baby Step Giant Step

**Taxonomy Path**: `Number Theory` > `Modular Arithmetic` > `Discrete Log / Baby Step Giant Step`

## Description
This topic focuses on discrete log / baby step giant step techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Unfolding the affine recurrence yields X_i = A^i S + B (A^i - 1) / (A - 1) mod P. Multiplying by (A - 1) yields A^i ((A - 1)S + B) = (A - 1)G + B mod P, which reduces to a standard discrete logarithm A^i = Y mod P solvable via Baby-Step Giant-Step (BSGS) in O(sqrt(P)) time.
- Common Reductions: Find the smallest index i >= 0 such that X_i = G for recurrence X_0 = S, X_i = (A X_{i-1} + B) mod P for prime P <= 10^9.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc270_g`](../../analysis/AtCoder-abc270_g.md) | Sequence in mod P | 2220 | Find the smallest index i >= 0 such that X_i = G for recurrence X_0 = S, X_i = (A X_{i-1} + B) mod P for prime P <= 10^9... |
