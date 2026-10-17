# DSU / Union Find

**Taxonomy Path**: `Data Structures (DS)` > `Disjoint Set Union (DSU)` > `DSU / Union Find`

## Description
This topic focuses on dsu / union find techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Being a level K palindrome forces mirror equalities across K recursive halving steps. If at any step length is 0, or final base string length L0 == 1, it is impossible (a length 1 string is always a palindrome, never level 0). If L0 >= 2, the base string t0 must NOT be a palindrome. If the greedy majority character assignment forms a palindrome, change one position to its second-best character at minimum penalty.
- Common Reductions: DSU equivalence class grouping across recursive palindrome halving with optimal majority character assignment and parity breaking.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-jsc2021_e`](../../analysis/AtCoder-jsc2021_e.md) | Level K Palindrome | 2213 | DSU equivalence class grouping across recursive palindrome halving with optimal majority character assignment and parity... |
