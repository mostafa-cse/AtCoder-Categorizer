# Rerooting Technique

**Taxonomy Path**: `Graph Theory` > `More Tree Stuff` > `Rerooting Technique`

## Description
This topic focuses on rerooting technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Deleting vertex $u$ preserves the maximum matching size iff there exists a maximum matching that leaves $u$ unmatched. In a tree, a vertex $u$ can be left unmatched iff, when the tree is rooted at $u$, ALL of its neighbors are matched within their respective subtrees (so $u$ has no unmatched neighbor to greedily match with).
- Common Reductions: Count vertices whose deletion does not decrease the tree's maximum matching size. A vertex can be left unmatched iff all its neighbors are matched in their subtrees when rooted at $u$, solved via 2-pass rerooting DP in $O(N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc223_g`](../../analysis/AtCoder-abc223_g.md) | G. Vertex Deletion | 2351 | Count vertices whose deletion does not decrease the tree's maximum matching size. A vertex can be left unmatched iff all... |
