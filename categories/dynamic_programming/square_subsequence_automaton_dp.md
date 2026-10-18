# Substring DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `Substring DP`

## Description
This topic focuses on substring dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: To count each square subsequence $T T$ exactly once, fix the canonical starting index $x$ of the second copy of $T$ in $S$. The first character is $T_1 = S_x$, and the first copy must start at $p_1 = \sigma(0, T_1)$. A common subsequence automaton DP on two pointers $(i, j)$ tracking the positions of $T$ in $S[1..x-1]$ and $S[x..N]$ counts valid $T$ under the termination rule $\sigma(p_n, T_1) = x$.
- Common Reductions: Count non-empty strings $T$ such that $T T$ is a subsequence of $S$. Fixing the canonical starting position of the second copy of $T$ eliminates duplicate counting, solved via subsequence automaton DP in $O(N^3 \cdot 26)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc299_f`](../../analysis/AtCoder-abc299_f.md) | F. Square Subsequence | 2349 | Count non-empty strings $T$ such that $T T$ is a subsequence of $S$. Fixing the canonical starting position of the secon... |
