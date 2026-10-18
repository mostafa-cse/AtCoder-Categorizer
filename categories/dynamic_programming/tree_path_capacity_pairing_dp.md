# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Every path operation connects two leaves. In the tree rooted at a non-leaf vertex, each child $w$ passes $c_w$ paths upward to vertex $v$. To cover $A_v$ stones at $v$, the number of paths paired internally at $v$ must be $P = \sum c_w - A_v$, and the upward paths to parent must be $c_v = 2 A_v - \sum c_w$. Valid pairing requires $0 \le P \le A_v$ and $\max(c_w) \le A_v$.
- Common Reductions: Determine if all stones on tree vertices can be removed by subtracting 1 along leaf-to-leaf paths. Rooted tree DP computes the required upward path capacity $c_v = 2 A_v - \sum c_w$ and verifies internal pairability in $O(N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc010_c`](../../analysis/AtCoder-agc010_c.md) | C. Cleaning | 2346 | Determine if all stones on tree vertices can be removed by subtracting 1 along leaf-to-leaf paths. Rooted tree DP comput... |
