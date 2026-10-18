# Prefix XOR

**Taxonomy Path**: `Basics` > `Range Queries Without Updates` > `Prefix XOR`

## Description
This topic focuses on prefix xor techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A partition has all segment XORs equal to X if and only if the prefix XOR at cut points strictly alternates between X and 0. For S == 0 and fixed X != 0, multiple zeros between consecutive occurrences of X can be skipped or chosen, multiplying the transition by the number of intervening zeros in O(1) time.
- Common Reductions: Partition array into segments of equal XOR beauty by analyzing prefix XOR values: if total XOR S != 0, prefix XORs must alternate between S and 0; if total XOR S == 0, either all parts are 0 (2^c subsets) or prefix XORs alternate between X and 0, computable in O(N) using prefix zero counts.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-diverta2019_e`](../../analysis/AtCoder-diverta2019_e.md) | XOR Partitioning | 2423 | Partition array into segments of equal XOR beauty by analyzing prefix XOR values: if total XOR S != 0, prefix XORs must ... |
