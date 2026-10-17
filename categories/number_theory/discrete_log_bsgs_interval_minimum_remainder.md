# Discrete Log / Baby Step Giant Step

**Taxonomy Path**: `Number Theory` > `Modular Arithmetic` > `Discrete Log / Baby Step Giant Step`

## Description
This topic focuses on discrete log / baby step giant step techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If [A, B] spans a multiple of P - 1, the power X^i mod P hits 1 (the global minimum). Otherwise, if B - A <= 2 * 10^7, directly iterate i from A to B computing X^i mod P in O(B - A). If B - A > 2 * 10^7, the minimum value a in [1, P-1] must be tiny by the pigeonhole principle (typically a <= 100). We can iterate candidate remainders a = 1, 2, ... and test if X^i = a (mod P) has a solution with i in [A, B] using Baby-Step Giant-Step.
- Common Reductions: Find the minimum value of X^i mod P over all integers i in the range [A, B], where P < 2^31 is prime.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc042_d`](../../analysis/AtCoder-arc042_d.md) | あまり | 2247 | Find the minimum value of X^i mod P over all integers i in the range [A, B], where P < 2^31 is prime.... |
