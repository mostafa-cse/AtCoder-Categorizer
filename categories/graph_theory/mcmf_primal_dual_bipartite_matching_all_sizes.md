# Min Cost Max Flow (MCMF)

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Min Cost Max Flow (MCMF)`

## Description
This topic focuses on min cost max flow (mcmf) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Universities (<= 150) form the left partition and subjects (<= 150) form the right partition. For each pair (u, v), only retain the maximum power person. By negating costs (or setting cost = BIG - C_{u, v}), each unit of augmented flow from Source to Sink adds exactly 1 person while maximizing power. The algorithm stops when no augmenting path exists.
- Common Reductions: Select a dream team of size k maximizing total power such that all universities and subjects are distinct. Formulated as maximum weight bipartite matching solved via successive shortest path Min-Cost Max-Flow (Primal-Dual) across all matching sizes k.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc247_g]` | Dream Team | 2159 | Select a dream team of size k maximizing total power such that all universities and subjects are distinct. Formulated as... |
