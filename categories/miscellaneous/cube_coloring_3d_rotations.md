# Burnside's Lemma / Polya Enumeration Theorem

**Taxonomy Path**: `Miscellaneous` > `General` > `Burnside's Lemma / Polya Enumeration Theorem`

## Description
This topic focuses on burnside's lemma / polya enumeration theorem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In every valid cube of 6 distinct tiles, exactly one tile has the minimum index i. Rotating the cube so tile i is on the top face in rotation 0 is unique. Iterating over bottom tile j (with j > i) and its 4 rotations fixes the 4 corner colors of all 4 side faces. Side faces are counted independently via a precomputed frequency map of canonical tile rotations, yielding exact O(N^2) enumeration.
- Common Reductions: Count distinct 3D cubes formed by 6 distinct oriented square tiles up to the 24 rotations of the octahedral group by canonically fixing the tile with the minimal index on the top face in standard orientation, uniquely fixing all remaining face requirements.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc062_c`](../../analysis/AtCoder-arc062_c.md) | Building Cubes with AtCoDeer | 2655 | Count distinct 3D cubes formed by 6 distinct oriented square tiles up to the 24 rotations of the octahedral group by can... |
