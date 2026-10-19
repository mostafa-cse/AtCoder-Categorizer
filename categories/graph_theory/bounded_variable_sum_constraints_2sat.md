# System Of Difference Constraints

**Taxonomy Path**: `Graph Theory` > `Satisfiability` > `System Of Difference Constraints`

## Description
This topic focuses on system of difference constraints techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since M is small (M <= 100), define boolean variables P(i, v) representing the proposition (x_i >= v) for 1 <= v <= M. Natural implications enforce ordering: P(i, v) => P(i, v-1). A constraint x_i + x_j <= S translates to: if x_i >= v then x_j <= S - v, which means P(i, v) => not P(j, S - v + 1). Similarly, x_i + x_j >= S translates to: not P(i, v) => P(j, S - v + 1). All constraints are 2-SAT clauses! This yields a 2-SAT instance with O(N * M) variables.
- Common Reductions: Given N integer variables x_i in [0, M] and Q constraints of the form x_i + x_j <= S or x_i + x_j >= S, find a valid integer assignment or report none exists.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc277_h`](../../analysis/AtCoder-abc277_h.md) | Ex. Constrained Sums | 2917 | Given N integer variables x_i in [0, M] and Q constraints of the form x_i + x_j <= S or x_i + x_j >= S, find a valid int... |
