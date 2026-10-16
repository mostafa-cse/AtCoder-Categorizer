# 🕸️ AtCoder Curriculum: Graph Theory

Curated collection of high-value problems in **Graph Theory** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.

- **Total Curated Problems**: 4
- **Taxonomy Tier**: Tag (Domain Level)

---

## 📑 Table of Contents

- [Connected Components](#connected-components)
  - [Disjoint Set Union (DSU) / Connected Component Cliques](#disjoint-set-union-dsu--connected-component-cliques) (1 problems)
- [Directed Graphs](#directed-graphs)
  - [Cycle Detection / Functional Graph Component Analysis](#cycle-detection--functional-graph-component-analysis) (1 problems)
- [Shortest Paths](#shortest-paths)
  - [Two-Way Dijkstra / Intermediate Node Shortest Paths](#two-way-dijkstra--intermediate-node-shortest-paths) (1 problems)
- [Trees](#trees)
  - [Tree Diameter / Double BFS-DFS](#tree-diameter--double-bfs-dfs) (1 problems)

---

## Connected Components

### Disjoint Set Union (DSU) / Connected Component Cliques

#### New Friends (`[problem:AtCoder-abc350_d]`)
- **Rating / Difficulty**: 1050
- **Contest**: `abc350` | [AtCoder Link](https://atcoder.jp/contests/abc350/tasks/abc350_d)
- **Detailed Analysis**: [`analysis/AtCoder-abc350_d.md`](../analysis/AtCoder-abc350_d.md)
- **Key Idea**: If A-B and B-C are friends, A and C can become friends. Calculate maximum new operations.
- **Core Observation**: The operation creates the transitive closure of the graph. Every connected component of size S will eventually become a complete graph (clique) with S*(S-1)/2 edges.
- **Algorithm & Complexity**: Time: O(N + M * alpha(N)), Space: O(N).
- **What This Problem Teaches**: Transitive relations on graphs and component-wise clique maximization.
- **Reusable Pattern**: `DSU component aggregation and clique edge counting.`

---

## Directed Graphs

### Cycle Detection / Functional Graph Component Analysis

#### Change of User Name (`[problem:AtCoder-abc285_d]`)
- **Rating / Difficulty**: 950
- **Contest**: `abc285` | [AtCoder Link](https://atcoder.jp/contests/abc285/tasks/abc285_d)
- **Detailed Analysis**: [`analysis/AtCoder-abc285_d.md`](../analysis/AtCoder-abc285_d.md)
- **Key Idea**: N users want to change their handles from S_i to T_i. Determine if all changes can be performed without handle collisions.
- **Core Observation**: Build directed graph with edge S_i -> T_i. A valid sequence of changes exists if and only if the directed graph contains NO directed cycle.
- **Algorithm & Complexity**: Time: O(N), Space: O(N).
- **What This Problem Teaches**: Modeling sequential dependencies as directed graph cycles and topological ordering.
- **Reusable Pattern**: `Topological sort cycle detection for dependency resolution.`

---

## Shortest Paths

### Two-Way Dijkstra / Intermediate Node Shortest Paths

#### Passing (`[problem:AtCoder-typical90_m]`)
- **Rating / Difficulty**: 1350
- **Contest**: `typical90` | [AtCoder Link](https://atcoder.jp/contests/typical90/tasks/typical90_m)
- **Detailed Analysis**: [`analysis/AtCoder-typical90_m.md`](../analysis/AtCoder-typical90_m.md)
- **Key Idea**: For every vertex k from 1 to N, find the shortest path from vertex 1 to vertex N passing through k.
- **Core Observation**: Shortest path from 1 to N through k is dist(1, k) + dist(k, N). Since edges are bidirectional, dist(k, N) = dist(N, k). Running Dijkstra only twice (from 1 and from N) resolves all queries in O(1).
- **Algorithm & Complexity**: Time: O(M log N), Space: O(N + M).
- **What This Problem Teaches**: Decomposing multi-point shortest path queries into two independent single-source runs.
- **Reusable Pattern**: `Dual Dijkstra intermediate point distance query.`

---

## Trees

### Tree Diameter / Double BFS-DFS

#### Longest Circular Road (`[problem:AtCoder-typical90_c]`)
- **Rating / Difficulty**: 1100
- **Contest**: `typical90` | [AtCoder Link](https://atcoder.jp/contests/typical90/tasks/typical90_c)
- **Detailed Analysis**: [`analysis/AtCoder-typical90_c.md`](../analysis/AtCoder-typical90_c.md)
- **Key Idea**: Add one edge between any two vertices in a tree to form the longest possible cycle.
- **Core Observation**: Adding edge (u, v) creates a cycle of length dist(u, v) + 1. The maximum distance in a tree is by definition the diameter of the tree.
- **Algorithm & Complexity**: Time: O(N), Space: O(N).
- **What This Problem Teaches**: Tree diameter characterization and the canonical 2-BFS algorithm.
- **Reusable Pattern**: `2-pass BFS tree diameter.`

---
