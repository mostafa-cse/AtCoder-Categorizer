# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each digit d in 1..9, the reachable columns from row mask R are the union of columns containing d across rows in R. Similarly, reachable rows from column mask C are the union of rows containing d across columns in C. There are at most 2^{10} = 1024 states, making DP over 2N steps extremely fast.
- Common Reductions: Counting distinct 2N-digit sequences produced by Takahashi (row moves) and Aoki (column moves) on an H x W grid (H, W <= 10). Modeled as a DFA using the subset construction (powerset automaton) where states at even steps are row subsets R in [1, 2^H - 1] and at odd steps are column subsets C in [1, 2^W - 1].

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc228_g`](../../analysis/AtCoder-abc228_g.md) | Digits on Grid | 2711 | Counting distinct 2N-digit sequences produced by Takahashi (row moves) and Aoki (column moves) on an H x W grid (H, W <=... |
