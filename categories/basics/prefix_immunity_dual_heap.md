# Priority Queue / Heap

**Taxonomy Path**: `Basics` > `Standard Template Library (STL)` > `Priority Queue / Heap`

## Description
This topic focuses on priority queue / heap techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any prefix of monsters and $k$ amulets, it is strictly optimal to grant immunity to the $k$ monster types with the largest accumulated damage in that prefix.
- Common Reductions: Given $N$ monsters each with type $A_i$ and attack $B_i$, and $M$ amulet slots, find the maximum prefix of monsters that can be defeated when using $k$ amulets for each $k = 0, \dots, M$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc314_g`](../../analysis/AtCoder-abc314_g.md) | G. Amulets | 2301 | Given $N$ monsters each with type $A_i$ and attack $B_i$, and $M$ amulet slots, find the maximum prefix of monsters that... |
