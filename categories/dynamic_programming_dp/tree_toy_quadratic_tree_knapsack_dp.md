# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Inserting an element at node $v$ shifts all elements on the path from $v$ to root 1, expelling the current root value. Inserting elements into a connected component $C$ containing root 1 from leaves to root completely expels the original values of $C$, replacing them with any $|C|$ elements from $t$. To maximize total sum, for each component size $k$, we replace the minimum sum connected component containing root 1 with the largest $k$ elements of $t$. The minimum sum for each size $k$ is computed via Tree Knapsack DP in bounded $O(N^2)$ time.
- Common Reductions: Maximize the total sum in a rooted tree with initial values $s_v$ by replacing values via path-shifting insertions with at most $M$ numbers from $t$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc029_4`](../../analysis/AtCoder-arc029_4.md) | D - 高橋君と木のおもちゃ | 2438 | Maximize the total sum in a rooted tree with initial values $s_v$ by replacing values via path-shifting insertions with ... |
