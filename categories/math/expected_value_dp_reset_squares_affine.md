# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If M consecutive squares are reset squares, the game cannot terminate (output -1). For each state i, the expected steps to finish satisfies E[i] = 1 + (1/M) sum_{d=1}^M E[i+d]. Landing on a reset square gives E[i] = E[0]. Since the recurrence is linear, every state can be expressed as E[i] = a_i * E[0] + b_i. Sliding window sums compute coefficients in O(1) backwards, and E[0] is solved directly from E[0] = a_0 * E[0] + b_0.
- Common Reductions: Compute the expected number of turns to reach square >= N on a 1D board with dice rolls 1..M, where landing on designated trap squares resets Takahashi back to square 0. Express each state expected value as an affine function of E[0] and maintain sliding window sums.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc189_f]` | Sugoroku2 | 2154 | Compute the expected number of turns to reach square >= N on a 1D board with dice rolls 1..M, where landing on designate... |
