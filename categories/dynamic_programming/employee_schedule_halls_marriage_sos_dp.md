# Sum Over Subsets DP (SOS DP)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Sum Over Subsets DP (SOS DP)`

## Description
This topic focuses on sum over subsets dp (sos dp) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: This is bipartite matching between N employees (demand K each) and days 1..D (capacity 1). By Hall's Marriage Theorem, a valid matching exists iff for every subset S of employees, the number of days where at least one employee in S works is at least |S| * K. Equivalently, the number of days where the working mask W(d) is a subset of S^c must be at most D - |S| * K. Since D <= 2NK <= 3.6 * 10^6, binary search on D with Fast Walsh-Hadamard / SOS DP on 2^18 masks checks Hall's condition in O(N * 2^N) per step.
- Common Reductions: N employees (N <= 18) cycle between working A_i days and resting A_i days. Each day, 1 working employee can receive a medal. Find the minimum days D so that every employee receives at least K medals.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc106_e`](../../analysis/AtCoder-arc106_e.md) | E - Medals | 2825 | N employees (N <= 18) cycle between working A_i days and resting A_i days. Each day, 1 working employee can receive a me... |
