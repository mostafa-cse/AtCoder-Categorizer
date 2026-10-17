# Dijkstra's Algorithm

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Dijkstra's Algorithm`

## Description
This topic focuses on dijkstra's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Standard multi-source Dijkstra from all popular people would only find the single shortest path, which might originate from the same country $A_i$. Because each person $i$ has only one forbidden country $A_i$, tracking the **top 2 shortest distances to popular people originating from distinct countries** at every vertex guarantees that for any vertex $i$, at least one of the top 2 shortest sources has country $\neq A_i$. Maintaining $(dist_1, country_1)$ and $(dist_2, country_2)$ with $country_1 \neq country_2$ in priority queue relaxation runs in $O((N + M) \log N)$.
- Common Reductions: In a graph of $N$ people and $M$ weighted edges, each person belongs to a country $A_i \in [1, K]$. There are $L$ popular people. For each person $i$, find the minimum cost path to any popular person belonging to a different country ($A_{popular} \neq A_i$), or -1 if impossible.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc245_g`](../../analysis/AtCoder-abc245_g.md) | G. Foreign Friends | 2270 | In a graph of $N$ people and $M$ weighted edges, each person belongs to a country $A_i \in [1, K]$. There are $L$ popula... |
