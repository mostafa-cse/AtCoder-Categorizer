# Digit DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Digit DP` > `Digit DP`

## Description
This topic focuses on digit dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If price contains only allowed digits, the answer is directly the number of digits. Otherwise, we must write an expression $X_1 + \dots + X_K =$. The total keystrokes equals the sum of lengths of $X_i$ plus $K$ (for $K-1$ '+' signs and one '=' sign). We iterate over the number of summands $K \in [1, 9]$. Moving from least significant to most significant digits, we maintain the active count of non-zero summands and carry $c$. Transitioning each column uses subsets of allowed digits of size equal to the active count. Dynamic programming over $(carry, active)$ finds the minimal keystroke count and reconstructs the optimal summands.
- Common Reductions: Represent price as a sum of valid numbers using only allowed digits, '+' and '=', minimizing the total button presses.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc005_4`](../../analysis/AtCoder-arc005_4.md) | D - 連射王高橋君 | 2487 | Represent price as a sum of valid numbers using only allowed digits, '+' and '=', minimizing the total button presses.... |
