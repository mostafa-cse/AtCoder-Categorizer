# Tree Isomorphism

**Taxonomy Path**: `Miscellaneous` > `General` > `Tree Isomorphism`

## Description
This topic focuses on tree isomorphism techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A tree with minimum colorfulness must be completely symmetric with respect to either a central vertex (giving radius $D$, colorfulness $D+1$) or a central edge (giving radius $D$, colorfulness $D+1$).
- Common Reductions: Expand a tree $G$ by adding leaves so that all vertices in each color class have isomorphic rooted trees. Minimize colorfulness, and secondarily minimize the number of leaves.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc024_d`](../../analysis/AtCoder-agc024_d.md) | D. Isomorphism Freak | 2307 | Expand a tree $G$ by adding leaves so that all vertices in each color class have isomorphic rooted trees. Minimize color... |
