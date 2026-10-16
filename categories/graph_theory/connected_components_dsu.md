# 📖 Connected Components & DSU Transitive Closure

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Connected Components`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Exploiting equivalence relations and transitive connectivity on undirected graphs using Disjoint Set Union (DSU) to compute component invariants and clique completions.

---

## 🏆 Curated High-Value Problems

### 1. New Friends (`[problem:AtCoder-abc350_d]`)

- **Role**: *Transitive Closure & Clique Completion via DSU*
- **Rating**: `1050` | **Contest**: [`abc350`](https://atcoder.jp/contests/abc350/tasks/abc350_d)
- **Full Analysis**: [AtCoder-abc350_d Analysis](../../analysis/AtCoder-abc350_d.md)

#### Problem Statement & Task
If A-B and B-C are friends, A and C can become friends. Count maximum possible new friendships.

#### Core Invariant & Observation
Edges can never form between disconnected components. Within any component of size S, all missing edges will eventually be added.

#### Algorithmic Formulation
1. Build DSU over all N vertices and M edges.
2. For each component root, find vertex count S and existing edge count E.
3. Total new edges = sum_{components} (S * (S - 1) / 2 - E).

**Complexity**: `Time: O(N + M * alpha(N)), Space: O(N).`  
**Editorial Alignment**: Transitive closure clique completion via DSU.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Transitive relations on graphs and component-wise clique maximization.
- **Reusable Pattern**: `DSU component aggregation and clique edge counting.`

---

[Back to Graph Theory Index](README.md) | [Back to Master Categories](../../README.md)
