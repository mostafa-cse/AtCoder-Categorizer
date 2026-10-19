# Aliens Trick / WQS Binary Search

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `Aliens Trick / WQS Binary Search`

## Description
This topic focuses on aliens trick / wqs binary search techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Choosing red lamps is equivalent to selecting items from an array where adjacent selections lose their mutual boundary reward. The optimal score as a function of the number of chosen red lamps k is strictly concave. This allows applying the Aliens Trick (WQS Binary Search / Lagrangian relaxation): introduce a penalty lambda per chosen red lamp, solve the unconstrained maximum weight problem with O(N) DP, and binary search lambda to find the slope matching R.
- Common Reductions: Given N lamps in a line with adjacent difference rewards A_i, choose exactly R lamps to color red and N - R to color blue to maximize total reward.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc218_h`](../../analysis/AtCoder-abc218_h.md) | H - Red and Blue Lamps | 2805 | Given N lamps in a line with adjacent difference rewards A_i, choose exactly R lamps to color red and N - R to color blu... |
