# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Root the tree at candidate vertex r. Each operation decreases the sum of depths of all pieces sum d_i by 2. Thus, the total depth must be even, and operations correspond to pairing moves from different subtrees of r. In any subtree, excess moves can be eliminated by internal pairings if the heavy subtree does not dominate. Tree DP computes the minimum and maximum remaining uncancelled depth for every subtree.
- Common Reductions: Given a tree with pieces on some vertices, an operation moves two pieces at distance >= 2 one step closer along their shortest path. Find the minimum operations to gather all pieces at a single vertex, or report impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc034_e`](../../analysis/AtCoder-agc034_e.md) | E - Complete Compress | 2637 | Given a tree with pieces on some vertices, an operation moves two pieces at distance >= 2 one step closer along their sh... |
