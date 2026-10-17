# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A sequence $b \le P$ diverges from $P$ at the earliest index $i$ where $b[i] < P[i]$. For each diverging index $i$, any element $t \in P[0 \dots i-1]$ is included with probability 1, while any $t \notin P[0 \dots i-1]$ is included if $b[i] = t$ (possible when $t < P[i]$) or if $t$ is chosen in the remaining $K - 1 - i$ positions.
- Common Reductions: For each $t \in [1, N]$, count permutations $b \le P$ of length $K$ containing $t$. Decomposing by the first diverging position and counting occurrences of $t$ via an offline Fenwick tree sweep solves in $O(N \log N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc174_e`](../../analysis/AtCoder-arc174_e.md) | E. Existence Counting | 2336 | For each $t \in [1, N]$, count permutations $b \le P$ of length $K$ containing $t$. Decomposing by the first diverging p... |
