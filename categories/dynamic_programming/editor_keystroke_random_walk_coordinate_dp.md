# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any surviving character in the final string must match s, giving 1 valid key choice, while any character deleted by a subsequent backspace had 2 valid key choices ('0' or '1'). By bitwise symmetry, all 2^|s| strings of length |s| are generated with equal frequency.
- Common Reductions: Count keystroke sequences resulting in string s by observing that symmetry between '0' and '1' renders the actual characters irrelevant, allowing an O(N^2) coordinate DP on string length followed by division by 2^|s| modulo 10^9 + 7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc059_d`](../../analysis/AtCoder-arc059_d.md) | Unhappy Hacking | 2427 | Count keystroke sequences resulting in string s by observing that symmetry between '0' and '1' renders the actual charac... |
