# Two Pointers

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Two Pointers`

## Description
This topic focuses on two pointers techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Eating 1 candy of value x is equivalent to pairing x with a phantom candy of value 0. If we add Z phantom zeros such that N + Z = 2M is even, every step is a pair of candies. To minimize max(pair_sum) - min(pair_sum) in an array of 2M numbers, the optimal pairing is always the extreme pairing: sort the array and pair the i-th smallest with the i-th largest using two pointers. Since N <= 5000, we can iterate over the number of zeros Z in 0..N such that N + Z is even, pair via two pointers, and find the minimum span.
- Common Reductions: You have N candies with tastiness values A_1, ..., A_N. In each step, you can eat either 1 candy or 2 candies. Minimize max(step_sum) - min(step_sum) across all steps.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc121_d`](../../analysis/AtCoder-arc121_d.md) | D - 1 or 2 | 2784 | You have N candies with tastiness values A_1, ..., A_N. In each step, you can eat either 1 candy or 2 candies. Minimize ... |
