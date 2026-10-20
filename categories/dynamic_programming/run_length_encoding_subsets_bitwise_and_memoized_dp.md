# Substring DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `Substring DP`

## Description
This topic focuses on substring dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Every valid encoding decodes to a unique string T. An encoding is valid for some T subseteq S if and only if its decoded string is pointwise <= S. An encoding decomposes uniquely into irreducible blocks E_1 E_{rest}. If E_1 is (P x K) covering length L x K, then P must be an encoding of a subset of the bitwise AND of the K chunks of length L. The number of reachable strings under repeated bitwise AND and suffix cuts is remarkably small (< 300 states for N <= 100), allowing memoized recursion.
- Common Reductions: Given a binary string S, count the total number of valid run-length encodings (using single characters, concatenation, and (P x K) repeats) across all subsets T subseteq S.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc020_e`](../../analysis/AtCoder-agc020_e.md) | E. Encoding Subsets | 2944 | Given a binary string S, count the total number of valid run-length encodings (using single characters, concatenation, a... |
