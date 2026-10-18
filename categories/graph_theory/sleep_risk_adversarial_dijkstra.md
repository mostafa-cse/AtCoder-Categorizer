# Dijkstra's Algorithm

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Dijkstra's Algorithm`

## Description
This topic focuses on dijkstra's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When riding an edge e = (u -> v) on line L, falling asleep carries the passenger to the terminus T in that direction with penalty P(e) = dist_L(u, T) + d_{normal}(T). The optimal adversarial step from u minimizes max(w(e) + dp(v), P(e)), which defines a monotonic Dijkstra operator backwards from dst.
- Common Reductions: Find the path from src to dst minimizing worst-case travel time when falling asleep carries the commuter to the terminus. After computing baseline distances d_{normal} to dst, each line edge e = (u -> v) carries risk P(e) = dist(u, T) + d_{normal}(T). Reverse Dijkstra solving dp(u) = min_e max(w(e) + dp(v), P(e)) runs in O((N + \sum L_i) \log N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-dwango2016qual_c`](../../analysis/AtCoder-dwango2016qual_c.md) | C. メンテナンス明け | 2384 | Find the path from src to dst minimizing worst-case travel time when falling asleep carries the commuter to the terminus... |
