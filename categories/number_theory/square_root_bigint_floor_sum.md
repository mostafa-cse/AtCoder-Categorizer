# Sum of Floors

**Taxonomy Path**: `Number Theory` > `Floor Sum` > `Sum of Floors`

## Description
This topic focuses on sum of floors techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: sqrt(N) starts with a means that for some power of 10, say 10^k, a * 10^k <= sqrt(N) < (a + 1) * 10^k. Squaring both sides yields (a * 10^k)^2 <= N < ((a + 1) * 10^k)^2. We want the minimal integer N whose decimal representation begins with a. This is an interval floor sum / square root inequality over arbitrary-precision integers (BigInt). We search for the smallest power k such that ceil((a * 10^k)^2) <= floor(((a + 1) * 10^k)^2) and find the minimal valid N.
- Common Reductions: Given a positive integer string a of length up to 1000 representing the initial digits of a square root, find the smallest integer N such that the decimal expansion of sqrt(N) starts with a.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc057_c`](../../analysis/AtCoder-arc057_c.md) | C. 2乗根 (Square Root) | 2547 | Given a positive integer string a of length up to 1000 representing the initial digits of a square root, find the smalle... |
