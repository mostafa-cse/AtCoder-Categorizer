# Eulerian Path and Cycle

**Taxonomy Path**: `Graph Theory` > `Eulerian Path` > `Eulerian Path and Cycle`

## Description
This topic focuses on eulerian path and cycle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If G already has an Eulerian circuit, answer is N. Otherwise, each connected component S requires max(1, sum_{v in S} max(0, in[v] - out[v])) trails. Total trails across all components gives minimum modifications, yielding max matching count N - sum trails.
- Common Reductions: N - 1 swaps of (i, j) with i < j generate precisely all single-cycle permutations of length N. In graph G with edges A_i -> B_i, making A_k = B_k corresponds to decomposing G into the minimum number of directed trails so that edges can form a single Eulerian circuit.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc220_b`](../../analysis/AtCoder-arc220_b.md) | B. Incomplete Shuffle | 2199 | N - 1 swaps of (i, j) with i < j generate precisely all single-cycle permutations of length N. In graph G with edges A_i... |
