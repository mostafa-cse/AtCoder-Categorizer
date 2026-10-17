# Suffix Array

**Taxonomy Path**: `Strings` > `Suffix Structures` > `Suffix Array`

## Description
This topic focuses on suffix array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any valid 221 contiguous subsequence, interior blocks must satisfy $v_i = m_i$, while endpoint blocks can take $v$ elements from a block of length $m \ge v$. Transforming the RLE of $A$ into string $T$ by mapping $(v, m)$ to $(0)$ if $v > m$, $(v)$ if $v = m$, and $(v, 0, v)$ if $v < m$ establishes a bijection between 221-sequences and contiguous subarrays of $T$ that contain no 0. Counting distinct 0-free subarrays is solved via Suffix Array and LCP array.
- Common Reductions: A 221-sequence is a sequence where every run-length encoding block $(v, m)$ has $v = m$. Count the number of distinct 221-sequences that appear as contiguous subsequences of $A$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc452_g`](../../analysis/AtCoder-abc452_g.md) | G. 221 Substring | 2255 | A 221-sequence is a sequence where every run-length encoding block $(v, m)$ has $v = m$. Count the number of distinct 22... |
