# Burnside's Lemma / Polya Enumeration Theorem

**Taxonomy Path**: `Miscellaneous` > `General` > `Burnside's Lemma / Polya Enumeration Theorem`

## Description
This topic focuses on burnside's lemma / polya enumeration theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Burnside's Lemma / Polya Enumeration Theorem, the number of distinct rotational orbits under the cube's rotation group G (of order 24) equals (1/24) * sum_{g in G} Fix(g). The 24 symmetries fall into 5 conjugacy classes according to cycle partitions of the 6 faces:
1. Identity (1 rotation): cycle type 1^6 -> x1 + x2 + x3 + x4 + x5 + x6 = S with xi >= 1. Solutions: C(S - 1, 5).
2. 90-degree and 270-degree face rotations (6 rotations): cycle type 1^2 4^1 -> x1 + x2 + 4*x3 = S with xi >= 1.
3. 180-degree face rotations (3 rotations): cycle type 1^2 2^2 -> x1 + x2 + 2*x3 + 2*x4 = S with xi >= 1.
4. 120-degree vertex rotations (8 rotations): cycle type 3^2 -> 3*x1 + 3*x2 = S with xi >= 1 (non-zero iff 3 | S, count = S/3 - 1).
5. 180-degree edge rotations (6 rotations): cycle type 2^3 -> 2*x1 + 2*x2 + 2*x3 = S with xi >= 1 (non-zero iff 2 | S, count = C(S/2 - 1, 2)).
Each equation sum ci * xi = S with xi >= 1 can be counted using generating functions, binomial coefficients, or closed arithmetic series in O(1) or small loops.
- Common Reductions: Given an integer S, compute the number of ways to write a positive integer on each of the six faces of a cube such that their sum equals S, modulo 998244353. Two cubes are considered identical if one can be rotated in 3D space to match the other.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc198_f`](../../analysis/AtCoder-abc198_f.md) | F - Cube | 2769 | Given an integer S, compute the number of ways to write a positive integer on each of the six faces of a cube such that ... |
