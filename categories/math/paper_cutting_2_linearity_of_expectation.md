# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The process terminates immediately when any of the $S = (r_2 - r_1) + (c_2 - c_1)$ separating cut lines between the two black squares is chosen. A cut line $L$ outside the bounding box at distance $d$ from the box is executed if and only if it is chosen before all $d - 1$ intervening lines and all $S$ terminating lines. Thus, among these $(d - 1) + 1 + S = d + S$ lines, $L$ must be chosen first, which occurs with probability $\frac{1}{d + S}$.
- Common Reductions: A rectangular grid $H \times W$ contains two marked black squares at $(r_1, c_1)$ and $(r_2, c_2)$. Cut lines are chosen uniformly at random without replacement from the remaining lines. After each cut, the piece not containing both black squares is discarded. The process halts when a cut separates the two black squares. By linearity of expectation, the expected number of cuts is $1 + \sum_{L} \mathbb{P}(L \text{ is cut before termination})$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc114_e`](../../analysis/AtCoder-arc114_e.md) | E. Paper Cutting 2 | 2514 | A rectangular grid $H \times W$ contains two marked black squares at $(r_1, c_1)$ and $(r_2, c_2)$. Cut lines are chosen... |
