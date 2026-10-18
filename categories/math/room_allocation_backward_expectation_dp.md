# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By linearity of expectation, the expected total penalty is the sum of expectations of state transitions. Because choices are uniform across available empty rooms, the probability distribution depends on the number of remaining rooms and the current cluster configurations. We formulate a backward dynamic programming over the number of occupied rooms and configuration states.
- Common Reductions: N people enter rooms sequentially. Person i chooses an empty room uniformly at random among available rooms. Compute the expected value of the penalty cost across all possible random room assignment outcomes.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-code_festival_final_h`](../../analysis/AtCoder-code_festival_final_h.md) | H. 部屋割り (Room Allocation) | 2535 | N people enter rooms sequentially. Person i chooses an empty room uniformly at random among available rooms. Compute the... |
