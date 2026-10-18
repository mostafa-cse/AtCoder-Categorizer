# Euclidean Algorithm

**Taxonomy Path**: `Number Theory` > `Euclidean Algorithm` > `Euclidean Algorithm`

## Description
This topic focuses on euclidean algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any fixed right endpoint $i$, the prefix GCDs $\gcd(A_j, \dots, A_i)$ as $j$ decreases from $i$ down to 1 can take at most $\log_2(\max A_i) \le 30$ distinct values because each change divides the GCD by at least 2. We maintain a compressed run-length list of pairs `(gcd_value, count)` ending at position $i$. Advancing to $i+1$ computes $\gcd(g, A_{i+1})$ for each distinct value, merges identical consecutive values, and accumulates counts into a global frequency map.
- Common Reductions: For $M \le 10^5$ queries $x$, count the number of subsegments $[s, t]$ with $\gcd(A_s, \dots, A_t) = x$ in an array of size $N \le 10^5$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc023_4`](../../analysis/AtCoder-arc023_4.md) | D - GCD区間 | 2511 | For $M \le 10^5$ queries $x$, count the number of subsegments $[s, t]$ with $\gcd(A_s, \dots, A_t) = x$ in an array of s... |
