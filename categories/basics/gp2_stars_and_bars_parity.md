# Stars and Bars

**Taxonomy Path**: `Basics` > `Basic Counting` > `Stars and Bars`

## Description
This topic focuses on stars and bars techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A sequence of non-negative integers is reachable after $M$ operations of adding 2 to one element and 1 to another iff: (1) $\sum x_i = 3M$, (2) number of odd elements $k \le M$ and $k \equiv M \pmod 2$, and (3) $\max x_i \le 2M$. Since at most one element can exceed $2M$, complementary counting over each valid odd count $k$ yields exact closed forms via stars and bars.
- Common Reductions: Characterize sequences reachable by $M$ operations of adding 2 to one element and 1 to another. Solved by stars and bars over each valid odd-element count $k \le M$ ($k \equiv M \pmod 2$) and subtracting the single exceeding element $> 2M$ in $O(N + M)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc036_c`](../../analysis/AtCoder-agc036_c.md) | C. GP 2 | 2357 | Characterize sequences reachable by $M$ operations of adding 2 to one element and 1 to another. Solved by stars and bars... |
