# Stars and Bars

**Taxonomy Path**: `Basics` > `Basic Counting` > `Stars and Bars`

## Description
This topic focuses on stars and bars techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Adjacent differences $d_i = a_{i+1} - a_i \not\equiv 0 \pmod 3$ decompose as $x_i + 3y_i$ with $x_i \in \{1, 2\}$. Fixing the count of $x_i = 1$ leaves the non-negative integer solutions to $\sum y_i \le L = \lfloor(M-B)/3\rfloor$, which evaluates in $O(1)$ via the hockey stick identity.
- Common Reductions: Count the number of non-decreasing sequences $0 \le A_1 \le A_2 \le \dots \le A_N \le M$ such that $A_{i+1} - A_i \not\equiv 0 \pmod 3$ for all $1 \le i < N$, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc276_g`](../../analysis/AtCoder-abc276_g.md) | G. Count Sequences | 2278 | Count the number of non-decreasing sequences $0 \le A_1 \le A_2 \le \dots \le A_N \le M$ such that $A_{i+1} - A_i \not\e... |
