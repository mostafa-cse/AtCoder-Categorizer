# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: First, the minimum side length L is determined by sorting pairwise coordinate differences or binary searching with a 2D sliding window. Once L is fixed, any valid subset of K points must have Chebyshev bounding square of side length exactly L. For each candidate position of an L x L square, we use inclusion-exclusion across the 4 boundaries (left, right, bottom, top) to count subsets of size K that span both horizontally by L and vertically by L.
- Common Reductions: Given N points in 2D, find the minimum side length L of an axis-aligned bounding square that can cover at least K points, and count the number of subsets of K points whose Chebyshev bounding square has side length exactly L, modulo 10^9+7.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc032_4`](../../analysis/AtCoder-arc032_4.md) | D - アットコーダーモンスターズ | 2861 | Given N points in 2D, find the minimum side length L of an axis-aligned bounding square that can cover at least K points... |
