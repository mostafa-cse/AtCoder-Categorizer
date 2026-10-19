# Games on Arbitrary Graphs

**Taxonomy Path**: `Game Theory` > `Graph Games` > `Games on Arbitrary Graphs`

## Description
This topic focuses on games on arbitrary graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When K=1 or K=N, the end cells are protected from being flanked from the outer side, so placing a stone on the boundary grants permanent dominance over adjacent cells. In general, whichever player secures cell K or builds an un-flippable wall can guarantee victory. The game forms a finite acyclic DAG of board states where backwards induction and reachability analysis yields a closed-form decision based on relative distances |K - 1| and |N - K|.
- Common Reductions: Two players alternate placing white and black stones on an empty length-N strip, flipping contiguous opponent segments bounded by their own stones. The winner is determined by the stone color of cell K. By analyzing game state transitions and terminal configurations, the outcome reduces to identifying who controls boundary expansion and reachability to position K.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc109_e`](../../analysis/AtCoder-arc109_e.md) | 1D Reversi Builder | 2661 | Two players alternate placing white and black stones on an empty length-N strip, flipping contiguous opponent segments b... |
