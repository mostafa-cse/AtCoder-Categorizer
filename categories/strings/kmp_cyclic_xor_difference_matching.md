# Knuth Morris Pratt (KMP) and Prefix Automaton

**Taxonomy Path**: `Strings` > `String Matching` > `Knuth Morris Pratt (KMP) and Prefix Automaton`

## Description
This topic focuses on knuth morris pratt (kmp) and prefix automaton techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The relation $a_{(i+k) \bmod N} \oplus x = b_i$ eliminates $x$ upon taking adjacent circular XOR differences $A'_j = a_{(j+1) \bmod N} \oplus a_j$ and $B'_i = b_{(i+1) \bmod N} \oplus b_i$. A valid cyclic shift $k$ corresponds exactly to an exact match of pattern $B'$ in the doubled text $A' A'$, found via KMP in $O(N)$.
- Common Reductions: Given two sequences $a$ and $b$ of length $N$, find all pairs $(k, x)$ with $0 \le k < N$ and $0 \le x < 2^{30}$ such that cyclically shifting $a$ left by $k$ positions and bitwise XORing with $x$ yields $b$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc150_f`](../../analysis/AtCoder-abc150_f.md) | F. Xor Shift | 2281 | Given two sequences $a$ and $b$ of length $N$, find all pairs $(k, x)$ with $0 \le k < N$ and $0 \le x < 2^{30}$ such th... |
