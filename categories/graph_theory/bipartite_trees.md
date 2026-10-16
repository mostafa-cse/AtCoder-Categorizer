# 📖 Bipartite 2-Coloring of Trees & Pigeonhole Independent Set

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Trees`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Bipartite 2-Coloring of Trees & Pigeonhole Independent Set**.

---

## 🏆 Curated High-Value Problems

### Independent Set on a Tree (`[problem:AtCoder-typical90_z]`)

- **Role**: *Bipartite 2-Coloring of Trees & Pigeonhole Independent Set*
- **Rating**: `1200` (★4) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_z)
- **Full Analysis**: [AtCoder-typical90_z Analysis](../../analysis/AtCoder-typical90_z.md)

#### Problem Statement & Task
Given a tree with N vertices (N even), find an independent set of size exactly N / 2.

#### Core Invariant & Observation
By the Pigeonhole Principle, at least one of the two color classes must contain at least N / 2 vertices. Any subset of an independent set is independent; output any N/2 vertices from the larger class.

#### Algorithmic Formulation
1. Run BFS/DFS from vertex 1 to compute bipartite colors (0 and 1).
2. Group vertices by color: group0 and group1.
3. Take group with size >= N / 2.
4. Output first N / 2 vertices from that group.

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: Tree bipartiteness and pigeonhole principle independent set selection.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Bipartite coloring on trees and the pigeonhole principle for constructive subproblems.
- **Reusable Pattern**: `Bipartite 2-Coloring on Trees.`

---

[Back to Master Categories](../../README.md)
