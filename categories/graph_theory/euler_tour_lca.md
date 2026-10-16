# 📖 Euler Tour DFS Order + LCA for Minimal Subtree on Subset of Vertices

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Trees & LCA`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Euler Tour DFS Order + LCA for Minimal Subtree on Subset of Vertices**.

---

## 🏆 Curated High-Value Problems

### Preserve Connectivity (`[problem:AtCoder-typical90_ai]`)

- **Role**: *Euler Tour DFS Order + LCA for Minimal Subtree on Subset of Vertices*
- **Rating**: `2450` (★7) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ai)
- **Full Analysis**: [AtCoder-typical90_ai Analysis](../../analysis/AtCoder-typical90_ai.md)

#### Problem Statement & Task
Given a tree with N vertices, answer Q queries: each query gives K vertices V_1, ..., V_K. Find the minimum number of edges in a connected subgraph containing all K vertices.

#### Core Invariant & Observation
Sort the K query vertices by their DFS entry time in an Euler Tour: u_1, u_2, ..., u_K. The minimal subtree edge count is (1/2) * sum_{i=1}^K dist(u_i, u_{i+1}) with u_{K+1} = u_1.

#### Algorithmic Formulation
1. Run DFS to compute depth, binary lifting LCA table, and entry timestamp tin[u].
2. For each query: sort the K vertices by tin[u].
3. Sum dist(u_i, u_{i+1}) = depth[u_i] + depth[u_{i+1}] - 2 * depth[LCA(u_i, u_{i+1})].
4. Output sum / 2.

**Complexity**: `Time: O((N + Q*K) log N), Space: O(N log N).`  
**Editorial Alignment**: Euler Tour order cyclic distance sum for minimal connecting subtree.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Euler Tour vertex ordering, minimal spanning forest on trees, and LCA distance queries.
- **Reusable Pattern**: `Euler Tour Order + LCA Cyclic Distance.`

---

[Back to Master Categories](../../README.md)
