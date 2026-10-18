# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: An operation '101' $\to$ '010' consumes a '0' flanked by '1's. When blocks of consecutive ones are separated by single zeros, each operation merges adjacent groups or transfers ones. Specifically, the string decomposes into maximal runs of the form $1^a 0 1^b 0 1^c \dots$. For any subsegment of ones separated by single zeros, an interval DP or linear DP tracking active ones determines the maximum operations achievable without interfering with adjacent blocks.
- Common Reductions: Maximize the number of operations replacing substring '101' with '010' in a binary string of length $N$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-code_festival_2017_qualb_d`](../../analysis/AtCoder-code_festival_2017_qualb_d.md) | D - 101 to 010 | 2499 | Maximize the number of operations replacing substring '101' with '010' in a binary string of length $N$.... |
