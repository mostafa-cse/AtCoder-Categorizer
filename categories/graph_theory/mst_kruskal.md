# 📖 Difference Array Graph Transformation & Minimum Spanning Tree (Kruskal)

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Minimum Spanning Tree (MST)`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Difference Array Graph Transformation & Minimum Spanning Tree (Kruskal)**.

---

## 🏆 Curated High-Value Problems

### Flip Digits 2 (`[problem:AtCoder-typical90_aw]`)

- **Role**: *Difference Array Graph Transformation & Minimum Spanning Tree (Kruskal)*
- **Rating**: `2150` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_aw)
- **Full Analysis**: [AtCoder-typical90_aw Analysis](../../analysis/AtCoder-typical90_aw.md)

#### Problem Statement & Task
Binary string of length N. M operations with cost C_i flip bits in [L_i, R_i]. Find minimum cost to make it possible to reach any binary string, or -1 if impossible.

#### Core Invariant & Observation
Flipping [L, R] adds an edge between vertex L - 1 and vertex R in a graph of N + 1 vertices! Reaching all 2^N states is equivalent to the graph being connected. The minimum cost to connect N + 1 vertices is the Minimum Spanning Tree (Kruskal's algorithm)!

#### Algorithmic Formulation
1. Create graph with N + 1 vertices (0 to N).
2. For each operation (C, L, R): add edge between L - 1 and R with weight C.
3. Run Kruskal's MST algorithm using DSU.
4. If MST connects all N + 1 vertices (uses N edges), return MST cost; else return -1.

**Complexity**: `Time: O(M log M), Space: O(N + M).`  
**Editorial Alignment**: Difference array range flip mapped to spanning tree on auxiliary graph.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: XOR range update reduction to edge connectivity and Kruskal's Minimum Spanning Tree.
- **Reusable Pattern**: `Difference Array Graph Reduction to MST.`

---

[Back to Master Categories](../../README.md)
