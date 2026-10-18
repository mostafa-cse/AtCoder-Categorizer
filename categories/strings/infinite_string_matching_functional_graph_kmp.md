# Knuth Morris Pratt (KMP) and Prefix Automaton

**Taxonomy Path**: `Strings` > `String Matching` > `Knuth Morris Pratt (KMP) and Prefix Automaton`

## Description
This topic focuses on knuth morris pratt (kmp) and prefix automaton techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If string t matches in s^infinity at position p in [0, |s|-1], the next consecutive copy of t must start at (p + |t|) mod |s|. This defines a functional graph on |s| vertices where each vertex has out-degree <= 1. An infinite repetition exists iff there is a directed cycle; otherwise the maximum repetition count is the longest path in the DAG.
- Common Reductions: Find maximum repetitions of string t inside s^infinity. Repeating s to length >= |t| + |s| and finding match positions via KMP builds a functional graph on starting positions 0 .. |s|-1 with edge p -> (p + |t|) mod |s|. Detecting cycles (outputting -1) or finding the DAG longest path takes O(|s| + |t|) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc135_f`](../../analysis/AtCoder-abc135_f.md) | F. Strings of Eternity | 2388 | Find maximum repetitions of string t inside s^infinity. Repeating s to length >= |t| + |s| and finding match positions v... |
