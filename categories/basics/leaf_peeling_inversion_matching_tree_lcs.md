# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If two opposite leaves u and v are paired with P[u] = v and P[v] = u, no simple path can contain both in its common subsequence with mapped values. By peeling leaves in pairs and assigning cross-mappings, we inductively reduce the tree by 2 vertices while preserving the invariant that no path shares more than 1 common vertex with its image.
- Common Reductions: Construct a permutation P of tree vertices that minimizes the maximum LCS between any simple path x and its mapped sequence P(x). A similarity of 1 can always be achieved by iteratively peeling pairs of leaves and swapping their permutation values.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-arc156_c]` | Tree and LCS | 2155 | Construct a permutation P of tree vertices that minimizes the maximum LCS between any simple path x and its mapped seque... |
