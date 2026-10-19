# Matrix Exponentiation

**Taxonomy Path**: `Math` > `Matrices` > `Matrix Exponentiation`

## Description
This topic focuses on matrix exponentiation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Two consecutive normal steps advance the state vector by T = M_even * M_odd = [[1, 1], [1, 2]], identical to the Fibonacci transformation matrix. For any uninhibited interval of length L, the transition is computed in O(log L) via matrix power.
- Common Reductions: Sequences of odd steps summing to S without hitting forbidden prefix sums A_1..A_N. dp[k] = sum_{odd x} dp[k-x] = S_even(k-1) if k odd, and S_odd(k-1) if k even. The state vector [S_odd(k), S_even(k)] updates via 2x2 matrices M_odd and M_even for normal points, and identity matrix I for forbidden points. Consecutive normal intervals are accelerated via 2x2 matrix exponentiation.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc258_h`](../../analysis/AtCoder-abc258_h.md) | Odd Steps | 2708 | Sequences of odd steps summing to S without hitting forbidden prefix sums A_1..A_N. dp[k] = sum_{odd x} dp[k-x] = S_even... |
