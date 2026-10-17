# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each number i, exactly i-1 copies must appear before position x_i, and N-i copies must appear after position x_i. The prefix placement is an interval scheduling problem with deadlines x_i: processing i in increasing order of x_i and greedily placing copies in the leftmost available slots guarantees feasibility if one exists. Suffix placement is handled symmetrically from right to left in decreasing order of x_i.
- Common Reductions: Construct an array of length N^2 containing N copies of each 1..N such that the i-th occurrence of i is at index x_i. Solved by Earliest Deadline First (EDF) greedy scheduling.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-agc008_d]` | K-th K | 2164 | Construct an array of length N^2 containing N copies of each 1..N such that the i-th occurrence of i is at index x_i. So... |
