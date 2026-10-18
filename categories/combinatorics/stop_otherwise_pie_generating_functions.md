# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each pair $\{u, v\}$ with $u + v = i$ cannot both have non-zero counts. If $P$ such pairs exist, choosing $c$ pairs to both appear with positive counts contributes $(-1)^c \binom{P}{c}$, and the remaining problem is standard stars-and-bars allocation of $N - 2c$ balls into $K$ distinct bins.
- Common Reductions: For each $i \in [2, 2K]$, count multisets of $N$ dice rolls with faces $1 \dots K$ where no two dice sum to $i$. Group the $K$ faces into pairs $\{u, v\}$ summing to $i$, at most one midpoint face $i/2$ (if $i$ is even and $i \le 2K$), and leftover independent faces. In any valid roll, at most one face of each pair can appear. Generating functions or PIE over which pairs are violated counts valid multisets with fixed coefficient extraction in $O(N)$ per query $i$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc102_c`](../../analysis/AtCoder-arc102_c.md) | E. Stop. Otherwise... | 2484 | For each $i \in [2, 2K]$, count multisets of $N$ dice rolls with faces $1 \dots K$ where no two dice sum to $i$. Group t... |
