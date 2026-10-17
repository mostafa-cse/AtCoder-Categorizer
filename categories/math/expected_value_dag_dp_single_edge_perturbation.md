# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Expected steps satisfy E[v] = 1 + (1 / deg(v)) sum_{(v, u)} E[u]. Because edges only go forward (s_i < t_i), removing an edge from room v leaves expected values for all rooms > v completely unaffected. To minimize E[v], greedily remove the outgoing edge to the neighbor with maximum expectation max_{(v, u)} E[u], then recompute expected values for rooms < v in reverse topological order in O(M) time.
- Common Reductions: In a DAG with s_i < t_i and exit N, Takahashi moves uniformly at random among outgoing passages. Block at most one passage to minimize expected steps from Room 1 to Room N.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc144_f`](../../analysis/AtCoder-abc144_f.md) | F. Fork in the Road | 2189 | In a DAG with s_i < t_i and exit N, Takahashi moves uniformly at random among outgoing passages. Block at most one passa... |
