# Interval Set

**Taxonomy Path**: `Miscellaneous` > `General` > `Interval Set`

## Description
This topic focuses on interval set techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because every harvest query overwrites the range [L, R] with the current day D, intervals of identical harvest dates are consolidated. Each query creates at most 2 new interval fragments, ensuring an amortized O(1) deletions per query.
- Common Reductions: Maintain trees' last harvest dates using an interval set (ODT) in std::set, computing harvested fruits via arithmetic progression formulas and consolidating queried ranges into single intervals in amortized O(Q log Q) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc255_h`](../../analysis/AtCoder-abc255_h.md) | Ex. Range Harvest Query | 2430 | Maintain trees' last harvest dates using an interval set (ODT) in std::set, computing harvested fruits via arithmetic pr... |
