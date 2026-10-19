# DP on Trees and DAGs

**Taxonomy Path**: `Dynamic Programming (DP)` > `Dp on Different Structures` > `DP on Trees and DAGs`

## Description
This topic focuses on dp on trees and dags techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Marbles starting at different depths never interact because they are always at different depths at every time step. For a fixed depth d, exactly 1 marble reaches the root iff at each ancestor node, exactly 1 child sends a marble. This can be tracked using tree DP with states (c_0, c_1, c_2) representing 0, 1, or >= 2 marbles from the subtree. Merging children's deques small-to-large achieves O(N) total complexity.
- Common Reductions: Each node in a rooted tree independently starts with a marble with probability 1/2. Marbles move to parents each step, and colliding marbles vanish. Find the expected number of marbles that reach the root, times 2^(N+1) mod 1000000007.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc086_c`](../../analysis/AtCoder-arc086_c.md) | E - Smuggling Marbles | 2814 | Each node in a rooted tree independently starts with a marble with probability 1/2. Marbles move to parents each step, a... |
