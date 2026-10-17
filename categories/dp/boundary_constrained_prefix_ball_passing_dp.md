# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A ball starting at Snuke $i$ requires at least $i$ steps to reach Takahashi. Therefore, among the first $t$ balls Takahashi receives, only balls originating from the first $\min(t, N)$ Snukes could possibly have arrived. Thus, for any step $t$, the number of received red balls $r_t$ must satisfy $r_t \le R_{\min(t, N)}$ and the number of blue balls $b_t = t - r_t \le B_{\min(t, N)}$. This condition is necessary and sufficient.
- Common Reductions: There are $N$ Snukes in a line, each starting with 2 balls (red/blue). In each of $2N$ steps, every Snuke with $\ge 1$ ball passes one ball forward, and Takahashi collects the ball from Snuke 1. Find the number of possible sequences of $2N$ balls Takahashi can receive modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-yahoo_procon2019_qual_f`](../../analysis/AtCoder-yahoo_procon2019_qual_f.md) | F. Pass | 2253 | There are $N$ Snukes in a line, each starting with 2 balls (red/blue). In each of $2N$ steps, every Snuke with $\ge 1$ b... |
