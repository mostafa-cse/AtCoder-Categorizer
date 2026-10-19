# Permutations, Combinations and Basic Counting Problems

**Taxonomy Path**: `Basics` > `Basic Counting` > `Permutations, Combinations and Basic Counting Problems`

## Description
This topic focuses on permutations, combinations and basic counting problems techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Work backwards from the operation sequence. Simulating greedy deletion on the identity sequence yields an upper bound vector U_1, U_2, ..., U_{A-B}. A set {x_1 < x_2 < ... < x_{A-B}} is achievable if and only if x_k <= U_k for all k. Counting such tuples is a standard O(A^2) prefix-sum DP.
- Common Reductions: A sequence of A insertions and B deletions of the maximum element produces an (A - B)-element multiset. By simulating the greedy envelope of elements that can survive the deletion schedule, valid multisets are characterized by prefix domination conditions equivalent to Dyck-path counting solvable by dynamic programming in O(A^2) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc127_e`](../../analysis/AtCoder-arc127_e.md) | Priority Queue | 2678 | A sequence of A insertions and B deletions of the maximum element produces an (A - B)-element multiset. By simulating th... |
