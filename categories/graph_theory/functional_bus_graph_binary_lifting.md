# Binary Lifting and LCA

**Taxonomy Path**: `Graph Theory` > `Lowest Common Ancestor (LCA)` > `Binary Lifting and LCA`

## Description
This topic focuses on binary lifting and lca techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because a person arriving at city $B_i$ at time $T_i$ must take the earliest departing bus with departure time $\ge T_i$, each bus $i$ has at most one deterministic successor bus. The bus transition system forms a directed functional forest.
- Common Reductions: Buses connect cities deterministically at discrete times. Each bus departure transitions to a unique subsequent bus, forming a functional graph. Binary lifting over bus transitions answers position queries at time $Z$ in $O(\log M)$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc212_f`](../../analysis/AtCoder-abc212_f.md) | F. Greedy Takahashi | 2332 | Buses connect cities deterministically at discrete times. Each bus departure transitions to a unique subsequent bus, for... |
