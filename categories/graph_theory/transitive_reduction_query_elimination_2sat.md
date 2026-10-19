# 2 SAT

**Taxonomy Path**: `Graph Theory` > `Satisfiability` > `2 SAT`

## Description
This topic focuses on 2 sat techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A query (u, v) is redundant at step t iff there exists a third element w such that (u, w) and (w, v) were both queried earlier and P_w lies strictly between P_u and P_v. To avoid redundancy, for all such w, P_w must NOT lie between P_u and P_v. That is, (P_u < P_w and P_v < P_w) or (P_w < P_u and P_w < P_v), which means (P_u < P_w) <=> (P_v < P_w). This constraint directly establishes 2-SAT equivalence clauses between the boolean orientation variables of earlier edges.
- Common Reductions: Given a sequence of all N*(N-1)/2 comparison queries on a hidden permutation, count the number of permutations where none of the first K queries are redundant (derivable by transitivity from earlier queries).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc059_c`](../../analysis/AtCoder-agc059_c.md) | C. Guessing Permutation for as Long as Possible | 2905 | Given a sequence of all N*(N-1)/2 comparison queries on a hidden permutation, count the number of permutations where non... |
