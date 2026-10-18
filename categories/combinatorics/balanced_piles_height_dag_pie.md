# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let the maximum pile height increase from $0$ to $H$. Every time the minimum pile height must be raised to avoid exceeding difference $D$, we apply the Principle of Inclusion and Exclusion (PIE) over which piles reached height $h$. The transitions reduce to a linear recurrence on height $h$ with constant multiplier $W = \sum_{i=1}^N i!$, maintained via a sliding window of width $D$.
- Common Reductions: Count sequences of $H$ pile additions across $N$ piles such that at all times, the difference between the maximum and minimum pile heights is at most $D$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-diverta2019_2_e`](../../analysis/AtCoder-diverta2019_2_e.md) | E - Balanced Piles | 2543 | Count sequences of $H$ pile additions across $N$ piles such that at all times, the difference between the maximum and mi... |
