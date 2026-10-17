# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In base 3, any subset whose ternary digits consist strictly of $\{0, 1\}$ contains no 3-term arithmetic progression because $2b = a + c$ forces $a_i = b_i = c_i$ at every ternary digit. Appending a sufficiently large element $X > 2 \max(S')$ and shifting the entire set uniformly preserves the 3-AP free invariant while achieving the exact target sum $M$.
- Common Reductions: Construct a set of $N$ distinct integers in $[-10^7, 10^7]$ with sum $M$ such that no three elements form an arithmetic progression.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc145_d`](../../analysis/AtCoder-arc145_d.md) | D. Non Arithmetic Progression Set | 2297 | Construct a set of $N$ distinct integers in $[-10^7, 10^7]$ with sum $M$ such that no three elements form an arithmetic ... |
