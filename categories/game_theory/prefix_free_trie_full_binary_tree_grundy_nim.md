# Grundy Number and Basic Game Theory

**Taxonomy Path**: `Game Theory` > `Grundy Number / Nim` > `Grundy Number and Basic Game Theory`

## Description
This topic focuses on grundy number and basic game theory techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Any available subtree in the trie is completely disjoint from all other available subtrees, making the game an impartial sum of independent games. A full binary tree with distance h to leaves has Grundy value equal to lowbit(h + 1) = lowbit(L - d).
- Common Reductions: Model the prefix-free string game on a complete binary tree of depth L as an independent sum of games on missing subtrees in the trie, where each full binary subtree of depth d has Grundy value lowbit(L - d).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc087_c`](../../analysis/AtCoder-arc087_c.md) | Prefix-free Game | 2431 | Model the prefix-free string game on a complete binary tree of depth L as an independent sum of games on missing subtree... |
