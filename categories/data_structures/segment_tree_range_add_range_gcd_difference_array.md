# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By the Euclidean algorithm property gcd(x, y) = gcd(x, y - x), the GCD of a range satisfies gcd(a_l, a_{l+1}, ..., a_r) = gcd(a_l, gcd_{i=l+1}^r |a_i - a_{i-1}|). Under the difference array D_i = a_i - a_{i-1}, a range addition [l, r] += t modifies only two elements: D_l += t and D_{r+1} -= t. Thus, range additions become point updates on D, and range GCD queries become gcd(prefix_sum(l), range_gcd(D, l+1, r)).
- Common Reductions: Maintain an array under range additions [l, r] += t and range greatest common divisor queries gcd(a_l, ..., a_r).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc017_4`](../../analysis/AtCoder-arc017_4.md) | ARCたんクッキー | 2244 | Maintain an array under range additions [l, r] += t and range greatest common divisor queries gcd(a_l, ..., a_r).... |
