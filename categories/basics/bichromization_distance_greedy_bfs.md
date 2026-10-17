# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any vertex $v$, its nearest opposite-color vertex has distance $D_v$. Therefore, $v$ must have at least one neighbor $u$ with $D_u \le D_v$. When processed in ascending order of $D$, coloring $v$ opposite to an already colored neighbor $u$ with $D_u \le D_v$ and setting edge weight $D_v$ satisfies $v$ without violating $u$.
- Common Reductions: Color vertices Black and White and assign edge weights so that the shortest path from each vertex $v$ to an opposite color equals $D_v$. Greedy processing in ascending order of $D_v$ pairs each vertex with a neighbor $u$ having $D_u \le D_v$ in $O(N \log N + M)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-keyence2020_e`](../../analysis/AtCoder-keyence2020_e.md) | E. Bichromization | 2340 | Color vertices Black and White and assign edge weights so that the shortest path from each vertex $v$ to an opposite col... |
