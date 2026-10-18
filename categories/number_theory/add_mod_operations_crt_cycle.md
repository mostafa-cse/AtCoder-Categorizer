# Chinese Remainder Theorem (CRT)

**Taxonomy Path**: `Number Theory` > `Modular Arithmetic` > `Chinese Remainder Theorem (CRT)`

## Description
This topic focuses on chinese remainder theorem (crt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Check consistency: if $A_i = A_j$ with $B_i \ne B_j$, output `No`. Otherwise, reduce to $N'$ distinct sorted pairs $(A_i, B_i)$. An operation with $y = x + \max(A)$ acts as a circular shift, dropping $\max(A)$ and inserting an interval of length $x + \min(A)$. Using a large modulus $K > \max(A) + \max(B)$ and target residue classes $B'_i = B_i + K \cdot r_i$, $N' - 1$ operations configure differences between adjacent elements, and a final operation $(B'_1, K)$ aligns all values simultaneously in $N' \le N$ operations.
- Common Reductions: Transform sequence $A$ to $B$ using at most $N$ operations of the form $A_i \leftarrow (A_i + x) \pmod y$ with $x \ge 0, y \ge 1$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc063_c`](../../analysis/AtCoder-agc063_c.md) | C. Add Mod Operations | 2500 | Transform sequence $A$ to $B$ using at most $N$ operations of the form $A_i \leftarrow (A_i + x) \pmod y$ with $x \ge 0,... |
