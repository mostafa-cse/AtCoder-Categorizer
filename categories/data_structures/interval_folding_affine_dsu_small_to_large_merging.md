# DSU on Tree and Small to Large Merging

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `DSU on Tree and Small to Large Merging`

## Description
This topic focuses on dsu on tree and small to large merging techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Active pieces at any step form a symmetric pair of contiguous intervals [xmin, xmax] with affine mapping x(i) = scale * i + offset. When step distance d falls inside [xmin, xmax], the interval splits: pieces hitting d stop at step i, and the smaller sub-interval folds into the larger sub-interval with an inverted affine sign. Small-to-large merging guarantees total work O(M log M).
- Common Reductions: Simultaneously simulate 2M pieces starting at +/-1, ..., +/-M following M steps where at step i, pieces at x > 0 move to x - X_i and pieces at x < 0 move to x + X_i, stopping if they hit 0.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc149_d`](../../analysis/AtCoder-arc149_d.md) | D - Simultaneous Sugoroku | 2991 | Simultaneously simulate 2M pieces starting at +/-1, ..., +/-M following M steps where at step i, pieces at x > 0 move to... |
