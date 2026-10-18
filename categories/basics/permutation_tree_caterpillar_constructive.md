# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A tree can be realized by a permutation iff it is a caterpillar tree (all vertices are at distance at most 1 from a central spine path). Pruning all leaves leaves a simple path u_1 - u_2 - ... - u_k. Each spine vertex u_i of degree deg(u_i) corresponds to a block of size deg(u_i) - 1. Blocks of the form (B+1 ... B+s-1, B) can be oriented forward or backward along the spine path.
- Common Reductions: Given a tree of N vertices, determine if it can be realized as a permutation tree and find the lexicographically smallest permutation P.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc095_d`](../../analysis/AtCoder-arc095_d.md) | F - Permutation Tree | 2626 | Given a tree of N vertices, determine if it can be realized as a permutation tree and find the lexicographically smalles... |
