# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A balanced bracket sequence naturally represents a forest of nested interval nodes. For each node $u$ corresponding to pair $(i, j)$, the substring $S[i \dots j]$ consists of the two outer brackets $i$ and $j$, plus the disjoint subtrees of its direct children $v \in children(u)$. The difference $\Delta = R - B$ is additive: $\Delta_u = (c_i + c_j) + \sum_{v} \Delta_v$. The outer brackets $(i, j)$ contribute $+2$ (1 way), $0$ (2 ways: RB or BR), or $-2$ (1 way). Since each child $v$ independently enforces $|\Delta_v| \le K$, node $u$ combines its children's $\Delta$ distributions via tree knapsack DP. The maximum value of $|\Delta|$ for a subtree is bounded by its size and by $K$, yielding an overall $O(|S|^2)$ tree DP.
- Common Reductions: Given a balanced bracket sequence $S$ ($|S| \le 3000$) and an integer $K$. Color each bracket Red or Blue such that for every matched pair of brackets $(i, j)$, the substring $S[i \dots j]$ satisfies $|R - B| \le K$. Find the number of valid colorings modulo $10^9 + 7$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-discovery_2016_final_c`](../../analysis/AtCoder-discovery_2016_final_c.md) | C. 特別講演「括弧列と塗り分け」 | 2266 | Given a balanced bracket sequence $S$ ($|S| \le 3000$) and an integer $K$. Color each bracket Red or Blue such that for ... |
