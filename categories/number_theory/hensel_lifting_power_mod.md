# Chinese Remainder Theorem (CRT)

**Taxonomy Path**: `Number Theory` > `Modular Arithmetic` > `Chinese Remainder Theorem (CRT)`

## Description
This topic focuses on chinese remainder theorem (crt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any $X$ coprime to 10, the equation $n^n \equiv X \pmod{10^k}$ has a unique solution modulo $10^k$ for every $k \ge 2$. Furthermore, the unique solution modulo $10^k$ extends the unique solution modulo $10^{k-1}$ by testing only 10 candidates $a_{k-1} + t \cdot 10^{k-1}$ for $t \in [0, 9]$.
- Common Reductions: Find the smallest positive integer $n$ such that $n^n \equiv X \pmod{10^9}$. Hensel lifting / digit-by-digit lifting uniquely extends the solution from $10^{k-1}$ to $10^k$ by testing only 10 candidates per digit in $O(L^2)$ per query.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc172_e`](../../analysis/AtCoder-arc172_e.md) | E. Last 9 Digits | 2358 | Find the smallest positive integer $n$ such that $n^n \equiv X \pmod{10^9}$. Hensel lifting / digit-by-digit lifting uni... |
