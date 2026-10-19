# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Once depth 2 is entered, every subsequent number can receive a positive sign (+) by appropriately opening/closing inner parentheses around each operator. Depth >= 3 is never needed. Thus, an O(N) DP with exactly 3 states suffices.
- Common Reductions: Maximizing arithmetic expression by inserting parentheses. The effect of nested parentheses after a '-' sign corresponds to 3 negation depth states j in {0, 1, 2}: depth 0 (unflipped), depth 1 (flipped: + becomes -, - becomes +), and depth 2 (double flipped: both + and - become +). Transitions between these 3 states solve the problem in O(N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc066_c`](../../analysis/AtCoder-arc066_c.md) | Addition and Subtraction Hard | 2709 | Maximizing arithmetic expression by inserting parentheses. The effect of nested parentheses after a '-' sign corresponds... |
