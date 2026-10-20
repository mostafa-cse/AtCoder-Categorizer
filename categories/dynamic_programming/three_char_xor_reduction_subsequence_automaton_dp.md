# Substring DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `Substring DP`

## Description
This topic focuses on substring dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Mapping 'A'->1, 'B'->2, 'C'->3, replacing adjacent x != y yields x XOR y. Any contracted character represents a contiguous substring whose XOR sum is that character. Furthermore, a substring can be reduced to a single character v iff its XOR sum is v and it is not a sequence of all identical characters of length > 1. To count distinct resulting strings uniquely without duplicate derivation paths, use a subsequence automaton DP: greedily jump to the first position where the prefix XOR matches pref[i] XOR v.
- Common Reductions: Given a string S of length N consisting of 'A', 'B', 'C', an operation replaces two adjacent different characters with the third character. Find the number of distinct strings that can be obtained modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc110_e`](../../analysis/AtCoder-arc110_e.md) | E - Shorten ABC | 2955 | Given a string S of length N consisting of 'A', 'B', 'C', an operation replaces two adjacent different characters with t... |
