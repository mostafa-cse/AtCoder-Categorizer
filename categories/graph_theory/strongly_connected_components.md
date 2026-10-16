# 📖 Strongly Connected Components (SCC) / Tarjan & Kosaraju

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Directed Graphs`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Strongly Connected Components (SCC) / Tarjan & Kosaraju**.

---

## 🏆 Curated High-Value Problems

### Come Back in One Piece (`[problem:AtCoder-typical90_u]`)

- **Role**: *Strongly Connected Components (SCC) / Tarjan & Kosaraju*
- **Rating**: `1750` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_u)
- **Full Analysis**: [AtCoder-typical90_u Analysis](../../analysis/AtCoder-typical90_u.md)

#### Problem Statement & Task
Given a directed graph with N vertices and M edges, count the number of pairs of vertices (u, v) with u < v such that u can reach v and v can reach u.

#### Core Invariant & Observation
Decompose the graph into SCCs. Each SCC of size S contributes C(S, 2) = S*(S - 1)/2 mutually reachable pairs.

#### Algorithmic Formulation
1. Build adjacency list G and reversed graph G_rev.
2. DFS 1 on G: record vertices in order of post-order finish time.
3. DFS 2 on G_rev in reverse finish order: extract connected components.
4. For each component of size S: add S * (S - 1) / 2 to total count.

**Complexity**: `Time: O(N + M), Space: O(N + M).`  
**Editorial Alignment**: Kosaraju's two-pass Strongly Connected Components algorithm.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Strongly Connected Components, mutual reachability equivalence classes, and Kosaraju/Tarjan linear-time decomposition.
- **Reusable Pattern**: `Kosaraju / Tarjan Strongly Connected Components.`

---

[Back to Master Categories](../../README.md)
