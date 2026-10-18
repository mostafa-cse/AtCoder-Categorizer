# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By symmetry of random transpositions on the complete graph $K_N$, the joint distribution of original elements $(A, B)$ ending up at any adjacent positions $(i, i+1)$ partitions into 3 symmetric states: Type 1 (both original $P_i, P_{i+1}$), Type 2 (one original, one outside), and Type 3 (both outside). The probabilities satisfy a 3-state Markov chain solved via matrix exponentiation.
- Common Reductions: Compute the sum of $\sum_{i=1}^{N-1} |P'_i - P'_{i+1}|$ after $M$ uniform random transpositions on permutation $P$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc176_d`](../../analysis/AtCoder-arc176_d.md) | D. Swap Permutation | 2572 | Compute the sum of $\sum_{i=1}^{N-1} |P'_i - P'_{i+1}|$ after $M$ uniform random transpositions on permutation $P$.... |
