# Green Hackenbush on Trees and Graphs

**Taxonomy Path**: `Game Theory` > `Hackenbush` > `Green Hackenbush on Trees and Graphs`

## Description
This topic focuses on green hackenbush on trees and graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: According to the Colon Principle in combinatorial game theory, attaching a subtree with Grundy value G(v) to a parent u via a single edge yields an equivalent game with Grundy value G(v) + 1. Multiple branches incident to the same root vertex behave as independent games summed via XOR: G(u) = XOR_{v in children(u)} (G(v) + 1). Alice wins iff G(root) != 0.
- Common Reductions: Determine the winner of Green Hackenbush on a rooted tree where players alternate cutting edges and components disconnected from the root are removed. Solved via the Colon Principle.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-agc017_d]` | Game on Tree | 2156 | Determine the winner of Green Hackenbush on a rooted tree where players alternate cutting edges and components disconnec... |
