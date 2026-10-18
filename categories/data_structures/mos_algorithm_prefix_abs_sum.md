# Mo's Algorithm

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Mo's Algorithm`

## Description
This topic focuses on mo's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Prefix queries $\sum_{i=1}^X \sum_{j=1}^Y |A_i - B_j|$ on static sequences $A$ and $B$ can be maintained under pointer movement: advancing $X$ queries the current multiset $B_{1..Y}$ via Fenwick tree in $O(\log N)$, and advancing $Y$ queries $A_{1..X}$. Ordering queries with Mo's algorithm on $(X_k, Y_k)$ with block size $N / \sqrt{K}$ yields $O((N + K)\sqrt{K} \log N)$ total work.
- Common Reductions: Answer $K$ prefix queries $\sum_{i=1}^X \sum_{j=1}^Y |A_i - B_j|$ on arrays of size $N$. Maintaining two Fenwick trees over coordinate-compressed values under 2D Mo's algorithm with block size $N/\sqrt{K}$ yields $O((N + K)\sqrt{K} \log N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc384_g`](../../analysis/AtCoder-abc384_g.md) | G. Abs Sum | 2343 | Answer $K$ prefix queries $\sum_{i=1}^X \sum_{j=1}^Y |A_i - B_j|$ on arrays of size $N$. Maintaining two Fenwick trees o... |
