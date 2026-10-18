# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A single pass of bubble sort produces a permutation $P'$ ending with $N$ with fiber size $2^{k-1}$, where $k$ is the number of prefix maxima of $P'$. Placing elements from left to right, each new prefix maximum multiplies the weight by 2. The number of available free elements $\le j$ depends only on $j$ and the number of elements placed so far.
- Common Reductions: Count permutations $P$ whose single-pass bubble sort output $P'$ matches sequence $Q$ on all non-(-1) entries.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc187_c`](../../analysis/AtCoder-arc187_c.md) | C. 1 Loop Bubble Sort | 2574 | Count permutations $P$ whose single-pass bubble sort output $P'$ matches sequence $Q$ on all non-(-1) entries.... |
