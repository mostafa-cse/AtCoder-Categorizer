# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: To minimize sum(c_j - a_j), each arriving ball should be matched as early as possible. If it can complete an existing 2-ball pair missing its color, it MUST do so. If not, it should be paired with an existing 1-ball single of a different color. If neither is available, it must start a new single.
- Common Reductions: Greedy prefix matching of 3-color balls minimizing span sum sum(c_j - a_j) with exact state multiplicity counting.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc037_b`](../../analysis/AtCoder-agc037_b.md) | RGB Balls | 2202 | Greedy prefix matching of 3-color balls minimizing span sum sum(c_j - a_j) with exact state multiplicity counting.... |
