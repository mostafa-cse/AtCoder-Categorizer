# Games on Arbitrary Graphs

**Taxonomy Path**: `Game Theory` > `Graph Games` > `Games on Arbitrary Graphs`

## Description
This topic focuses on games on arbitrary graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The game terminates when the graph is partitioned into two complete components of sizes n and N-n. Total edges is N(N-1)/2 - n(N-n). If N is odd, n(N-n) is always even, so total moves has fixed parity N(N-1)/2 - M. If N is even, parity depends on whether initial components containing 1 and N have same or different parity.
- Common Reductions: Two players alternate adding an edge such that vertex 1 and vertex N remain disconnected. Normal play convention. Determine whether First or Second wins under optimal play.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc105_e`](../../analysis/AtCoder-arc105_e.md) | E. Keep Graph Disconnected | 2615 | Two players alternate adding an edge such that vertex 1 and vertex N remain disconnected. Normal play convention. Determ... |
