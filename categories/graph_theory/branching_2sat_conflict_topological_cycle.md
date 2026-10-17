# Topological Sorting

**Taxonomy Path**: `Graph Theory` > `Graph Traversal` > `Topological Sorting`

## Description
This topic focuses on topological sorting techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each Type 2 constraint $(u, v)$ requires either $u$ is painted before $v$ (adding directed edge $u \to v$) or $u$ is never painted (marking $u$ as forbidden).
- Common Reductions: Given directed dependency constraints of Type 1 ($y$ must be painted before $x$) and Type 2 ($v$ must not be painted when painting $u$), find the maximum number of paintable vertices.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc049_c`](../../analysis/AtCoder-arc049_c.md) | C. ぬりまーす | 2308 | Given directed dependency constraints of Type 1 ($y$ must be painted before $x$) and Type 2 ($v$ must not be painted whe... |
