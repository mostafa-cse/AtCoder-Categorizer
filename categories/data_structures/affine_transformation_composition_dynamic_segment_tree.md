# Dynamic Segment Tree

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Dynamic Segment Tree`

## Description
This topic focuses on dynamic segment tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Linear transformations compose associatively: f_R(f_L(x)) = a_R * (a_L * x + b_L) + b_R = (a_R * a_L) * x + (a_R * b_L + b_R). Because only at most M distinct machines are ever updated, coordinate compression reduces the pipeline to size <= M.
- Common Reductions: Coordinate-compress updated box positions up to 10^12 and maintain compositions of affine transformations f(x) = a * x + b using a Segment Tree, tracking global minimum and maximum flavor across all M updates in O(M log M).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc008_4`](../../analysis/AtCoder-arc008_4.md) | タコヤキオイシクナール | 2430 | Coordinate-compress updated box positions up to 10^12 and maintain compositions of affine transformations f(x) = a * x +... |
