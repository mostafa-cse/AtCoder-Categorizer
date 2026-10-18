# Exchange Arguments

**Taxonomy Path**: `Miscellaneous` > `Greedy Algorithms` > `Exchange Arguments`

## Description
This topic focuses on exchange arguments techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Sort boxes descending by capacity $V_i$. If $M > N$, Mr. Box cannot achieve positive score (output 0). If box $t$ is the $M$-th largest capacity chosen, the top $M-1$ chosen boxes must come from $\{0 \dots t-1\}$ and contribute $-(P_i - 1)$ to profit. To maximize profit, greedily select the $M-1$ smallest values of $P_i - 1$. Box $t$ yields $V_t - P_t$, and all subsequent boxes $i > t$ with $V_i > P_i$ can be freely included.
- Common Reductions: Mr. Box chooses a subset of boxes with capacities $V_i$ and prices $P_i$. If $\ge M$ boxes are bought, Mr. Ball leaves the $M-1$ largest-capacity chosen boxes empty and fills the rest to capacity. Maximize Mr. Box's profit.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc186_c`](../../analysis/AtCoder-arc186_c.md) | C. Ball and Box | 2451 | Mr. Box chooses a subset of boxes with capacities $V_i$ and prices $P_i$. If $\ge M$ boxes are bought, Mr. Ball leaves t... |
