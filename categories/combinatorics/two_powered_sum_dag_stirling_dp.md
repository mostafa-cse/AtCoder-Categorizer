# Contribution Technique

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Contribution Technique`

## Description
This topic focuses on contribution technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: An array $A$ is reachable iff its non-zero positions are partitioned into sets $U_v$ corresponding to operations $S_v$ such that the overwrite dependency graph on operations forms a DAG. Running operations in reverse uniquely partitions newly exposed elements at each step, yielding an exact $O(N^3)$ DP parameterized by total exposed elements and the size of the previous layer.
- Common Reductions: Count reachable arrays formed by subset bitwise operations $A_i = \sum_{j \in S} 2^{j-1}$. Reversing the overwrite dependency DAG uniquely layers newly exposed elements, computed via Stirling numbers and $O(N^3)$ layer DP.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc221_b`](../../analysis/AtCoder-arc221_b.md) | B. Two-Powered Sum | 2350 | Count reachable arrays formed by subset bitwise operations $A_i = \sum_{j \in S} 2^{j-1}$. Reversing the overwrite depen... |
