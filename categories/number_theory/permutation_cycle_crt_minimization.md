# Chinese Remainder Theorem (CRT)

**Taxonomy Path**: `Number Theory` > `Modular Arithmetic` > `Chinese Remainder Theorem (CRT)`

## Description
This topic focuses on chinese remainder theorem (crt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Decompose permutation $P$ into disjoint cycles. To minimize $A$ lexicographically, we greedily determine the optimal shift $s_c$ for each cycle in increasing order of index $1 \dots N$. Each cycle of length $L$ restricts the exponent $k$ by $k \equiv s_c \pmod L$, which propagates constraints $k \equiv s_c \pmod{\gcd(L, L')}$ to all other cycle lengths $L'$ via Chinese Remainder Theorem.
- Common Reductions: Find the lexicographically smallest permutation $A_{P^k(i)}$. Permutation cycle decomposition and greedy shift selection sequentially constrain $k$ across distinct cycle lengths via CRT and extended GCD in $O(N + D^2 \log N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc371_g`](../../analysis/AtCoder-abc371_g.md) | G. Lexicographically Smallest Permutation | 2348 | Find the lexicographically smallest permutation $A_{P^k(i)}$. Permutation cycle decomposition and greedy shift selection... |
