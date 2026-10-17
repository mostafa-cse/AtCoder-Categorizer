# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By symmetry, every starting vertex i contributes identically to the total sum. For vertex 1, a walk v_1, ..., v_l repeats for the first time when f(v_l) loops back to some v_r (1 <= r <= l). Elements appearing exactly once are v_1, ..., v_{r-1}, totaling r - 1 elements. Summing r - 1 over all l loopback positions yields l(l - 1) / 2. Each path of length l has P(N - 1, l - 1) * N^{N - l} completions, leading to an O(N) closed summation.
- Common Reductions: Compute the sum over all N^N functional graphs f: [1, N] -> [1, N] of the number of elements that appear exactly once in the walk starting at each vertex i.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc284_g`](../../analysis/AtCoder-abc284_g.md) | Only Once | 2218 | Compute the sum over all N^N functional graphs f: [1, N] -> [1, N] of the number of elements that appear exactly once in... |
