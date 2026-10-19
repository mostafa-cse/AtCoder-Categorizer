# Sum Over Subsets DP (SOS DP)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Sum Over Subsets DP (SOS DP)`

## Description
This topic focuses on sum over subsets dp (sos dp) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Define vertex potentials b_v = XOR_{e in incident(v)} a_e. A path XOR operation with x between u and v changes only b_u <- b_u ^ x and b_v <- b_v ^ x, preserving total XOR sum b_v = 0. The problem reduces to partitioning non-zero potentials into the maximum number of zero-XOR subsets. Equal values are greedily paired up, leaving at most 15 distinct values. Partitioning the remaining <= 15 values is solved via SOS DP / subset DP on 2^15 states.
- Common Reductions: Given a tree where edges have weights in [0, 15], an operation XORs all edges on any simple path with x. Find the minimum number of operations to make all edge weights 0.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-apc001_f`](../../analysis/AtCoder-apc001_f.md) | F - XOR Tree | 2865 | Given a tree where edges have weights in [0, 15], an operation XORs all edges on any simple path with x. Find the minimu... |
