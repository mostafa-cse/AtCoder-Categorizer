# Stack

**Taxonomy Path**: `Basics` > `Standard Template Library (STL)` > `Stack`

## Description
This topic focuses on stack techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A planar tree embedding allows contractible boundary leaves. Consecutive duplicate values merge. A degree-1 leaf adjacent to 2 can be contracted, and a degree-4 node adjacent to 3 can be contracted. Repeatedly simulating these reductions on the circular sequence using a circular doubly-linked list / stack until no further operations are possible reveals that a valid tree exists if and only if the reduced cycle satisfies count(2) > count(4) and count(3) > count(1).
- Common Reductions: Given a circular sequence of vertex degrees A_1, ..., A_N in {1, 2, 3, 4}, determine if there exists a planar tree embedded in the plane with these cyclic boundary degrees.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc058_c`](../../analysis/AtCoder-agc058_c.md) | C - Planar Tree | 2991 | Given a circular sequence of vertex degrees A_1, ..., A_N in {1, 2, 3, 4}, determine if there exists a planar tree embed... |
