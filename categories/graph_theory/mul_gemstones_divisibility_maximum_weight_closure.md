# Maximum Closure Problem

**Taxonomy Path**: `Graph Theory` > `Flow and Min Cut` > `Maximum Closure Problem`

## Description
This topic focuses on maximum closure problem techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If gem $y$ is kept, every divisor $x$ of $y$ must also be kept (otherwise smashing $x$ would have smashed $y$). Retaining a set of gems forms a closure on the divisibility DAG where $y \to x$ for all $x \mid y$. This is equivalent to Maximum Weight Closure via Dinic min-cut.
- Common Reductions: Smashing gem $x$ smashes all multiples $2x, 3x, \dots \le N$. Earn $a_i$ for each retained gem. Maximize total earnings.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc085_c`](../../analysis/AtCoder-arc085_c.md) | E. MUL | 2571 | Smashing gem $x$ smashes all multiples $2x, 3x, \dots \le N$. Earn $a_i$ for each retained gem. Maximize total earnings.... |
