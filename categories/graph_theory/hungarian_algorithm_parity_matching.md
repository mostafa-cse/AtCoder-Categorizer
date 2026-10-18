# Hungarian Algorithm / Bipartite Weighted Matching

**Taxonomy Path**: `Graph Theory` > `Matching` > `Hungarian Algorithm / Bipartite Weighted Matching`

## Description
This topic focuses on hungarian algorithm / bipartite weighted matching techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Fixing the number $s$ of all-add operations, matching $A_i$ to $B_j$ requires: (1) $(A_i + s) \equiv B_j \pmod 2$, and (2) $||A_i| - |B_j|| \le s$. The number of required sign flips is 0 if $A_i + s = B_j$, 1 if $|A_i + B_j| \le s$, and 2 otherwise. The minimal feasible $s_{min}$ is found by sorting $|A_i|$ and $|B_j|$ by parity; since every element can match with at most 2 sign flips, the optimal $s$ lies in $[s_{min}, s_{min} + 2N]$.
- Common Reductions: Match multisets $A$ and $B$ under adding 1 to all elements or negating single elements. The minimum required shift $s_{min}$ is found by sorting by parity; iterating $s \in [s_{min}, s_{min} + 2N]$ and running the Hungarian algorithm on sign-flip costs solves the problem in $O(N^4)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc232_c`](../../analysis/AtCoder-arc232_c.md) | C. All Add or Single Negate | 2360 | Match multisets $A$ and $B$ under adding 1 to all elements or negating single elements. The minimum required shift $s_{m... |
