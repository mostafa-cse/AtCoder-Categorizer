# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The vehicle moves towards the destination if distance decreases: x -> |x - d| if d < 2x, else x stays unchanged. Rewriting d_q allows the witch to set the distance entering step q+1 to any integer y in [0, X_{q-1}]. By backward simulation, let req[i] be the minimum distance before step i that avoids reaching 0 after steps i..N: req[N+1] = 1, and req[i] = req[i+1] if d_i >= 2*req[i+1] else req[i+1] + d_i. The witch succeeds iff X_{q-1} >= req[q+1].
- Common Reductions: Determining whether rewriting the q-th step in a vehicle's sequence of greedy moves can prevent reaching distance 0 decomposes into forward position tracking and backward threshold reachability DP.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc072_c`](../../analysis/AtCoder-arc072_c.md) | Alice in linear land | 2655 | Determining whether rewriting the q-th step in a vehicle's sequence of greedy moves can prevent reaching distance 0 deco... |
