# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Operations fall into two categories: three evens (permutes 3 adjacent evens) and two odds + one even (moves an even past two odds). The feasibility of the latter is an invariant across the sequence. If two-odd operations are impossible, odds cannot move and act as fixed walls, allowing each even segment of length >= 3 to be independently sorted. If two-odd operations are possible, all elements can be freely permuted except when the count of evens is exactly 2, in which case their relative order is invariant.
- Common Reductions: Determine whether sequence A can be transformed into B by repeatedly rearranging any three consecutive elements whose sum is even.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc155_c`](../../analysis/AtCoder-arc155_c.md) | Even Sum Triplet | 2219 | Determine whether sequence A can be transformed into B by repeatedly rearranging any three consecutive elements whose su... |
