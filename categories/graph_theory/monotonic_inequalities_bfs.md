# Breadth First Search (BFS)

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Breadth First Search (BFS)`

## Description
This topic focuses on breadth first search (bfs) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each constraint (P, X, Q, Y) implies: if A_P >= X then A_Q >= Y; if A_P >= X+1 then A_Q >= Y+1 (and symmetrically). Maintaining lower bounds L[v] initialized to 1, any increase in L[P] triggers only thresholds <= L[P]. Since lower bounds only increase and each trigger is processed at most once, the propagation terminates at the unique minimal valid sequence, or detects impossibility if any L[v] > M.
- Common Reductions: Minimizing the sum of sequence elements under trichotomy constraints (both <, both =, or both >) reduces to monotonic lower bound propagation via queue-based BFS.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc146_d`](../../analysis/AtCoder-arc146_d.md) | >=< | 2663 | Minimizing the sum of sequence elements under trichotomy constraints (both <, both =, or both >) reduces to monotonic lo... |
