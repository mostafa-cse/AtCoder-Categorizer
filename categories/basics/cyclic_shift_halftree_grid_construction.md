# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Adding M edges doubles to 2M edges after the +K mod N shift. For the result to be a tree, 2M = N - 1, which requires N to be odd (impossible if N is even). For odd N, arranging vertices on an n x g torus grid where moving down a row represents +K mod N allows constructing a tree via interlaced vertical backbone paths and horizontal comb bridges.
- Common Reductions: Add (N-1)/2 edges to an empty graph such that shifting every edge by +K mod N forms a tree. Impossible iff N is even. For odd N, arranging vertices in an n x g grid (n = N/g, g = gcd(N, K)) and placing vertical edges in odd columns, horizontal edges from odd columns, and bottom horizontal edges from even columns constructs a valid spanning tree in O(N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc152_d`](../../analysis/AtCoder-arc152_d.md) | D. Halftree | 2381 | Add (N-1)/2 edges to an empty graph such that shifting every edge by +K mod N forms a tree. Impossible iff N is even. Fo... |
