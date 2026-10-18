# DSU / Union Find

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `DSU / Union Find`

## Description
This topic focuses on dsu / union find techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each index i with radius A[i], character pairs (i - k, i + k) for k = 1..A[i] must be equal, while if i - A[i] - 1 >= 0 and i + A[i] + 1 < N, the characters at i - A[i] - 1 and i + A[i] + 1 must be strictly unequal. Unite equal indices using DSU, skipping already-united components using a maximum-reach pointer. Create a directed inequality graph between DSU components and assign minimal positive integers greedily via mex/topological order.
- Common Reductions: Constructing a positive integer sequence satisfying given palindrome radii requirements decomposes into equality constraints united via DSU (accelerated via Manacher-style jumps) and inequality constraints colored via a greedy DAG topological sort.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc349_g`](../../analysis/AtCoder-abc349_g.md) | Palindrome Construction | 2655 | Constructing a positive integer sequence satisfying given palindrome radii requirements decomposes into equality constra... |
