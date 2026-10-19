# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In S + S^R, any substring of length N can be extracted. The best first move maximizes the contiguous block of minimum characters c_min ending at the suffix. On subsequent operations, appending S^R places a reversed run of c_min adjacent to the existing run, doubling the consecutive sequence of c_min with each operation (L -> 2L). After at most ceil(log2 N) operations, the entire string becomes all c_min.
- Common Reductions: Given string S of length N, an operation replaces S with a length-N substring of S + S^R. Find the lexicographically smallest string after K operations. The optimal strategy identifies the minimal character c_min, uses the first operation to create the longest contiguous run of c_min at the suffix, and each subsequent operation doubles the length of this run by reversal and concatenation, rapidly saturating the string within log2(N) steps.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc037_e`](../../analysis/AtCoder-agc037_e.md) | Reversing and Concatenating | 2667 | Given string S of length N, an operation replaces S with a length-N substring of S + S^R. Find the lexicographically sma... |
