# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each position $i$, $|P_i - i| < X$ confines banned values to a sliding window $[i - X + 1, i + X - 1]$ of width $2X - 1 \le 9$. By Principle of Inclusion-Exclusion, the answer is $\sum_{k=0}^N (-1)^k ways(k) (N-k)!$, where $ways(k)$ is the number of ways to choose $k$ non-conflicting banned placements computed via DP over the $2^{2X-1}$ mask of used window values.
- Common Reductions: Count permutations with $|P_i - i| \ge X$ ($X \le 5, N \le 100$). Inclusion-exclusion on banned positions uses profile DP tracking a sliding bitmask of width $2X - 1 \le 9$ of used values, running in $O(N^2 2^{2X-1})$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc309_g`](../../analysis/AtCoder-abc309_g.md) | G. Ban Permutation | 2372 | Count permutations with $|P_i - i| \ge X$ ($X \le 5, N \le 100$). Inclusion-exclusion on banned positions uses profile D... |
