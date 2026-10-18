# Cycle Detection

**Taxonomy Path**: `Graph Theory` > `Cycles` > `Cycle Detection`

## Description
This topic focuses on cycle detection techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: With '(' as $+1$ and ')' as $-1$, a closed walk covering all edges can balance to 0 while keeping all prefix sums $\ge 0$ iff either: (1) both positive and negative cycles exist (allowing arbitrary balance pump and deflation), or (2) all cycles have weight 0 (potential field ensures zero net sum). A walk is impossible iff strictly one sign of cycles exists.
- Common Reductions: Determine if a strongly connected graph with '(' and ')' edges admits a closed walk covering every edge that forms a regular bracket sequence.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc173_d`](../../analysis/AtCoder-arc173_d.md) | D. Bracket Walk | 2598 | Determine if a strongly connected graph with '(' and ')' edges admits a closed walk covering every edge that forms a reg... |
