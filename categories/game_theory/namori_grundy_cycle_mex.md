# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The graph consists of a directed cycle with attached directed trees rooted along the cycle. Vertices with out-degree 0 (sinks) have Grundy value 0. In-tree vertices have uniquely determined Grundy values by bottom-up mex evaluation. For the cycle, each cycle vertex c_i has a set of values from its non-cycle predecessors. There are at most 2 candidate Grundy values for any cycle vertex. Testing both candidates and verifying cycle consistency resolves the problem in O(N).
- Common Reductions: Given a directed functional graph where each vertex has out-degree 1, determine if there exists an assignment of non-negative integers g_u such that g_u = mex{g_v | u -> v}.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc079_d`](../../analysis/AtCoder-arc079_d.md) | F - Namori Grundy | 2636 | Given a directed functional graph where each vertex has out-degree 1, determine if there exists an assignment of non-neg... |
