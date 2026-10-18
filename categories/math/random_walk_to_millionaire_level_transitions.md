# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because expectation is linear, knowing $E[1], E[X], E[X^2]$ at each vertex at step $t$ completely determines $E[1], E[X], E[X^2]$ at step $t + 1$. The transitions from all incoming edges average the state vectors, and applying the local level increment $(X + 1)$ shifts $E[X^2] \leftarrow E[X^2] + 2E[X] + E[1]$.
- Common Reductions: A token starts at vertex 1 with level $X = 0$. At each step, it moves uniformly at random to an adjacent vertex $v$. If $C_v = 0$, $X \leftarrow X + 1$. If $C_v = 1$, level is unchanged and you receive $X^2$ money. Track the state vector of expected values $(E[1], E[X], E[X^2])$ at each vertex across $K$ steps. When moving to a vertex with $C_v = 0$, expanding $(X + 1)^2 = X^2 + 2X + 1$ linearly transforms the expected values. Accumulate expected money reward whenever visiting $C_v = 1$ vertices.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc277_g`](../../analysis/AtCoder-abc277_g.md) | G. Random Walk to Millionaire | 2491 | A token starts at vertex 1 with level $X = 0$. At each step, it moves uniformly at random to an adjacent vertex $v$. If ... |
