# Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)

**Taxonomy Path**: `Geometry` > `Geometry 2D` > `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`

## Description
This topic focuses on points, vectors, transformations, dot products, cross products, precision issues and polar sort(2d) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Allowed movements form a subset of the 8 compass direction vectors. The reachable area after k steps is the Minkowski sum of the allowed vectors. For long distances, optimal paths lie along the boundaries of the 2D cone containing vector (a, b). Decomposing (a, b) as a non-negative linear combination of adjacent cone-generating basis vectors provides the base step count, while parity adjustments and small bounded perturbations handle integer grid constraints.
- Common Reductions: Starting at the origin in 2D space, move to target (a, b) using a given subset of 8 octagonal directions in the minimum number of steps.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc271_h`](../../analysis/AtCoder-abc271_h.md) | Ex. One-digit Movements | 2906 | Starting at the origin in 2D space, move to target (a, b) using a given subset of 8 octagonal directions in the minimum ... |
