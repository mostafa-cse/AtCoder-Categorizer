# Rerooting Technique

**Taxonomy Path**: `Graph Theory` > `More Tree Stuff` > `Rerooting Technique`

## Description
This topic focuses on rerooting technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By tree distance properties, moving across edge (u, v) changes the distance sum by D(u) - D(v) = N - 2 * sz(u), where sz(u) is the subtree size of u directed away from v. The vertex with the maximum D_u must be a leaf (sz(u) = 1). Its parent v must uniquely have D(v) = D(u) - (N - 2 * sz(u)). Processing vertices in descending order of D greedily identifies each parent, accumulating subtree sizes. Finally, verifying the distance sum of the centroid/root on the reconstructed tree confirms correctness.
- Common Reductions: Given N distinct integers D_1, ..., D_N representing the sum of tree distances from each vertex to all other vertices, reconstruct the tree or determine that none exists.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc103_d`](../../analysis/AtCoder-arc103_d.md) | F - Distance Sums on a Tree | 2836 | Given N distinct integers D_1, ..., D_N representing the sum of tree distances from each vertex to all other vertices, r... |
