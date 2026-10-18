# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the lexicographically smallest permutation $P$ derived from a valid bracket sequence $S$, consecutive pairs $(P_{2i-1}, P_{2i})$ with $P_{2i-1} > P_{2i}$ can only occur if $S[P_{2i-1}] = '('$ and $S[P_{2i}] = ')'$. In the lexicographically largest permutation $Q$, pairs $(Q_{2i-1}, Q_{2i})$ with $Q_{2i-1} < Q_{2i}$ force $S[Q_{2i-1}] = '('$ and $S[Q_{2i}] = ')'$. Any unspecified characters can be uniquely deduced, and then validated by greedy reconstruction.
- Common Reductions: Reconstruct a valid bracket sequence from its lexicographically smallest and largest permutations. Adjacent inversions force bracket types, with greedy validation in $O(N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc141_c`](../../analysis/AtCoder-arc141_c.md) | C. Bracket Manufacture | 2342 | Reconstruct a valid bracket sequence from its lexicographically smallest and largest permutations. Adjacent inversions f... |
