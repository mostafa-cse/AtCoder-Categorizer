# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A string lies on a shortest swap path between S and T iff the cumulative count of ones at every prefix p is bounded within [low[p], high[p]] = [min(pref_S[p], pref_T[p]), max(pref_S[p], pref_T[p])]. Maximizing beauty (n + m - 1 - transitions) is equivalent to minimizing the number of alternating runs of 0s and 1s. This maps to finding a path with minimum turns in a 2D corridor from (0,0) to (n,m). Greedily ray-shooting horizontally and vertically as far as possible from the current position achieves the theoretical minimum turns.
- Common Reductions: Maximize the beauty (number of adjacent identical characters) of a binary string lying on the shortest swap path between two given binary strings S and T.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc132_d`](../../analysis/AtCoder-arc132_d.md) | Between Two Binary Strings | 2221 | Maximize the beauty (number of adjacent identical characters) of a binary string lying on the shortest swap path between... |
