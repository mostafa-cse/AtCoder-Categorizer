# 📖 Two-Way Bidirectional Dijkstra

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Shortest Paths`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Decomposing intermediate node constraints along paths into independent single-source shortest path passes from source and target endpoints.

---

## 🏆 Curated High-Value Problems

### 1. Passing (`[problem:AtCoder-typical90_m]`)

- **Role**: *Dual-Source Dijkstra Intermediate Distance Queries*
- **Rating**: `1350` | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_m)
- **Full Analysis**: [AtCoder-typical90_m Analysis](../../analysis/AtCoder-typical90_m.md)

#### Problem Statement & Task
For every vertex k from 1 to N, find the shortest path from vertex 1 to vertex N passing through k.

#### Core Invariant & Observation
Running Dijkstra only twice (from vertex 1 and from vertex N) precomputes dist1 and distN, allowing O(1) query response for all k.

#### Algorithmic Formulation
1. Run Dijkstra from node 1 -> dist1 array.
2. Run Dijkstra from node N -> distN array.
3. For each k in 1..N: output dist1[k] + distN[k].

**Complexity**: `Time: O(M log N), Space: O(N + M).`  
**Editorial Alignment**: Two-source bidirectional Dijkstra.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Decomposing multi-point shortest path queries into two independent single-source runs.
- **Reusable Pattern**: `Dual Dijkstra intermediate point distance query.`

---

[Back to Graph Theory Index](README.md) | [Back to Master Categories](../../README.md)
