# Suffix Array

**Taxonomy Path**: `Strings` > `Suffix Structures` > `Suffix Array`

## Description
This topic focuses on suffix array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: To compare $S_i + S_j$ and $S_j + S_i$ where $|S_i| < |S_j|$: if $S_i$ is not a prefix of $S_j$, the first $|S_i|$ characters determine the comparison via $LCP(i, j)$. If $S_i$ is a prefix of $S_j$, comparing $S_i + S_j$ with $S_j + S_i$ reduces to comparing $S_j$ with $S_j[|S_i| \dots] + S_i$, which is a second LCP query between $j$ and $j + |S_i|$.
- Common Reductions: Given a string $S$ of length $N$, sort the $N$ suffixes by comparing the infinite periodic concatenations $S[i \dots N]^\infty$ vs $S[j \dots N]^\infty$, which simplifies to comparing $S_i + S_j$ against $S_j + S_i$ where $S_i = S[i \dots N]$. The string comparison $S_i + S_j < S_j + S_i$ can be evaluated in $O(1)$ time by comparing at most two intervals using Longest Common Prefix (LCP) queries on the Suffix Array with a Sparse Table RMQ.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc050_d`](../../analysis/AtCoder-arc050_d.md) | D. Suffix Concat | 2487 | Given a string $S$ of length $N$, sort the $N$ suffixes by comparing the infinite periodic concatenations $S[i \dots N]^... |
