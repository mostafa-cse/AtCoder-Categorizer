# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Use Principle of Inclusion and Exclusion. The forbidden positions (i, P_i) with |P_i - i| = K form disjoint paths in the bipartite placement grid: each path corresponds to residue classes modulo 2K. Placing non-attacking rooks on disjoint paths is equivalent to independent sets / matching on paths. We compute the rook polynomial coefficients dp[i] (ways to choose i forbidden edges) via linear DP across the concatenated disjoint paths, then apply PIE: sum_{i=0}^N (-1)^i dp[i] (N - i)! mod 924844033.
- Common Reductions: Count permutations P of (1, ..., N) such that |P_i - i| != K for all i.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc005_d`](../../analysis/AtCoder-agc005_d.md) | D. ~K Perm Counting | 2943 | Count permutations P of (1, ..., N) such that |P_i - i| != K for all i.... |
