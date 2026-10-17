# BIT / Fenwick Tree

**Taxonomy Path**: `Data Structures (DS)` > `Binary Indexed Tree (BIT)` > `BIT / Fenwick Tree`

## Description
This topic focuses on bit / fenwick tree techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If a < b < c and c - a <= K, then both b - a <= K and c - b <= K. Thus, graph connectivity is completely determined by adjacent differences in sorted order of S. A component boundary occurs at any adjacent pair (u, v) with v - u > K. The component containing x is [L, R] where L is the successor of the nearest break < x (or min(S)), and R is the nearest break >= x (or max(S)).
- Common Reductions: Maintain a dynamic set S under insertions/deletions and compute the size of the connected component containing x in a graph with edges between points having distance <= K. Monotonicity implies components are contiguous sorted intervals where consecutive gaps are <= K. Track break points (gaps > K) in an ordered set and count elements in interval [L, R] using a Fenwick tree.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc356_f]` | Distance Component Size Query | 2152 | Maintain a dynamic set S under insertions/deletions and compute the size of the connected component containing x in a gr... |
