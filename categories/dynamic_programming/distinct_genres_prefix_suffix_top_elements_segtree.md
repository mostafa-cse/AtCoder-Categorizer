# Knapsack and Basic Dynamic Programming

**Taxonomy Path**: `Dynamic Programming (DP)` > `Intro to DP` > `Knapsack and Basic Dynamic Programming`

## Description
This topic focuses on knapsack and basic dynamic programming techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Choosing 6 problems i1 < i2 < i3 < i4 < i5 < i6 where Div 2 (i1..i4) and Div 1 (i3..i6) have distinct genres separates at the shared boundary (i3, i4). In the prefix before i3, only the top 4 genre-distinct elements matter; similarly in the suffix after i4. Fixing the genre c of i4, the prefix best values M(x) undergo only O(1) transitions across all c, maintainable dynamically in a segment tree.
- Common Reductions: Partition 6 problems into prefix (i1, i2), pivot pair (i3, i4), and suffix (i5, i6). Forbidding the 2 pivot genres reduces prefix and suffix choices to top-4 distinct genre candidates, dynamically maintained in a segment tree in O(N log N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc447_g`](../../analysis/AtCoder-abc447_g.md) | G. Div. 1 & Div. 2 | 2391 | Partition 6 problems into prefix (i1, i2), pivot pair (i3, i4), and suffix (i5, i6). Forbidding the 2 pivot genres reduc... |
