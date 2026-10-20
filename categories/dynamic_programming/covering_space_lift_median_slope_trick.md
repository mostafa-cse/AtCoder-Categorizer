# Slope Trick

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Slope Trick`

## Description
This topic focuses on slope trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because adjacent elements never cross, their relative winding number on the circle is invariant. Lift B to the universal covering space (integers Z) by setting C_0 = B_0 and uniquely determining C_i such that |C_i - C_{i-1}| < M and sgn(C_i - C_{i-1}) = sgn(A_i - A_{i-1}). Any global rotation by k * M preserves winding. The total cost is \sum |(A_i + k * M) - C_i|, which is a convex piecewise linear function minimized at the median of C_i - A_i via Slope Trick.
- Common Reductions: Transform array A into B modulo M using cyclic +/-1 operations without adjacent elements ever being equal. Minimize total operations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc182_d`](../../analysis/AtCoder-arc182_d.md) | D - Increment Decrement Again | 2992 | Transform array A into B modulo M using cyclic +/-1 operations without adjacent elements ever being equal. Minimize tota... |
