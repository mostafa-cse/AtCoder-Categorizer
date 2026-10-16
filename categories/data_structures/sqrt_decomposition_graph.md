# 📖 Square Root Decomposition on Graph Vertex Degrees (Heavy-Light)

- **Tag / Domain**: `Data Structures (DS)`
- **Subtopic**: `Square Root Decomposition`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Square Root Decomposition on Graph Vertex Degrees (Heavy-Light)**.

---

## 🏆 Curated High-Value Problems

### Colorful Graph (`[problem:AtCoder-typical90_ce]`)

- **Role**: *Square Root Decomposition on Graph Vertex Degrees (Heavy-Light)*
- **Rating**: `2300` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ce)
- **Full Analysis**: [AtCoder-typical90_ce Analysis](../../analysis/AtCoder-typical90_ce.md)

#### Problem Statement & Task
Graph with N, M <= 2*10^5. Q <= 2*10^5 queries: given (x, y), print color of vertex x, then color x and all its neighbors with color y.

#### Core Invariant & Observation
There are at most 2M / B <= 2 * sqrt(M) heavy vertices. Light vertices query all neighbors in O(B). Heavy vertices push updates to light neighbors or keep a timestamp tag checked by adjacent heavy nodes.

#### Algorithmic Formulation
1. Threshold B = sqrt(2 * M).
2. Vertices with deg >= B are Heavy.
3. For each vertex: keep list of adjacent heavy vertices.
4. Query (x, y): determine color of x by checking x's own color vs latest timestamp among heavy neighbors. Color x and update x.

**Complexity**: `Time: O((N + M + Q) * sqrt(M)), Space: O(N + M).`  
**Editorial Alignment**: Square root decomposition on vertex degrees partitioning into heavy and light hubs.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Sqrt decomposition on graphs, heavy-light degree balancing, and lazy timestamped propagation.
- **Reusable Pattern**: `Heavy-Light Vertex Degree Sqrt Decomposition.`

---

[Back to Master Categories](../../README.md)
