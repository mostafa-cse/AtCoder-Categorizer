# Suffix Array

**Taxonomy Path**: `Strings` > `Suffix Structures` > `Suffix Array`

## Description
This topic focuses on suffix array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For adjacent suffixes $A_i$ and $A_{i+1}$ in the suffix array, $S[A_i] \le S[A_{i+1}]$. If $rank[A_i + 1] < rank[A_{i+1} + 1]$, equality $S[A_{i+1}] = S[A_i]$ preserves suffix order; otherwise, a strict character increment $S[A_{i+1}] = S[A_i] + 1$ is strictly required.
- Common Reductions: Invert a given suffix array $A$ into the lexicographically smallest uppercase string $S$. Characters are determined greedily by comparing next-suffix ranks $rank[A_i + 1] < rank[A_{i+1} + 1]$ in $O(N)$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc044_d`](../../analysis/AtCoder-arc044_d.md) | D. suffix array | 2335 | Invert a given suffix array $A$ into the lexicographically smallest uppercase string $S$. Characters are determined gree... |
