# Functional Graphs

**Taxonomy Path**: `Miscellaneous` > `General` > `Functional Graphs`

## Description
This topic focuses on functional graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Deleting the last B and stripping trailing Rs leaves S = R^{c_B} B ... R^{c_1} B. The final pile corresponds to partitioning the R chips into B blocks of sizes (l_1, ..., l_B) extracted greedily. Sorting l into descending order l'_1 >= ... >= l'_B >= 0, dominance inequalities require sum_{q=0}^p l'_q >= sum_{q=0}^p c_q for all p, where l'_0 = R - sum l'_i. Equivalently, the suffix sums of l' are bounded by the suffix sums of c. Counting permutations with multiplicity factor B! / prod(f_i!) reduces to an integer partition DP in O(R^3) time.
- Common Reductions: Given an N-character string S of R and B chips with square N guaranteed to be blue, chips at square i are repeatedly merged onto higher-indexed blue squares j. Determine the number of distinct color sequences in the final stack at square N modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc064_d`](../../analysis/AtCoder-agc064_d.md) | D - Red and Blue Chips | 2808 | Given an N-character string S of R and B chips with square N guaranteed to be blue, chips at square i are repeatedly mer... |
