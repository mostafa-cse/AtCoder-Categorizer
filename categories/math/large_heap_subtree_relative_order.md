# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any vertex in a min-heap, its value is the minimum of its subtree. The relative ordering of nodes on two branches descending from an LCA can be analyzed by considering the sizes of subtrees attached along the paths to U and V. At each step, the probability that the next element from branch 1 is smaller than branch 2 is sz_1 / (sz_1 + sz_2), reducing to a 2D path DP.
- Common Reductions: In a complete binary tree of depth N labeled uniformly at random with a min-heap structure, find the probability that vertex U has a smaller label than vertex V. The relative order of U and V in a random heap depends on their lowest common ancestor W and the subtrees hanging along the paths from W to U and W to V, solvable by DP over tree ancestor paths in O(N^2) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc060_c`](../../analysis/AtCoder-agc060_c.md) | Large Heap | 2680 | In a complete binary tree of depth N labeled uniformly at random with a min-heap structure, find the probability that ve... |
