# Basic Greedy Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Greedy Algorithms`

## Description
This topic focuses on basic greedy algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A number $z$ remains a non-representable hole after adding $A_i$ if and only if $z$ was a hole before adding $A_i$ and $z - A_i$ was also a hole before adding $A_i$. Any hole strictly smaller than $A_i$ can never be eliminated by any subsequent element $\ge A_i$.
- Common Reductions: Given a multiset $A$ of $N$ positive integers, find the $K$ smallest positive integers that cannot be represented as the sum of a subset of $A$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc062_c`](../../analysis/AtCoder-agc062_c.md) | C. Mex of Subset Sum | 2320 | Given a multiset $A$ of $N$ positive integers, find the $K$ smallest positive integers that cannot be represented as the... |
