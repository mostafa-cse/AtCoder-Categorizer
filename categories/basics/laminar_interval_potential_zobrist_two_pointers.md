# Two Pointers

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Two Pointers`

## Description
This topic focuses on two pointers techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A subset of trips on a line has no conflicts iff: (1) all forward trips form a laminar family, (2) all reverse trips form a laminar family, and (3) no forward trip and reverse trip share an endpoint or overlap in conflicting direction. The validity of a range [L, R] is monotonic. We maintain the laminar family condition and endpoint disjointness using two pointers on R, checking validity using Zobrist hashing and a Binary Indexed Tree (BIT) to detect crossing intervals in O(log N).
- Common Reductions: Given M directed trips (S_i, T_i) along a linear road of N cities, count pairs (L, R) (1 <= L <= R <= M) such that the subset of trips with indices in [L, R] can be executed simultaneously without traffic conflict.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc196_d`](../../analysis/AtCoder-arc196_d.md) | D - Roadway | 2973 | Given M directed trips (S_i, T_i) along a linear road of N cities, count pairs (L, R) (1 <= L <= R <= M) such that the s... |
