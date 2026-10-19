# Heavy Light Decomposition (HLD) ft Subtrees and Path Query

**Taxonomy Path**: `Data Structures (DS)` > `Heavy Light Decomposition (HLD)` > `Heavy Light Decomposition (HLD) ft Subtrees and Path Query`

## Description
This topic focuses on heavy light decomposition (hld) ft subtrees and path query techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each node's hash transition is an affine transformation x -> m * x + c of its heavy child's hash, with multiplier m given by the product of light children's hashes. Under Heavy-Light Decomposition (HLD), each heavy path is a sequence of affine functions whose composition is associative. A Segment Tree over each heavy chain maintains the composed affine transformation. Point updates modify a leaf and propagate up light edges in O(log^2 N) time.
- Common Reductions: Given a rooted tree with values A_v where each node's hash is recursively defined as an affine function of its children's hashes, process point value updates and query the root hash H(1).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc351_g`](../../analysis/AtCoder-abc351_g.md) | G. Hash on Tree | 2920 | Given a rooted tree with values A_v where each node's hash is recursively defined as an affine function of its children'... |
