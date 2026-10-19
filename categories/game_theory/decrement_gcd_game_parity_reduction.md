# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Analyze parity. If the number of even elements cnt_even is odd, the first player can decrement an even element to make it odd, leaving an even number of even elements and no GCD division can occur (since at least one odd element remains odd). If cnt_even is even and cnt_odd > 1, any move leaves an odd number of even elements, and GCD cannot divide out 2, so the opponent wins. The only non-trivial case is when cnt_even is even and cnt_odd == 1: the player must decrement the single odd element (if > 1), after which all elements become even and GCD is divided by an even number >= 2. This recursive division can happen at most O(log(max A)) times.
- Common Reductions: Two players play a game with an array of positive integers A where gcd(A_1, ..., A_N) = 1. A move consists of choosing an element A_i > 1, decrementing it by 1, and dividing all elements by their new GCD. The first player who cannot move loses. Determine if the first player has a winning strategy.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc010_d`](../../analysis/AtCoder-agc010_d.md) | D - Decrementing | 2795 | Two players play a game with an array of positive integers A where gcd(A_1, ..., A_N) = 1. A move consists of choosing a... |
