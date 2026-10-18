# 2D Prefix Sum

**Taxonomy Path**: `Basics` > `2D Prefix Sum` > `2D Prefix Sum`

## Description
This topic focuses on 2d prefix sum techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When inserting element i into permutation prefixes of length i-1 at relative ranks j and l, the relation between the previous element and the new element depends solely on whether the old element's rank was < or >= the new element's rank. This decomposes the transitions into 4 independent 2D rectangular subgrids that update similarity by +1 or +0.
- Common Reductions: Count pairs of permutations (A, B) of length N with similarity K (matching direction of adjacent steps) by inserting elements 1 to N, maintaining relative ranks of the latest elements, and optimizing rectangular quadrant transitions via 2D prefix sums in O(N^4).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc282_g`](../../analysis/AtCoder-abc282_g.md) | Similar Permutation | 2412 | Count pairs of permutations (A, B) of length N with similarity K (matching direction of adjacent steps) by inserting ele... |
