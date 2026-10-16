# 📖 K Distinct Topological Sorts via Kahn Backtracking

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Topological Sort`

---

## 💡 Topic Overview
High-value competitive programming techniques for **K Distinct Topological Sorts via Kahn Backtracking**.

---

## 🏆 Curated High-Value Problems

### Fuzzy Priority (`[problem:AtCoder-typical90_bs]`)

- **Role**: *K Distinct Topological Sorts via Kahn Backtracking*
- **Rating**: `2550` (★7) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bs)
- **Full Analysis**: [AtCoder-typical90_bs Analysis](../../analysis/AtCoder-typical90_bs.md)

#### Problem Statement & Task
Given a DAG with N vertices and M edges, output K distinct topological sort permutations, or output -1 if fewer than K distinct valid topological orderings exist.

#### Core Invariant & Observation
Maintain set of available in-degree 0 vertices. At each step, branch by selecting any available vertex. Terminate as soon as K permutations are collected, bounding search complexity.

#### Algorithmic Formulation
1. Compute in-degrees.
2. DFS(order, available_set):
   - If order.size() == N: record permutation; if collected K, stop.
   - For vertex u in available_set: branch, decrement child in-degrees, recurse, backtrack.

**Complexity**: `Time: O(K * (N + M)), Space: O(N + M).`  
**Editorial Alignment**: Backtracking search on Kahn's algorithm finding K topological sorts.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: K-shortest topological sorts, in-degree backtracking, and early termination on query budgets.
- **Reusable Pattern**: `Kahn Algorithm Backtracking for K Topological Sorts.`

---

[Back to Master Categories](../../README.md)
