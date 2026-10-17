# [Technique] XOR Basis ft Reduced Row Echelon Form

**Taxonomy Path**: `Math` > `Linear Algebra` > `[Technique] XOR Basis ft Reduced Row Echelon Form`

## Description
This topic focuses on [technique] xor basis ft reduced row echelon form techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Starting with V = {0}, at step k connecting each u in V to u ^ b_k adds 2^{k-1} edges with allowed difference b_k in S. Because b_k is linearly independent from previous basis vectors, no cycles are formed, producing a valid tree of N - 1 edges.
- Common Reductions: Build a spanning tree on N = 2^n vertices using edges with XOR differences not in A. The allowed difference set S = {1..N-1} \ A must span F_2^n; if not, output -1. If S spans F_2^n, extract a basis b_1..b_n in S and build a hypercube spanning tree by iteratively doubling components: (u, u ^ b_k).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-zone2021_f`](../../analysis/AtCoder-zone2021_f.md) | F. Encounter and Farewell | 2197 | Build a spanning tree on N = 2^n vertices using edges with XOR differences not in A. The allowed difference set S = {1..... |
