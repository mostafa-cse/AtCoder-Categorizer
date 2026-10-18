# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The relative order of any two strings A and B in an optimal concatenation must satisfy the comparator A + B < B + A. Sorting all strings by this comparator establishes the total order of chosen cards.
- Common Reductions: Given N strings S_i, choose K cards and concatenate them in any order to form the lexicographically smallest possible string.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc225_f`](../../analysis/AtCoder-abc225_f.md) | F. String Cards | 2612 | Given N strings S_i, choose K cards and concatenate them in any order to form the lexicographically smallest possible st... |
