# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The operation shifts bits right with the new MSB equal to 1 - LSB, which is a negated cyclic shift of string S. A sequence has return period 2d dividing 2N iff N/d is odd and S satisfies S[i+d] = 1 - S[i] for all i. The sequence is completely determined by its prefix of length d.
- Common Reductions: Compute the sum of return periods under negated cyclic bit shifts for all integers k <= X. Any state has period 2d dividing 2N with N/d odd, uniquely determined by its length-d prefix. Counting valid prefixes <= X in O(N) per divisor and applying inclusion-exclusion over odd-quotient divisors solves the problem in O(N d(N)) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc039_c`](../../analysis/AtCoder-agc039_c.md) | C. Division by Two with Something | 2379 | Compute the sum of return periods under negated cyclic bit shifts for all integers k <= X. Any state has period 2d divid... |
