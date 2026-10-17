# Basic SQRT Decomposition

**Taxonomy Path**: `Data Structures (DS)` > `Square Root Decomposition` > `Basic SQRT Decomposition`

## Description
This topic focuses on basic sqrt decomposition techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If $n = s$, the smallest base is $n + 1$. If $n < s$, no such base exists. For $s < n$, we partition into $b \le \sqrt{n}$ and $b > \sqrt{n}$. For $b \le \sqrt{n}$, directly simulate the digit sum in $O(\sqrt{n} \log n)$. For $b > \sqrt{n}$, $n$ has at most 2 digits: $n = p b + q$ with $p + q = s$, so $p(b - 1) = n - s$. Because $p \le \sqrt{n}$, we check all divisors $p$ of $n - s$ in $O(\sqrt{n})$.
- Common Reductions: Given integers $n$ and $s$, find the smallest integer base $b \ge 2$ such that the digit sum of $n$ in base $b$ equals $s$, or report -1 if impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc060_b`](../../analysis/AtCoder-arc060_b.md) | D. Digit Sum | 2261 | Given integers $n$ and $s$, find the smallest integer base $b \ge 2$ such that the digit sum of $n$ in base $b$ equals $... |
