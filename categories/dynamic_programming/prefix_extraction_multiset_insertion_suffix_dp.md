# Substring DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `Substring DP`

## Description
This topic focuses on substring dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any reachable string consists of a suffix of S, say S[i ... |S|], combined with some counts of '0's and '1's harvested into the pool from the consumed prefix. To avoid overcounting strings that can be formed in multiple ways, establish a canonical parsing: greedily match characters from the suffix S[i...] whenever possible, and only draw from the pool (c0, c1) when forced. Reachable configurations (i, c0, c1) are found via forward DP, and distinct strings are counted via backward DP.
- Common Reductions: Given a binary string S, repeatedly remove the first 2 characters, save one to a multiset pool, and optionally insert characters from the pool anywhere. Count the number of distinct reachable strings modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc046_d`](../../analysis/AtCoder-agc046_d.md) | D. Secret Passage | 2911 | Given a binary string S, repeatedly remove the first 2 characters, save one to a multiset pool, and optionally insert ch... |
