# Interactive Problems

**Taxonomy Path**: `Miscellaneous` > `Interactive Problems` > `Interactive Problems`

## Description
This topic focuses on interactive problems techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because all A_i > 0, querying (1, i) for all i >= 2 identifies an extreme endpoint m with maximal range sum (so P_m = 1 or P_m = N). Assuming P_m = 1, querying (m, i) sorts elements along the line, yielding P and differences A_3..A_N. One boundary query finds A_1 and A_2. If P_1 > P_2, invert P_i <- N + 1 - P_i and reverse A.
- Common Reductions: Interactive reconstruction of a permutation P and positive array A from at most 2N range sum queries sum_{i=min(P_s, P_t)}^{max(P_s, P_t)} A_i with P_1 < P_2 guaranteed.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-arc192_c]` | Range Sums 2 | 2158 | Interactive reconstruction of a permutation P and positive array A from at most 2N range sum queries sum_{i=min(P_s, P_t... |
