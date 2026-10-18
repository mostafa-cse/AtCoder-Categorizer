# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Baggage weights and person capacities are integers in $[1, 5]$. Larger weights have strictly fewer container choices. Assigning weights from 5 down to 1 greedily to the tightest fitting available containers maximizes flexibility for smaller weights, with weight 1 items simply requiring total remaining capacity $\ge A_1$.
- Common Reductions: Determine if baggages of weights $1..5$ can be carried by people of capacities $1..5$. Strict greedy allocation matches items from weight 5 down to 1 to the tightest fitting available containers in $O(1)$ per testcase.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc226_g`](../../analysis/AtCoder-abc226_g.md) | G. The baggage | 2373 | Determine if baggages of weights $1..5$ can be carried by people of capacities $1..5$. Strict greedy allocation matches ... |
