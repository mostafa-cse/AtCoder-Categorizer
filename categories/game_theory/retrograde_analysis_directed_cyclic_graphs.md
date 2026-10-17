# Games on Arbitrary Graphs

**Taxonomy Path**: `Game Theory` > `Graph Games` > `Games on Arbitrary Graphs`

## Description
This topic focuses on games on arbitrary graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When Takahashi says s_i, Aoki moves from vertex v = suffix3(s_i). In a finite impartial/normal play game on a directed graph with cycles: a state is LOSE if out-degree is 0 or all outgoing edges lead to WIN; a state is WIN if at least one outgoing edge leads to LOSE; all remaining undetermined states are DRAW. Retrograde BFS propagates known states backwards along reverse edges.
- Common Reductions: Model 3-character prefix/suffix word transitions as a directed graph. Determine whether Takahashi wins, Aoki wins, or the game draws if Takahashi plays word s_i first. Since cycles allow infinite play (Draw), classify vertex outcomes (Win/Lose/Draw) via retrograde analysis BFS on the reversed graph.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc209_e]` | Shiritori | 2153 | Model 3-character prefix/suffix word transitions as a directed graph. Determine whether Takahashi wins, Aoki wins, or th... |
