# Chicken McNugget Theorem

**Taxonomy Path**: `Number Theory` > `Euclidean Algorithm` > `Chicken McNugget Theorem`

## Description
This topic focuses on chicken mcnugget theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By the Chicken McNugget Theorem / Frobenius coin problem, any safe distance w >= B^2 - 3B + 2 <= 342 can always be represented as a non-negative combination of steps in {B-1, B} <= [A, B]. Thus, safe gaps between bad intervals longer than ~400 allow complete reachability across the gap. Only boundaries of safe intervals within distance B matter, reducing N <= 10^18 to O(MB^2) transitions.
- Common Reductions: Determine whether square N can be reached from square 1 with jump lengths in [A, B] avoiding M dangerous intervals of length <= B on a line of size N <= 10^18.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc388_f`](../../analysis/AtCoder-abc388_f.md) | Dangerous Sugoroku | 2214 | Determine whether square N can be reached from square 1 with jump lengths in [A, B] avoiding M dangerous intervals of le... |
