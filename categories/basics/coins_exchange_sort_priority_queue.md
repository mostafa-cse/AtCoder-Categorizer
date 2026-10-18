# Priority Queue / Heap

**Taxonomy Path**: `Basics` > `Standard Template Library (STL)` > `Priority Queue / Heap`

## Description
This topic focuses on priority queue / heap techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Give everyone bronze coins as base sum sum C_i. Person i provides net gain A_i - C_i for gold and B_i - C_i for silver. By exchange argument, people chosen for gold lie to the left of people chosen for silver when sorted in descending order of (A_i - B_i).
- Common Reductions: Given N = X + Y + Z people where person i has A_i gold, B_i silver, and C_i bronze coins. Select X people for gold, Y for silver, and Z for bronze to maximize total coins.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc018_c`](../../analysis/AtCoder-agc018_c.md) | C. Coins | 2618 | Given N = X + Y + Z people where person i has A_i gold, B_i silver, and C_i bronze coins. Select X people for gold, Y fo... |
