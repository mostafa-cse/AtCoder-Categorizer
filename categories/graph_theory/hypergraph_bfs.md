# 📖 Auxiliary Intermediate Node for Clique / Hypergraph Compression in BFS

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Graph Modeling & Transformations`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Auxiliary Intermediate Node for Clique / Hypergraph Compression in BFS**.

---

## 🏆 Curated High-Value Problems

### Takahashi Number (`[problem:AtCoder-typical90_bb]`)

- **Role**: *Auxiliary Intermediate Node for Clique / Hypergraph Compression in BFS*
- **Rating**: `2150` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bb)
- **Full Analysis**: [AtCoder-typical90_bb Analysis](../../analysis/AtCoder-typical90_bb.md)

#### Problem Statement & Task
N authors, M research papers. Paper i is co-authored by K_i authors. Co-authors have collaboration distance 1. Find the Takahashi number (shortest distance from author 1) for all authors.

#### Core Invariant & Observation
For paper i, add undirected edges between paper node P_i and each of its authors. Distance between authors in the auxiliary bipartite graph is exactly 2 * original_distance.

#### Algorithmic Formulation
1. Build bipartite graph with N + M vertices (1..N authors, N+1..N+M papers).
2. For paper j: add edge between author u and paper node N + j.
3. Run standard unweighted BFS from author 1.
4. For author i: distance is dist[i] / 2 (or -1 if unreachable).

**Complexity**: `Time: O(N + sum K_i), Space: O(N + sum K_i).`  
**Editorial Alignment**: Bipartite auxiliary node graph modeling for hyperedge / clique reduction.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Replacing quadratic clique edges with auxiliary star hubs and hypergraph BFS.
- **Reusable Pattern**: `Auxiliary Hub Node Clique Compression.`

---

[Back to Master Categories](../../README.md)
