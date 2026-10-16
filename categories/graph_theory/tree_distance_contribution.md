# 📖 Contribution to the Sum / Edge Subtree Size Multiplication

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Trees`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Contribution to the Sum / Edge Subtree Size Multiplication**.

---

## 🏆 Curated High-Value Problems

### Tree Distance (`[problem:AtCoder-typical90_am]`)

- **Role**: *Contribution to the Sum / Edge Subtree Size Multiplication*
- **Rating**: `1500` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_am)
- **Full Analysis**: [AtCoder-typical90_am Analysis](../../analysis/AtCoder-typical90_am.md)

#### Problem Statement & Task
Given a tree with N vertices, compute the sum of distances between all N*(N - 1)/2 pairs of vertices: sum_{1 <= u < v <= N} dist(u, v).

#### Core Invariant & Observation
Removing an edge e partitions the tree into two subtrees of sizes sz and N - sz. Exactly sz * (N - sz) paths must cross edge e! The total sum of distances is sum_{e} (sz_e * (N - sz_e)).

#### Algorithmic Formulation
1. Run DFS from vertex 1 to calculate subtree sizes sz[u].
2. For each node u != 1: the edge to parent has contribution sz[u] * (N - sz[u]).
3. Sum contributions across all N - 1 edges.

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: Linear-time all-pairs tree distance via edge contribution.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Contribution to the Sum principle and tree bipartition counts per edge.
- **Reusable Pattern**: `Edge Contribution to All-Pairs Tree Distance.`

---

[Back to Master Categories](../../README.md)
