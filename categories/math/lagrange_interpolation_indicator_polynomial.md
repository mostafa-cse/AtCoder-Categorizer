# Lagrange Interpolation

**Taxonomy Path**: `Math` > `Polynomial` > `Lagrange Interpolation`

## Description
This topic focuses on lagrange interpolation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any element a in F_p, (x - a)^{p-1} is 0 if x=a and 1 if x != a (mod p). Thus, the indicator polynomial for x = a is I_a(x) = 1 - (x - a)^{p-1}. Summing over all a with f(a) = 1 gives P(x) = sum_{a: f(a)=1} (1 - (x - a)^{p-1}) mod p.
- Common Reductions: Given a function f: F_p -> {0, 1}, construct a polynomial P(x) of degree at most p-1 such that P(x) = f(x) for all x in F_p. By Fermat's Little Theorem, the indicator function for x=a is 1 - (x - a)^{p-1}.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc137_f`](../../analysis/AtCoder-abc137_f.md) | F. Polynomial Construction | 2402 | Given a function f: F_p -> {0, 1}, construct a polynomial P(x) of degree at most p-1 such that P(x) = f(x) for all x in ... |
