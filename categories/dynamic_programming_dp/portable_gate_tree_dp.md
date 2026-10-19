# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The vertices visited by the gate form a connected subtree A containing the start vertex v. Any edge outside A belongs to a connected subtree B_i rooted at some l_i in A. In any subtree with m edges ending at depth d from its root, traversing all edges costs 2m - d. Since the sum of edges across all subtrees is N - 1, minimizing total cost is equivalent to maximizing the sum of saved endpoint distances sum(d). For a fixed root v, tree DP maintains: (1) height h(u), (2) dp0(u): max savings if u in A and the journey in A exits u to return to its parent, and (3) dp1(u): max savings if the journey in A terminates inside subtree u. Rerooting DP computes this for all possible roots v in O(N) time.
- Common Reductions: Alice visits all vertices of a tree using a piece and a magical gate. Moving the piece to an adjacent vertex costs 1. Teleporting the piece to the gate or moving the gate to the piece costs 0. We want to find the minimum total movement cost to visit every vertex.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc179_d`](../../analysis/AtCoder-arc179_d.md) | D - Portable Gate | 2717 | Alice visits all vertices of a tree using a piece and a magical gate. Moving the piece to an adjacent vertex costs 1. Te... |
