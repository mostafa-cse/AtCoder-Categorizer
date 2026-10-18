# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: To maximize the prefix balance everywhere, all '?' converted to '(' must appear as early as possible (before a split point mid), while all '?' converted to ')' must appear after mid. The prefix balance condition decomposes into two independent range minimum queries over prefix arrays.
- Common Reductions: Determine whether a substring with '?' wildcards can be completed into a regular bracket sequence. A valid bracket sequence requires that the total balance is 0 and all prefix balances remain non-negative.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-mujin_pc_2016_d`](../../analysis/AtCoder-mujin_pc_2016_d.md) | D. Parenthesis Sequence | 2404 | Determine whether a substring with '?' wildcards can be completed into a regular bracket sequence. A valid bracket seque... |
