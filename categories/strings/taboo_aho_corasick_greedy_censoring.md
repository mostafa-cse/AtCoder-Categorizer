# Aho Corasick

**Taxonomy Path**: `Strings` > `Aho Corasick` > `Aho Corasick`

## Description
This topic focuses on aho corasick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Greedy choice property: modifying the rightmost character of the detected forbidden substring maximizes disruption to any future overlapping forbidden substrings. When the current character is modified, the automaton resets to the root in $O(1)$ time, guaranteeing minimum total modifications.
- Common Reductions: Given string $S$ and $N$ forbidden substrings $T_1 \dots T_N$, find the minimum character modifications to make $S$ contain no $T_i$ as a substring. Build the Aho-Corasick automaton on $T_1 \dots T_N$. Mark any node as forbidden if it matches a $T_i$ or its suffix link points to a forbidden node. Walk through $S$ character by character: the moment we enter a forbidden node, we greedily modify the current character to a wildcard, resetting the automaton state to root.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc268_h`](../../analysis/AtCoder-abc268_h.md) | Ex. Taboo | 2560 | Given string $S$ and $N$ forbidden substrings $T_1 \dots T_N$, find the minimum character modifications to make $S$ cont... |
