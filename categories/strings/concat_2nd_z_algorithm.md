# Z Algorithm

**Taxonomy Path**: `Strings` > `String Matching` > `Z Algorithm`

## Description
This topic focuses on z algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The first lexicographical concatenation A_1 is obtained by sorting the strings according to the comparator X + Y < Y + X. Comparing X + Y and Y + X naively takes O(|X| + |Y|), which can TLE (O(N * |S_i|)). However, using the Z-algorithm array Z_X of each string X, we can compare X + Y and Y + X in O(min(|X|, |Y|)), allowing the full sort in O(sum(|S_i|) log N). Once sorted as S'_1, ..., S'_N: if any adjacent pair has S'_i + S'_{i+1} == S'_{i+1} + S'_i, swapping them yields the identical minimal string, so A_2 = A_1. Otherwise, no adjacent pairs are identical, so A_2 must be the smaller of swapping the last two strings (S'_N, S'_{N-1}) or swapping the last three (S'_{N-1}, S'_{N-2}, S'_N).
- Common Reductions: Given N strings S_i with total length sum(|S_i|) <= 10^6, consider all N! concatenations S_{P_1} S_{P_2} ... S_{P_N} sorted in lexicographical order. Output the second lexicographically smallest string A_2.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc434_f`](../../analysis/AtCoder-abc434_f.md) | I. Concat (2nd) | 2600 | Given N strings S_i with total length sum(|S_i|) <= 10^6, consider all N! concatenations S_{P_1} S_{P_2} ... S_{P_N} sor... |
