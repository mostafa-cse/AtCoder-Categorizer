# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The reversible deterministic condition forces the tree to be partitioned into disjoint simple paths (movement paths) of length >= 2, where exactly one endpoint is empty and tokens oscillate back and forth. No conflicting edges can exist between adjacent paths: non-endpoints can only connect to non-endpoints, and endpoints must connect oppositely. This yields a tree DP with states classifying a node's path degree (0, 1, or 2 connections into child subtrees) and endpoint status.
- Common Reductions: On a tree of N vertices, place tokens on a non-empty subset such that every good move (moving each token to an adjacent vertex with at most 1 token per edge and per vertex) is uniquely determined for all infinite steps.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc142_d`](../../analysis/AtCoder-arc142_d.md) | D. Deterministic Placing | 2938 | On a tree of N vertices, place tokens on a non-empty subset such that every good move (moving each token to an adjacent ... |
