# Mo's Algorithm

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Mo's Algorithm`

## Description
This topic focuses on mo's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The number of distinct permutations of remaining elements in $A[L..R]$ after removing elements $\ge X$ is the multinomial coefficient $S! / \prod_{v < X} c_v!$, where $S = \sum_{v < X} c_v$ and $c_v$ is the frequency of value $v$ in $A[L..R]$. By sorting queries using Mo's algorithm and maintaining frequency counts with block-based SQRT decomposition on the value domain, updates are $O(1)$ and range prefix queries take $O(\sqrt{N})$.
- Common Reductions: Count permutations of remaining elements in $A[L..R]$ after removing elements $\ge X$ as a multinomial coefficient. Sorting queries via Mo's algorithm and maintaining frequency counts with block-based SQRT decomposition on the value domain achieves $O((N + Q) \sqrt{N})$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc405_g`](../../analysis/AtCoder-abc405_g.md) | G. Range Shuffle Query | 2354 | Count permutations of remaining elements in $A[L..R]$ after removing elements $\ge X$ as a multinomial coefficient. Sort... |
