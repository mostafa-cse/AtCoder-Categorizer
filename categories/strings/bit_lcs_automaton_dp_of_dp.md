# Bit LCS

**Taxonomy Path**: `Strings` > `Longest Common Subsequence (LCS)` > `Bit LCS`

## Description
This topic focuses on bit lcs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In the standard dynamic programming table for LCS between S and a prefix of T, adjacent DP entries satisfy 0 <= dp[i] - dp[i-1] <= 1. Thus, the DP state against S is fully encoded by the binary difference vector Delta in {0, 1}^N (a bitmask of 2^N states). Precomputing the deterministic automaton transition next_mask = trans[mask][c] for all 2^N masks and 26 characters turns the problem into counting paths of length M in the LCS DFA.
- Common Reductions: Count the number of lowercase strings of length M whose longest common subsequence with a given string S of length N <= 10 has length exactly k, for all 0 <= k <= N.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc391_g`](../../analysis/AtCoder-abc391_g.md) | Many LCS | 2247 | Count the number of lowercase strings of length M whose longest common subsequence with a given string S of length N <= ... |
