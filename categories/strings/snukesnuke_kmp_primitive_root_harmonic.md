# Knuth Morris Pratt (KMP) and Prefix Automaton

**Taxonomy Path**: `Strings` > `String Matching` > `Knuth Morris Pratt (KMP) and Prefix Automaton`

## Description
This topic focuses on knuth morris pratt (kmp) and prefix automaton techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any string $S_i$ has a unique primitive root $T$ such that $S_i = T^c$. Two powers $S_i^k$ and $S_j^{k'}$ are identical iff they share the exact same root $T$ and $c_i \cdot k = c_j \cdot k'$. Group strings by primitive root $T$ (found in $O(|S_i|)$ via KMP $\pi$-table). For each multiplicity $c$, advance a pointer `next_k[c]` while $c \cdot k$ is already in the used set. The total work per root is bounded by the harmonic series $\sum M/c = O(M \log M)$.
- Common Reductions: For strings $S_1, \dots, S_N$, find the smallest $k \ge 1$ such that $S_i^k$ has not yet been registered, register it, and output $k$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc312_h`](../../analysis/AtCoder-abc312_h.md) | Ex. snukesnuke | 2477 | For strings $S_1, \dots, S_N$, find the smallest $k \ge 1$ such that $S_i^k$ has not yet been registered, register it, a... |
