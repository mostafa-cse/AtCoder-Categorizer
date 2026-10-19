# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each turn outcome either eliminates the current customer (upon winning an item) and decrements inventory, or passes the turn to the next customer. When a round finishes, all active customers cycle to the next round with decremented round limit. Memoizing (n, i, rem_items, rem_rounds) computes win probabilities for all players.
- Common Reductions: N customers in line each make K shopping rounds, winning an item with probability 1 / (remaining items + 1). By tracking the number of active customers n, the current customer position i, remaining items, and remaining rounds, state transitions form a finite acyclic DAG solvable by memoized DP in O(N^3 K) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc050_d`](../../analysis/AtCoder-agc050_d.md) | Shopping | 2674 | N customers in line each make K shopping rounds, winning an item with probability 1 / (remaining items + 1). By tracking... |
