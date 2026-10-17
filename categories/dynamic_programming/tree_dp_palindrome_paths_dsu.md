# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A tree path between $u$ and $v$ is a palindrome if and only if $u$ and $v$ have the same character ($find(u) = find(v)$ in DSU) and the subpath between the next step from $u$ towards $v$ and the next step from $v$ towards $u$ is also a palindrome.
- Common Reductions: In a tree with $N$ vertices and given binary constraints $A_{u, v} = 1$ indicating path $(u, v)$ is a palindrome, find the maximum possible number of palindromic simple paths over all valid character assignments.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc198_d`](../../analysis/AtCoder-arc198_d.md) | D. Tree Palindrome | 2299 | In a tree with $N$ vertices and given binary constraints $A_{u, v} = 1$ indicating path $(u, v)$ is a palindrome, find t... |
