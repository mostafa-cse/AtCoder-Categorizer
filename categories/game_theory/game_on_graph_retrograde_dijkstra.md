# Games on Arbitrary Graphs

**Taxonomy Path**: `Game Theory` > `Graph Games` > `Games on Arbitrary Graphs`

## Description
This topic focuses on games on arbitrary graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: This is a zero-sum game on a graph with positive edge weights, solvable by Retrograde Dijkstra (value iteration on game graphs). Let $D[0][u]$ be the game value from $u$ when First Player moves, and $D[1][u]$ when Second Player moves. Terminal vertices (out-degree 0) have $D[0][t] = D[1][t] = 0$. In retrograde analysis:
- First Player (Min) can choose ANY outgoing edge, so $D[0][u] = \min_{(u, v)} (D[1][v] + c)$. The first time an edge reaches $u$ in Dijkstra, $D[0][u]$ is finalized.
- Second Player (Max) will choose the WORST option for First Player. Second Player's value $D[1][u] = \max_{(u, v)} (D[0][v] + c)$ can only be finalized when ALL outgoing moves from $u$ have been determined (i.e. remaining outgoing degree drops to 0)! The final edge that closes the degree determines the maximum.
- Common Reductions: A game is played on a directed graph with edge weights $c_e \ge 0$. A token starts at vertex $v$. First Player wants to minimize total cost; Second Player wants to maximize total cost. At any step, the active player chooses an outgoing edge $(u, w)$, paying $c_e$ to the total score. If the active player cannot move (out-degree 0), the game ends. If Second Player can force infinite loops, cost is $\infty$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc261_h`](../../analysis/AtCoder-abc261_h.md) | Ex. Game on Graph | 2531 | A game is played on a directed graph with edge weights $c_e \ge 0$. A token starts at vertex $v$. First Player wants to ... |
