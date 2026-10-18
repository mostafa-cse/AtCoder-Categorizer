# Maximum Closure Problem

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Closure Problem`

## Description
This topic focuses on maximum closure problem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The continuous relaxation of max-weight independent set subject to W_u + W_v <= 2026 possesses the half-integrality property (Nemhauser-Trotter): basic optimal solutions have W_j in {0, 1013, 2026}. On the bipartite double cover of the graph with source capacities 1013 to u_L, sink capacities 1013 from u_R, and infinity cross edges (u_L -> v_R, v_L -> u_R), max flow equals the min cut, achieving the maximum total weight 2026 * N - min_cut.
- Common Reductions: The integer vertex weight sum under edge bounds W_u + W_v <= 2026 attains its LP bound at half-integers W_j in {0, 1013, 2026}. Solved via Dinic's min cut on the bipartite double cover in O((N + M) sqrt(N)) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc461_g`](../../analysis/AtCoder-abc461_g.md) | G. Graph Problem 2026 | 2391 | The integer vertex weight sum under edge bounds W_u + W_v <= 2026 attains its LP bound at half-integers W_j in {0, 1013,... |
